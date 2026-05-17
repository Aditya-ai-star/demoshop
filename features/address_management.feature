Feature: Address Management

  Scenario: Add new address
    Given user is logged in
    When user adds new address
    And user saves address
    Then address should be added successfully