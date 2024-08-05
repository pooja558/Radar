import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException, TimeoutException
from LoginVars import LoginVar

username = ""
password = ""
tenancy_name = ""


def login_helper(username,password,tenancy_name):
    driver = webdriver.Edge()
    driver.maximize_window()

    try:
        driver.get('https://10.100.13.14/Account/Login')
        driver.implicitly_wait(50)

        # Click the "details" button
        driver.find_element(By.XPATH, "//*[@id=\"details-button\"]").click()

        # Click the "proceed" link
        driver.find_element(By.XPATH, "//*[@id=\"proceed-link\"]").click()
        driver.refresh()
        time.sleep(100)

        # Click the "Change" link
        driver.find_element(By.LINK_TEXT, "Change").click()

        # Enter TenancyName and submit
        driver.find_element(By.ID, "TenancyName").send_keys(tenancy_name)
        driver.find_element(By.XPATH, "//button[@type='submit']").click()


        time.sleep(2)
        driver.find_element(By.XPATH, "//input[@id='usernameOrEmailAddress']").send_keys(username)
        # Enter password and click LoginButton
        driver.find_element(By.ID, "pass").send_keys(password)
        driver.find_element(By.ID, "LoginButton").click()



        print(f"Login successful as {username}")

    except TimeoutException as te:
        print(f"Login failed: {te}")
    except Exception as e:
        print(f"Login failed: {e}")
    finally:
        driver.quit()


def login(username="", password='', tenancy_name=''):
    file_path = 'C:/Users/SISAPoojaB/Desktop/logintestcases.txt'  # Update with the correct file path
    test_cases = read_test_cases(file_path)

    for username, password, tenancy_name in test_cases:
        print(f"Running test case: {username} | {password} | {tenancy_name}")
        LoginVar.username = username
        LoginVar.password = password
        LoginVar.tenancy_name = tenancy_name
        login_helper(LoginVar.username,LoginVar.password,LoginVar.tenancy_name)
    # driver = webdriver.Edge()
    # driver.maximize_window()
    #
    # try:
    #     driver.get('https://192.168.43.110/Account/Login')
    #     driver.implicitly_wait(50)
    #
    #     # Click the "details" button
    #     driver.find_element(By.XPATH, "//*[@id=\"details-button\"]").click()
    #
    #     # Click the "proceed" link
    #     driver.find_element(By.XPATH, "//*[@id=\"proceed-link\"]").click()
    #
    #     # Click the "Change" link
    #     driver.find_element(By.LINK_TEXT, "Change").click()
    #
    #     # Enter TenancyName and submit
    #     driver.find_element(By.ID, "TenancyName").send_keys(tenancy_name)
    #     driver.find_element(By.XPATH, "//button[@type='submit']").click()
    #
    #     # Re-locate the "usernameOrEmailAddress" element
    #     username_input = WebDriverWait(driver, 10).until(
    #         EC.presence_of_element_located((By.ID, "usernameOrEmailAddress"))
    #     )
    #
    #     # Handle StaleElementReferenceException by re-locating the element
    #     try:
    #         username_input.send_keys(username)
    #     except StaleElementReferenceException:
    #         username_input = WebDriverWait(driver, 10).until(
    #             EC.presence_of_element_located((By.ID, "usernameOrEmailAddress"))
    #         )
    #         username_input.send_keys(username)
    #
    #     # Enter password and click LoginButton
    #     driver.find_element(By.ID, "pass").send_keys(password)
    #     driver.find_element(By.ID, "LoginButton").click()
    #
    #
    #
    #     print(f"Login successful as {username}")
    #
    # except TimeoutException as te:
    #     print(f"Login failed: {te}")
    # except Exception as e:
    #     print(f"Login failed: {e}")
    # finally:
    #     driver.quit()

def read_test_cases(file_path):
    test_cases = []

    with open(file_path, 'r') as file:
        lines = file.readlines()

        for line in lines[1:-1]:  # Skip the header line and empty lines
            values = [v.strip() for v in line.split('|') if v.strip()]

            # Check if there are enough values to unpack
            if len(values) == 4:
                username, password, tenancy_name, _ = values
                test_cases.append((username, password, tenancy_name))

    return test_cases

if __name__ == "__main__":
        # login(username, password, tenancy_name)
        login()
        print("Test case executed.\n")
