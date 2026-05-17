Feature: Product Sorting

  Scenario: Sort products by price
    Given user is on category page
    When user sorts products by price low to high
    Then products should be sorted successfully