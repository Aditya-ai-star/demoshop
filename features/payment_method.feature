Feature: Payment Method

  Scenario: Select payment method
    Given user is on payment page
    When user selects payment method
    Then payment method should be selected