Feature: Order Confirmation

  Scenario: Confirm order successfully
    Given user completes checkout process
    When user confirms the order
    Then order should be placed successfully