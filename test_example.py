import allure
import pytest

@allure.parent_suite("Tests for web interface")
@allure.suite("Tests for essential features")
@allure.sub_suite("Tests for authentication")
@pytest.mark.parametrize("auth", [str(x) for x in range(1, 30)])
@allure.title("Test Authentication (as {auth})")
@allure.description("This test attempts to log into the website using a login and a password. ")
@allure.tag("NewUI", "Essentials", "Authentication")
@allure.severity(allure.severity_level.CRITICAL)
@allure.label("owner", "chaocw")
@allure.link("https://dev.example.com/", name="Website")
@allure.issue("AUTH-{auth}")
@allure.testcase("TMS-AUTH-{auth}")
def test_authentication(auth):
    ...

@allure.epic("Tests for web page")
@allure.feature("Tests for essential features")
@allure.story("Tests for order")
@pytest.mark.parametrize("order", [str(x) for x in range(1, 30)])
@allure.title("Test Order (as {order})")
@allure.description("This test attempts to log into the website using a login and a password.")
@allure.tag("NewUI", "Essentials", "Order")
@allure.severity(allure.severity_level.NORMAL)
@allure.label("owner", "chaocw")
@allure.link("https://dev.example.com/", name="Website")
@allure.issue("ORDER-{order}")
@allure.testcase("TMS-ORDER-{order}")
def test_order(order):
    ...
