from behave import *
from hamcrest import *

from features.pages.SearchByModelPage import SearchByModelPage
from features.pages.SearchResultsPage import SearchResultsPage


@given('I own a {make} {model}')
def step_impl(context, make, model):
    context.bike['make'] = make
    context.bike['model'] = model
    context.bike['capacity'] = model[2:]


@when('I search by my model')
def step_impl(context):
    page = SearchByModelPage(context)
    page.opem()
    page.search_by_model(context.bike['model'], context.bike['capacity'])


@then('I should see some results')
def step_impl(context):
    model = context.bike['model'].replace(' ', '-')
    assert_that(context.driver.current_url, is_(equal_to_ignoring_case(f"https://www.davidsilverspares.co.uk/{model}/")))


@then('I should see an "{item}" in the list')
def step_impl(context, item):
    page = SearchResultsPage(context)
    assert_that(page.product_count_containing(item), is_(greater_than(0)))


@then(u'I should not see an "{item}" in the list')
def step_impl(context, item):
    page = SearchResultsPage(context)
    assert_that(page.product_count_containing(item), is_(less_than(1)))
