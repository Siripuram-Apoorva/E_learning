import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions

@pytest.fixture(params=["chrome", "firefox", "edge"])
def driver(request):
    """Fixture to initialize the browser driver for Chrome, Firefox, and Edge."""
    browser = request.param

    if browser == "chrome":
        options = ChromeOptions()
        options.add_argument("--start-maximized")
        driver = webdriver.Chrome(service=ChromeService(), options=options)

    elif browser == "firefox":
        options = FirefoxOptions()
        driver = webdriver.Firefox(service=FirefoxService(), options=options)
        driver.maximize_window()

    elif browser == "edge":
        options = EdgeOptions()
        driver = webdriver.Edge(service=EdgeService(), options=options)
        driver.maximize_window()

    yield driver
    driver.quit()
