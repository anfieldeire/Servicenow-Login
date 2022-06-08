import pytest
from datetime import date

@pytest.mark.usefixtures("webdriver")
class BaseTest:

    base_url = 'https://url.service-now.com/'
    identifier = "AUTOMATED TESTING"
    module = "INCIDENT"
    action = "CREATE"
    job_name = ""
    today = str(date.today())

    pass
