import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException, TimeoutException

def Dashboard():
    driver = webdriver.Edge()
    driver.maximize_window()

    try:
        driver.get('https://10.100.13.14/Account/Login')
        driver.implicitly_wait(50)

        # Click the "details" button
        driver.find_element(By.XPATH, "//*[@id=\"details-button\"]").click()

        # Click the "proceed" link
        driver.find_element(By.XPATH, "//*[@id=\"proceed-link\"]").click()

        # Click the "Change" link
        driver.find_element(By.LINK_TEXT, "Change").click()

        # Enter TenancyName and submit
        driver.find_element(By.ID, "TenancyName").send_keys("testradar")
        driver.find_element(By.XPATH, "//button[@type='submit']").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "//input[@id='usernameOrEmailAddress']").send_keys("zakir.rashid@sisainfosec.com")

        # Enter password and click LoginButton
        driver.find_element(By.ID, "pass").send_keys("Sisa@123456*")
        driver.find_element(By.ID, "LoginButton").click()
        print("Login successful")
        driver.find_element(By.XPATH, "//li/a/i").click()
        driver.find_element(By.LINK_TEXT, "Sensitive Data Overview").click()
        driver.refresh()
        driver.find_element(By.XPATH, "//li/a/i").click()
        driver.find_element(By.LINK_TEXT, "Scan Dashboard").click()
        driver.refresh()
        driver.find_element(By.XPATH, "//li/a/i").click()
        driver.find_element(By.LINK_TEXT, "Scan Analytics").click()
        driver.refresh()

        driver.find_element(By.ID, "ExportExcel").click()
        driver.refresh()
        driver.find_element(By.XPATH, "//section[@id='scanAnaDiv']/div/div/div[2]/button").click()
        driver.find_element(By.XPATH, "//form[@id='formFilter']/div[2]/div[2]/div[2]/select").click()
        driver.find_element(By.XPATH, "//form[@id='formFilter']/div/div[2]/button/span").click()

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        driver.quit()

if __name__ == "__main__":
    Dashboard()
