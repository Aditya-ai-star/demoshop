Feature: Billing Address

  Scenario: Add billing address
    Given user proceeds to checkout
    When user enters billing address
    Then billing address should be saved