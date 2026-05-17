Feature: Add Product To Cart

  Scenario: Add product to cart successfully
    Given user opens homepage
    When user adds product to cart
    Then product should be added successfully