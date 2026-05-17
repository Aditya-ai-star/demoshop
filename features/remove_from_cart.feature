Feature: Remove Product From Cart

  Scenario: Remove product from cart successfully
    Given user has product in cart
    When user removes product from cart
    Then cart should become empty