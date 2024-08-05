import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException, TimeoutException

def Admin():
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
        driver.find_element(By.XPATH, "/html/body/div/aside/nav/ul/li[4]/a/i").click()
        driver.find_element(By.XPATH, "/html/body/div[1]/aside/nav/ul/li[4]/div/ul/li[1]/a[1]").click()
        # click on users
        driver.find_element(By.XPATH, "/html/body/div/aside/nav/ul/li[4]/a/i").click()
        driver.find_element(By.XPATH, "/html/body/div/aside/nav/ul/li[4]/div/ul/li[6]/a[2]").click()
        driver.find_element(By.XPATH, "//a[@class='btn btn-sm btn-primary']").click()
        driver.find_element(By.XPATH, "//*[@id=\"username\"]").send_keys("Automation")
        driver.find_element(By.XPATH, "//*[@id=\"UserCreateModal\"]/div/form/div[2]/div[2]/input").send_keys("pooja")
        driver.find_element(By.XPATH, "//*[@id=\"useremail\"]").send_keys("pooja.ptttp@gmail.com")
        driver.find_element(By.XPATH, "//*[@id=\"UserCreateModal\"]/div/form/div[2]/div[4]/div[1]/label").click()
        driver.find_element(By.XPATH, "//*[@id=\"UserCreateModal\"]/div/form/div[3]/button[2]").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "/html/body/div[3]/div/div[3]/div/button").click()
        driver.find_element(By.XPATH, "//*[@id=\"UserCreateModal\"]/div/form/div[1]/button/span").click()
        print("user created successful")
        # Roles
        driver.find_element(By.XPATH, "/html/body/div/aside/nav/ul/li[4]/a/i").click()
        driver.find_element(By.XPATH, "/html/body/div/aside/nav/ul/li[4]/div/ul/li[4]/a[2]").click()
        driver.find_element(By.XPATH, "//a[@class='btn btn-sm btn-primary']").click()
        driver.find_element(By.XPATH, "//*[@id=\"rolename\"]").send_keys("pooja")
        driver.find_element(By.XPATH, "//*[@id=\"displayname\"]").send_keys("Testing")
        driver.find_element(By.XPATH, "//*[@id=\"RoleCreateModal\"]/div/form/div[3]/button[2]").click()
        driver.find_element(By.XPATH, "/html/body/div[3]/div/div[3]/div/button").click()
        driver.find_element(By.XPATH, "//*[@id=\"RoleCreateModal\"]/div/form/div[1]/button").click()
        print("Roles successful")
        # logout
        driver.find_element(By.XPATH, "/html/body/div/aside/nav/ul/li[4]/div/ul/li[6]/a[2]")
        driver.find_element(By.XPATH, "/html/body/div/header/nav/ul/li[2]/a/span[2]/span[2]").click()
        driver.find_element(By.XPATH, "/html/body/div/header/nav/ul/li[2]/div/div[3]/a").click()
        print("Logout successful")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        driver.quit()

if __name__ == "__main__":
    Admin()