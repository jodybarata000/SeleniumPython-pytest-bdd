Feature: Login Page
  Tests for the 'https://opensource-demo.orangehrmlive.com/' home page
  Background: Open home page
    Given User navigated to the OrangeHRM Login page

  Scenario: Login Valid Credentials
    When User Enters Valid username and password
    And User Clicks Login Button
    Then User redirects to OrangeHRM Dashboard
