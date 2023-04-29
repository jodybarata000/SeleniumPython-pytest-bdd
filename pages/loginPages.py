from pages.loginElements import LoginElements

class LoginPage(LoginElements):

    def userEntersUsername(self,username):
        return self.entertext(LoginElements.getUsernameTextField(self), username)

    def userEntersPassword(self,password):
        return self.entertext(LoginElements.getPasswordTextField(self), password)

    def userClickLoginButton(self):
        return self.clickElement(LoginElements.getLoginButton(self))

    def userRedirectToOrangeHRMDashboard(self):
        return self.waitUntileElementDisplayed(LoginElements.getDashboardText(self))
