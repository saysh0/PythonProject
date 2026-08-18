import pytest
from playwright.sync_api import sync_playwright, Page

site_url = "https://www.saucedemo.com/"
username = "standard_user"
password = "secret_sauce"

items = ["Sauce Labs Backpack", "Sauce Labs Bolt T-Shirt", "Sauce Labs Onesie"]

first_name = "Nikita"
last_name = "Ormandzhan"
post_code = "99000"

total_value = "$58.29"


class LoginPage:
    username_input = "#user-name"
    password_input = "#password"
    log_in = "#login-button"

    def __init__(self, page: Page):
        self.page = page

    def open(self):
        self.page.goto(site_url)

    def login(self, username: str, password: str):
        self.page.fill(self.username_input, username)
        self.page.fill(self.password_input, password)
        self.page.click(self.log_in)


class InventoryPage:
    bucket = ".shopping_cart_link"

    def __init__(self, page: Page):
        self.page = page

    def add_to_cart(self, product_name: str):
        (self.page.locator(".inventory_item").filter(has_text=product_name).locator("button").click())

    def add_multiple_to_cart(self, *product_names: str):
        for name in product_names:
            self.add_to_cart(name)

    def go_to_cart(self):
        self.page.click(self.bucket)


class CartPage:
    checkout = "#checkout"

    def __init__(self, page: Page):
        self.page = page

    def go_to_checkout(self):
        self.page.click(self.checkout)


class CheckoutPage:
    first_name_input = "#first-name"
    last_name_input = "#last-name"
    postal_code_input = "#postal-code"
    continue_button = "#continue"
    total_label = ".summary_total_label"

    def __init__(self, page: Page):
        self.page = page

    def put_personal_info(self, first_name: str, last_name: str, postal_code: str):
        self.page.fill(self.first_name_input, first_name)
        self.page.fill(self.last_name_input, last_name)
        self.page.fill(self.postal_code_input, postal_code)
        self.page.click(self.continue_button)

    def get_total(self) -> str:
        return self.page.locator(self.total_label).text_content()


@pytest.fixture(scope="function")
def browser_page():
    with sync_playwright() as p:
        browser = p.firefox.launch(headless=True)
        page = browser.new_page()
        yield page
        browser.close()


def test_checkout_total(browser_page):
    login_page = LoginPage(browser_page)
    login_page.open()
    login_page.login(username, password)

    inventory_page = InventoryPage(browser_page)
    inventory_page.add_multiple_to_cart(*items)
    inventory_page.go_to_cart()

    cart_page = CartPage(browser_page)
    cart_page.go_to_checkout()

    checkout_page = CheckoutPage(browser_page)
    checkout_page.put_personal_info(first_name, last_name, post_code)

    total_text = checkout_page.get_total()

    assert total_value in total_text, (f"Ожидали: {total_value}, получили: {total_text}")
