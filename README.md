# Selenium with Python and pytest-bdd

## Overview
Selenium is a popular open-source tool for automating web browsers. It allows developers to simulate user interaction with web pages by writing scripts in a variety of programming languages, including Python.

pytest-bdd is a behavior-driven development (BDD) test framework for Python that allows developers to write tests in Gherkin syntax, which is a plain-text language that is easy to understand and maintain by non-technical stakeholders. pytest-bdd uses the power of the pytest testing framework to execute the tests and report the results.

## Installation
1. Clone this repository.
>git clone https://github.com/your_username/your_repository.git
2. Install Pipenv.
>pip install pipenv
3. Install the dependencies from the Pipfile.
>pipenv install
4. Run the project 
>pipenv run pytest .\steps\loginSteps.py

### Tech stack
As this is a Python project, build and dependency management is handled by Pipenv, so there is a `Pipfile` (and associated `.lock` file) defining the versions of the dependencies:
* Python v3.11
* Selenium v3.141.59
* Pytest v6.2.4
* Pytest BDD v4.1.0
* Webdriver-Manager v3.4.2
