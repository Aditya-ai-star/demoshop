Feature: Search Product

  Scenario: Search product successfully
    Given user is on homepage
    When user searches for product
    Then searched product should be displayed