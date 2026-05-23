import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 🛠 Update this to your actual local project path
BASE = "file:///Users/Bin_2/Desktop/Apoorva/e-learning/"

@pytest.mark.usefixtures("driver")
class TestAuth:

    def wait_for(self, driver, locator, timeout=20):
        """Reusable explicit wait with extended timeout (default: 20s)."""
        return WebDriverWait(driver, timeout).until(EC.presence_of_element_located(locator))

    def wait_for_alert(self, driver, timeout=20):
        """Wait for an alert to appear."""
        return WebDriverWait(driver, timeout).until(EC.alert_is_present())

    def test_signup_and_login(self, driver):
        """✅ Test full signup + login flow"""
        # --- SIGNUP ---
        driver.get(BASE + "signup.html")

        # Wait for form
        self.wait_for(driver, (By.ID, "signupForm"))

        # Fill out the form
        driver.find_element(By.ID, "studentName").send_keys("Test User")
        driver.find_element(By.ID, "studentId").send_keys("T123")
        driver.find_element(By.ID, "studentEmail").send_keys("test@example.com")
        driver.find_element(By.ID, "studentGender").send_keys("Other")
        driver.find_element(By.ID, "studentAge").send_keys("25")
        driver.find_element(By.ID, "signupUsername").send_keys("testuser")
        driver.find_element(By.ID, "signupPassword").send_keys("Passw0rd!")

        # Submit form
        driver.find_element(By.CSS_SELECTOR, "#signupForm button[type='submit']").click()

        # Handle alert (if any)
        try:
            alert = self.wait_for_alert(driver)
            alert.accept()
        except:
            pass  # no alert, continue

        # Wait until redirected to index.html
        WebDriverWait(driver, 20).until(EC.url_contains("index.html"))

        # --- LOGIN ---
        driver.get(BASE + "index.html")

        self.wait_for(driver, (By.ID, "loginForm"))
        driver.find_element(By.ID, "loginUsername").send_keys("testuser")
        driver.find_element(By.ID, "loginPassword").send_keys("Passw0rd!")
        driver.find_element(By.CSS_SELECTOR, "#loginForm button[type='submit']").click()

        # Handle any alert or redirect
        try:
            alert = self.wait_for_alert(driver)
            alert.accept()
        except:
            pass

        # Wait until redirected to home.html
        WebDriverWait(driver, 20).until(EC.url_contains("home.html"))

        # Verify welcome message contains the name
        el = self.wait_for(driver, (By.ID, "welcomeUser"))
        assert "Test User" in el.text, "Welcome message should include username."

    def test_invalid_login_shows_error(self, driver):
        """❌ Test invalid login triggers alert."""
        driver.get(BASE + "index.html")

        self.wait_for(driver, (By.ID, "loginForm"))

        # Enter wrong credentials
        driver.find_element(By.ID, "loginUsername").send_keys("wrong")
        driver.find_element(By.ID, "loginPassword").send_keys("wrong")
        driver.find_element(By.CSS_SELECTOR, "#loginForm button[type='submit']").click()

        # Wait for and verify alert
        alert = self.wait_for_alert(driver)
        assert "Invalid" in alert.text, "Expected invalid credentials alert."
        alert.accept()
