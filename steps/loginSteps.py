from pytest_bdd import scenarios, when, then, parsers
from pages.loginPages import LoginPage

scenarios('../features/loginTest.feature')

@when('User Enters Valid username and password')
def userEntersValidUsernameandPassword(browser):
    LoginPage(browser).userEntersUsername("Admin")


@when('User Clicks Login Button')
def userClicksLoginButton(browser):
    LoginPage(browser).userEntersPassword("admin123")
    LoginPage(browser).userClickLoginButton()


@then('User redirects to OrangeHRM Dashboard')
def userRedirectsToOrangeHRMDashboard(browser):
    LoginPage(browser).userRedirectToOrangeHRMDashboard()