Feature: User Registration

  Scenario: Register new user successfully
    Given user opens registration page
    When user enters registration details
    And user clicks register button
    Then user should register successfully