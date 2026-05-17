Feature: Shipping Method

  Scenario: Select shipping method
    Given user is on shipping method page
    When user selects shipping method
    Then shipping method should be selected