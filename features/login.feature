Feature: Login Functionality

  Scenario: Successful Login
    Given user opens login page
    When user enters valid email and password
    And user clicks login button
    Then user should login successfully