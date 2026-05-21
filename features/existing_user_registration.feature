Feature: Existing User Registration

  Scenario: Register with existing email
    Given user is on register page
    When user enters already registered email
    And user clicks register button
    Then registration should fail