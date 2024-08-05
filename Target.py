import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException, TimeoutException


def Target():
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

            # Forget password link
            # driver.find_element(By.XPATH, "//*[@id=\"LoginForm\"]/div[3]/a").click()

        # Enter password and click LoginButton
        driver.find_element(By.ID, "pass").send_keys("Sisa@123456*")
        driver.find_element(By.ID, "LoginButton").click()
        print("Login successful")
        driver.find_element(By.XPATH, "/html/body/div/aside/nav/ul/li[3]/a").click()
        driver.find_element(By.XPATH, "//a[normalize-space()='Agent']").click()
        # driver.find_element(By.XPATH, "/html/body/div[1]/div/section/div/div[1]/div[2]/a[5]").click()
        # driver.find_element(By.XPATH, "//*[@id=\"AgentCreateModal\"]/div/div/form/div/div[2]/div/div/div/button").click()
        print("Agent Running successful")

        driver.find_element(By.XPATH, "/html/body/div/aside/nav/ul/li[2]/a[1]/i").click()

        # Configuration page
        driver.find_element(By.LINK_TEXT, "0000000Agent").click()
        select_pci = True  # Change this to False if you want to select PII data instead

        if select_pci:
            try:
                pci_element = driver.find_element(By.XPATH, "//*[@id=\"headingpcipii\"]/div[2]/div/label")
                pci_element.click()
                print("Selected PCI data successfully")
            except Exception as e:
                print("Error selecting PCI data:", e)
        else:
            try:
                pii_element = driver.find_element(By.XPATH, "//*[@id=\"headingpii\"]/div[2]/div/label")
                pii_element.click()
                print("Selected PII data successfully")
            except Exception as e:
                print("Error selecting PII data:", e)

        #driver.find_element(By.XPATH, "//*[@id=\"headingpcipii\"]/div[2]/div/label").click()
       # print("Selected PCI data successful")
       # driver.find_element(By.XPATH, "//*[@id=\"headingpii\"]/div[2]/div/label").click()
       # print("Selected PII data successful")
        # Indian data selected
        #driver.find_element(By.ID, "pills-ind-tab").click()
       # driver.find_element(By.XPATH, "//div[@id='indtable']/div/label").click()
       # driver.find_element(By.XPATH, "//div[@id='indtable']/div[2]/label").click()
        #driver.find_element(By.XPATH, "//div[@id='indtable']/div[3]/label").click()
       # print("Indian data selected successfully")

        # Target page
        # driver.find_element(By.XPATH, "//*[@id=\"NavTargetsPage\"]").click()
        driver.find_element(By.ID, "NavTargetsPage").click()
        print("Selected Target page successful")
        driver.find_element(By.XPATH, "//*[@id=\"aAddAgent\"]").click()

        print("Selected  Add Agent successful")
        element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//div[@id='TargetAddModel']/div/form/div[3]/button"))
        )

        # Click the element
        element.click()
        # driver.find_element(By.XPATH, "//div[@id='TargetAddModel']/div/form/div[3]/button").click()
        driver.find_element(By.XPATH, "//*[@id=\"aAddAllAgent\"]").click()
        element1 = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//div[@id='TargetAddALLModel']/div/div/div/div[2]/button/span"))
        )

        # Click the element
        element1.click()
        print("Selected  Add all Agents successful")
        driver.find_element(By.ID, "dropdownMenuButton").click()
        driver.find_element(By.XPATH, "//section[@id='Sec']/div/div/div[2]/div/div/a").click()
        print("Updated target  successful")
        # driver.find_element(By.XPATH, "//div[@id='modifyTagsModal']/div/div/div[2]/button").click()
        # Filter
        time.sleep(2)
        driver.find_element(By.XPATH, "//*[@id=\"Sec\"]/div/div[1]/div[2]/a[2]").click()
        driver.find_element(By.ID, "select2-fltrStatus-container").click()
        driver.find_element(By.XPATH, "//div[@id='filterTarget']/div/form/div[3]/button[2]").click()
        driver.find_element(By.XPATH, "//section[@id='Sec']/div/div/div[2]/a[2]").click()
        driver.find_element(By.ID, "select2-fltrStatus-container").click()
        driver.find_element(By.XPATH, "//div[@id='filterTarget']/div/form/div[3]/button[2]").click()
        driver.find_element(By.XPATH, "//section[@id='Sec']/div/div/div[2]/a[2]").click()
        driver.find_element(By.ID, "select2-fltrStatus-container").click()
        driver.find_element(By.XPATH, "//div[@id='filterTarget']/div/form/div[3]/button[2]").click()
        driver.find_element(By.XPATH, "//section[@id='Sec']/div/div/div[2]/a[2]/i").click()
        driver.find_element(By.ID, "select2-fltrStatus-container").click()
        driver.find_element(By.XPATH, "//div[@id='filterTarget']/div/form/div[3]/button[2]").click()
        driver.find_element(By.XPATH, "//section[@id='Sec']/div/div/div[2]/a[2]/i").click()
        driver.find_element(By.ID, "select2-fltrStatus-container").click()
        driver.find_element(By.XPATH, "//div[@id='filterTarget']/div/form/div[3]/button[2]").click()
        driver.find_element(By.XPATH, "//section[@id='Sec']/div/div/div[2]/a[2]").click()
        driver.find_element(By.ID, "select2-fltrStatus-container").click()
        driver.find_element(By.XPATH, "//div[@id='filterTarget']/div/form/div[3]/button[2]").click()
        driver.find_element(By.ID, "target-Refresh").click()
        print("Filtered successful")



    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        driver.quit()


if __name__ == "__main__":
    Target()
