Feature: Logout Functionality

  Scenario: Successful logout
    Given user logs into application
    When user clicks logout button
    Then user should logout successfully