## Test for the Servicenow App Using Pytest and Selenium
* Test1: Login to the app
* Test2: Create an incident record
* Browser: Firefox
* Python Version Created/Tested in: 3.6
* Use base_test class so that the webdriver is inherited by the other classes
* The script will verify login by finding the header on the right of the home page with the logged in users first and last name.
* Custom logger will log (and append to a file in the same directory)
* Use pip install -r requirements.txt to install the packages from command line to your virtual enviroment
* Run Instructions: Activate the virtual environment, then type pytest from command line to run all tests
