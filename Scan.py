import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException, TimeoutException
import python_utils

def Scan():
    driver = webdriver.Edge()
    driver.maximize_window()

    try:
        driver.get('https://10.100.13.14/Account/Login')
        driver.implicitly_wait(50)
        time.sleep(10)
        # Click the "details" button
        driver.find_element(By.XPATH, "//*[@id=\"details-button\"]").click()

        # Click the "proceed" link
        driver.find_element(By.XPATH, "//*[@id=\"proceed-link\"]").click()

        # Click the "Change" link
        driver.find_element(By.LINK_TEXT, "Change").click()

        # Enter TenancyName and submit
        driver.find_element(By.ID, "TenancyName").send_keys("testradar")
        driver.implicitly_wait(5)
        driver.find_element(By.XPATH, "//div[@id='TenantChangeModal']/div/div/form/div[2]/button[2]").click()

        time.sleep(2)
        driver.find_element(By.XPATH, "//input[@id='usernameOrEmailAddress']").send_keys("zakir.rashid@sisainfosec.com")
        driver.find_element(By.ID, "pass").send_keys("Sisa@123456*")
        driver.find_element(By.ID, "LoginButton").click()
        print("Login successful")
        #driver.find_element(By.XPATH, "/html/body/div/aside/nav/ul/li[3]/a").click()
       # driver.find_element(By.XPATH, "//a[normalize-space()='Agent']").click()
       #driver.find_element(By.XPATH, "/html/body/div[1]/div/section/div/div[1]/div[2]/a[5]").click()
       # driver.find_element(By.XPATH, "//*[@id=\"AgentCreateModal\"]/div/div/form/div/div[2]/div/div/div/button").click()
        #print("Agent Running successful")
       # driver.find_element(By.XPATH, "//li[2]/a/i")

        driver.find_element(By.XPATH, "//input[@type='search']").click()
        driver.find_element(By.XPATH, "//input[@type='search']").clear()
        driver.find_element(By.XPATH, "//input[@type='search']").send_keys("Zakir Corp test")
        driver.find_element(By.XPATH, "//button[@type='button']").click()
        time.sleep(20)
        print("searched sucessfully")
        #driver.find_element(By.LINK_TEXT, "Zakir Corp Test").click()
        #driver.find_element(By.XPATH, "//a[contains(text(),'Zakir Corp Test')]").click()
        time.sleep(20)

        print ("Entered config ")
        # Scan page
        driver.find_element(By.ID, "NavScanPage").click()

        print("Scan page entered successful")
        driver.find_element(By.ID, "4638").click()
        print("Target selected to scan")
        driver.find_element(By.ID, "Scan-Start").click()
        print("click  to scan")
        driver.find_element(By.ID, "continueScan").click()
        print("click on Continue scan")
        # Wait for the button to be clickable
        element1 = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@class='swal-button swal-button--confirm']"))
        )
        # Click the button
        element1.click()

        print("click on yes to scan")
        driver.refresh()
        time.sleep(100)
        element2 = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//*[@id=\"Scan-Refresh\"]"))
        )
        # Click the button
        element2.click()
        print("click on Refresh ")
        # Filter
        #driver.find_element(By.XPATH, "//section[@id='Sec']/div/div/div[2]/a[5]").click()
        #driver.find_element(By.ID, "select2-fltbystatus-container").click()
        #driver.find_element(By.XPATH, "//div[@id='filterScan']/div/form/div[3]/button[2]").click()
        #driver.find_element(By.XPATH, "//*[@id=\"filterScan\"]/div/form/div[1]/button").click()
        #print("Filtered sucessfully")
        # Export excel
        element3 = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "exportExcel"))
        )

        # Once the element is found, interact with it
        element3.click()
        #driver.find_element(By.XPATH, "//*[@id=\"exportExcel\"]").click()
        print("Export excel sucessfully")
        driver.refresh()
        # Configuration
        element4 = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.LINK_TEXT, "Configuration"))
        )

        # Once the element is found, interact with it
        element4.click()
        #driver.find_element(By.LINK_TEXT, "Configuration").click()
        driver.find_element(By.XPATH, "//div[@id='ConfigScan']/div/form/div[3]/button").click()
        print("Configuration/exclude/accuray ")
        # Report page
        #driver.find_element(By.ID, "NavReportPage").click()
        element5 = driver.find_element(By.ID, "NavReportPage")
        driver.execute_script("arguments[0].click();", element5)
        print("Entered report page")
        #driver.get("https://10.100.13.9/Report")
        driver.refresh()
        driver.find_element(By.ID, "dropdownMenuButton").click()
        driver.find_element(By.ID, "aCurrentReport").click()
        print("selected current report")
        driver.find_element(By.ID, "4626").click()
        driver.find_element(By.ID, "btnRunReport").click()
        print("Report generated sucessfully")
        driver.refresh()
        # Schedule page
        driver.find_element(By.ID, "NavSchedulePage").click()
        print("Schedule page entered sucessfully")
        #driver.get("https://10.100.13.9/Scheduling")
        driver.refresh()
        driver.find_element(By.LINK_TEXT, "Create").click()
        driver.find_element(By.ID, "Title").click()
        driver.find_element(By.ID, "Title").clear()
        driver.find_element(By.ID, "Title").send_keys("automation")
        driver.find_element(By.ID, "date").click()
        driver.find_element(By.ID, "date").clear()
        driver.find_element(By.ID, "date").send_keys("2024-02-21T16:14")
        driver.find_element(By.XPATH, "//button[@type='submit']").click()
        driver.find_element(By.XPATH, "//button[@type='button']").click()
        print("Schedule sucessfully")
        #Logout
        driver.find_element(By.XPATH,
            "(.//*[normalize-space(text()) and normalize-space(.)='Cancel'])[2]/following::button[1]").click()
        driver.find_element(By.XPATH,
            "(.//*[normalize-space(text()) and normalize-space(.)='pooja m'])[1]/following::span[1]").click()
        driver.find_element(By.XPATH,
            "(.//*[normalize-space(text()) and normalize-space(.)='Sensitive Data Overview'])[1]/preceding::span[1]").click()
        print("Logout sucessfully")

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        driver.quit()

if __name__ == "__main__":
    Scan()
