Feature: Payment Information

  Scenario: Verify payment information page
    Given user is on payment information page
    When user continues payment information
    Then payment information should be processed