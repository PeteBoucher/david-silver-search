Feature: As a customer I should be able to find any part for my bike

  Scenario: Happy path
    Given I own a Honda CB200 TWIN
    When I search by my model
    Then I should see some results
    And I should see an "Exhaust silencer and downpipe, Right hand" in the list

  Scenario: Sad path
    Given I own a Honda CB200 TWIN
    When I search by my model
    Then I should see some results
    And I should not see an "Exhaust silencer and downpipe, Left hand" in the list