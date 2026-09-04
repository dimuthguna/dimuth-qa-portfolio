Feature: SauceDemo checkout flow

  Scenario: User logs in successfully
    Given the user is on the SauceDemo login page
    When the user enters valid username and password
    And clicks the login button
    Then the user should see the products page

  Scenario: User adds an item to the cart
    Given the user is on the products page
    When the user adds an item to the cart
    Then the cart icon should show one item

  Scenario: User completes checkout
    Given the user has an item in the cart
    When the user proceeds to checkout and completes payment details
    Then the order confirmation message should be displayed
