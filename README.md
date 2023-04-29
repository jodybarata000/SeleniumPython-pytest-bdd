# SeleniumPython-pytest-bdd


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
