from behave import given, when, then

BASE_URL = "https://www.saucedemo.com/"


@given("the user is on the SauceDemo login page")
def step_open_login_page(context):
    context.page.goto(BASE_URL)


@when("the user enters valid username and password")
def step_enter_credentials(context):
    page = context.page
    page.fill("#user-name", "standard_user")
    page.fill("#password", "secret_sauce")


@when("clicks the login button")
def step_click_login(context):
    page = context.page
    page.click("#login-button")


@then("the user should see the products page")
def step_verify_products_page(context):
    page = context.page
    page.wait_for_selector(".inventory_list")
    assert page.url == BASE_URL + "inventory.html"


@given("the user is on the products page")
def step_on_products_page(context):
    page = context.page
    if "inventory.html" not in page.url:
        page.goto(BASE_URL)
        page.fill("#user-name", "standard_user")
        page.fill("#password", "secret_sauce")
        page.click("#login-button")
        page.wait_for_selector(".inventory_list")


@when("the user adds an item to the cart")
def step_add_item_to_cart(context):
    page = context.page
    page.click(".inventory_item >> nth=0 >> button")


@then("the cart icon should show one item")
def step_verify_cart_badge(context):
    page = context.page
    badge = page.text_content(".shopping_cart_badge")
    assert badge == "1"


@given("the user has an item in the cart")
def step_item_in_cart(context):
    page = context.page
    if "inventory.html" not in page.url:
        page.goto(BASE_URL)
        page.fill("#user-name", "standard_user")
        page.fill("#password", "secret_sauce")
        page.click("#login-button")
        page.wait_for_selector(".inventory_list")
    badge_count = page.locator(".shopping_cart_badge").count()
    if badge_count == 0:
        page.click(".inventory_item >> nth=0 >> button")


@when("the user proceeds to checkout and completes payment details")
def step_checkout(context):
    page = context.page
    page.click(".shopping_cart_link")
    page.click("#checkout")
    page.fill("#first-name", "Dimuth")
    page.fill("#last-name", "Anjuka")
    page.fill("#postal-code", "28038")
    page.click("#continue")
    page.click("#finish")


@then("the order confirmation message should be displayed")
def step_verify_confirmation(context):
    page = context.page
    page.wait_for_selector(".complete-header")
    message = page.text_content(".complete-header")
    assert "Thank you" in message
