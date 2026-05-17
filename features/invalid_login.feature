Feature: Invalid Login

  Scenario: Login with invalid credentials
    Given user opens login page for invalid login
    When user enters invalid email and password
    And user clicks login button for invalid login
    Then error message should be displayed