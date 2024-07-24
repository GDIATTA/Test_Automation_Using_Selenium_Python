### Test_Automation_Using_Selenium_Python

------------------------ **TEST - AUTOMATION USING SELENIUM AND PYTHON** ------------------ 

**Selenium** is an open source automation tool used for interacting with web applications for testing purposes.<br>

-1. **How can you use selenium with python for automatic test ?**<br>

That's two ways to do a automatic test using **python** and **selenium** :<br>

**Way 1 :** <br>

First, you will need to configure the coding environment. This involves :<br>

> Downloading the ChromeDriver corresponds to our Chrome browser version(if you're using Chrome).<br>
> Installing the "selenium" package.<br>

Second time, you need to write the code to perform the test<br>

**Way2 :**<br>

First you need to configure the coding environment. Follow these steps :<br>

> 1. Create the project folder.<br>
> 2. Install pipenv by running: **pip install pipenv**.<br>
> 3. Locate where pipenv is installed by running: python -m site --user-base. Copy the directory path and add it to the system environment variables. Verify the pipenv installation by running: **pipenv --version**.<br>
> 4. Activate the project folder by running: pipenv shell.<br>
> 5. Install the necessary packages (selenium and pytest) using pipenv: pipenv install selenium pytest. Verify the installation by running: pip list and pipenv graph.<br>
> 6. Create a file structure in the project folder as follows:<br>
├── **Pipfile**
├── **Pipfile.lock**
├── **pytest.ini**
└── **tests**
    ├── __init__.py
    ├── **conftest.py**
    ├── **pages**
    │   ├── **login_page.py**
    │   └── **search_page.py**
    ├── **test_basic_selenium.py**
    └── **test_pom.py**

To do this, follow these steps:<br>
**mkdir tests**
**New-Item -ItemType File -Name Pipfile**
**New-Item -ItemType File -Name pytest.ini**
**New-Item -ItemType Directory -Name tests**
**New-Item -ItemType File -Name tests\__init__.py**
**New-Item -ItemType File -Name tests\conftest.py**
**New-Item -ItemType Directory -Name tests\pages**
**New-Item -ItemType File -Name tests\pages\login_page.py**
**New-Item -ItemType File -Name tests\pages\search_page.py**
**New-Item -ItemType File -Name tests\test_basic_selenium.py**
**New-Item -ItemType File -Name tests\test_pom.py**
