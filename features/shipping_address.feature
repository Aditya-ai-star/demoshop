Feature: Shipping Address

  Scenario: Add shipping address
    Given user is on checkout page
    When user enters shipping address
    Then shipping address should be saved