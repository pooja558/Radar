import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException, TimeoutException


def config():
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


        # Configuration page
        WebDriverWait(driver, 10).until(
            EC.invisibility_of_element_located((By.ID, "ScanCreateModal"))
        )

        # Now, attempt to click the link
        driver.find_element(By.CLASS_NAME, "view-scan").click()
        # Assuming you have initialized your WebDriver instance as 'driver'

        # Add your logic here to determine which data to select
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

        # Function to select Indian data
        def select_indian_data():
            driver.find_element(By.ID, "pills-ind-tab").click()
            driver.find_element(By.XPATH, "//div[@id='indtable']/div/label").click()
            driver.find_element(By.XPATH, "//div[@id='indtable']/div[2]/label").click()
            driver.find_element(By.XPATH, "//div[@id='indtable']/div[3]/label").click()
            print("Indian data selected successfully")

        # Function to select GDPR data
        def select_gdpr_data():
            driver.find_element(By.ID, "pills-gdpr-tab").click()
            driver.find_element(By.XPATH, "//div[@id='gdprtable']/div/label").click()
            driver.find_element(By.XPATH, "//div[@id='gdprtable']/div[2]/label").click()
            driver.find_element(By.XPATH, "//div[@id='pills-gdpr']/div/div/label").click()
            print("GDPR data selected successfully")

        # Function to select Apra data
        def select_apra_data():
            driver.find_element(By.ID, "pills-apra-tab").click()
            driver.find_element(By.XPATH, "//div[@id='apratable']/div/label").click()
            driver.find_element(By.XPATH, "//div[@id='apratable']/div[2]/label").click()
            driver.find_element(By.XPATH, "//div[@id='apratable']/div[3]/label").click()
            driver.find_element(By.XPATH, "//div[@id='apratable']/div[4]/label").click()
            print("APRA data selected successfully")

        # Function to select CCPA data
        def select_ccpa_data():
            driver.find_element(By.ID, "pills-ccpa-tab").click()
            driver.find_element(By.XPATH, "//div[@id='ccpatable']/div/label").click()
            print("CCPA data selected successfully")

        # Function to select Lgpd data
        def select_lgpd_data():
            driver.find_element(By.ID, "pills-lgpd-tab").click()
            driver.find_element(By.XPATH, "//div[@id='lgpdtable']/div/label").click()
            driver.find_element(By.XPATH, "//div[@id='lgpdtable']/div[2]/label").click()
            print("LGPD data selected successfully")

        # Function to select Hipaa data
        def select_hipaa_data():
            driver.find_element(By.ID, "pills-hipaa-tab").click()
            driver.find_element(By.XPATH, "//div[@id='hipaatable']/div/label").click()
            driver.find_element(By.XPATH, "//div[@id='hipaatable']/div[2]/label").click()
            driver.find_element(By.XPATH, "//div[@id='hipaatable']/div[3]/label").click()
            driver.find_element(By.XPATH, "//div[@id='hipaatable']/div[4]").click()
            driver.find_element(By.XPATH, "//div[@id='hipaatable']/div[4]/label").click()
            print("HIPAA data selected successfully")

        # Function to select Gcc data
        def select_gcc_data():
            driver.find_element(By.ID, "pills-gcc-tab").click()
            driver.find_element(By.XPATH, "//div[@id='gcctable']/div/label").click()
            driver.find_element(By.XPATH, "//div[@id='gcctable']/div[2]/label").click()
            driver.find_element(By.XPATH, "//div[@id='gcctable']/div[3]/label").click()
            print("GCC data selected successfully")

        # Function to select Other data
        def select_other_data():
            driver.find_element(By.ID, "pills-other-tab").click()
            driver.find_element(By.XPATH, "//div[@id='otherpiitable']/div/div/div/label").click()
            driver.find_element(By.XPATH, "//div[@id='otherpiitable']/div/div/div[2]/label").click()
            print("Other data selected successfully")

        # Select the data based on user's choice
        choice = input("Enter your choice (Indian/GDPR/APRA/CCPA/LGPD/HIPAA/GCC/Other): ").lower()

        if choice == "indian":
            select_indian_data()
        elif choice == "gdpr":
            select_gdpr_data()
        elif choice == "apra":
            select_apra_data()
        elif choice == "ccpa":
            select_ccpa_data()
        elif choice == "lgpd":
            select_lgpd_data()
        elif choice == "hipaa":
            select_hipaa_data()
        elif choice == "gcc":
            select_gcc_data()
        elif choice == "other":
            select_other_data()
        else:
            print("Invalid choice! Please select from the given options.")

        # Indian data selected
        driver.find_element(By.ID, "pills-ind-tab").click()
        driver.find_element(By.XPATH, "//div[@id='indtable']/div/label").click()
        driver.find_element(By.XPATH, "//div[@id='indtable']/div[2]/label").click()
        driver.find_element(By.XPATH, "//div[@id='indtable']/div[3]/label").click()
        print("Indian data selected successfully")
        # GDPR data
        driver.find_element(By.ID, "pills-gdpr-tab").click()
        driver.find_element(By.XPATH, "//div[@id='gdprtable']/div/label").click()
        driver.find_element(By.XPATH, "//div[@id='gdprtable']/div[2]/label").click()
        driver.find_element(By.XPATH, "//div[@id='pills-gdpr']/div/div/label").click()
        print("Gdpr selected successfully")
        #Apra
        driver.find_element(By.ID, "pills-apra-tab").click()
        driver.find_element(By.XPATH, "//div[@id='apratable']/div/label").click()
        driver.find_element(By.XPATH, "//div[@id='apratable']/div[2]/label").click()
        driver.find_element(By.XPATH, "//div[@id='apratable']/div[3]/label").click()
        driver.find_element(By.XPATH, "//div[@id='apratable']/div[4]/label").click()
        print("Apra selected successfully")
        #Ccpa
        driver.find_element(By.ID, "pills-ccpa-tab").click()
        driver.find_element(By.XPATH, "//div[@id='ccpatable']/div/label").click()
        print("Ccpa selected successfully")
        # Lgpd
        driver.find_element(By.ID, "pills-lgpd-tab").click()
        driver.find_element(By.XPATH, "//div[@id='lgpdtable']/div/label").click()
        driver.find_element(By.XPATH, "//div[@id='lgpdtable']/div[2]/label").click()
        print("Lgpd selected successfully")
         # Hipaa
        driver.find_element(By.ID, "pills-hipaa-tab").click()
        driver.find_element(By.XPATH, "//div[@id='hipaatable']/div/label").click()
        driver.find_element(By.XPATH, "//div[@id='hipaatable']/div[2]/label").click()
        driver.find_element(By.XPATH, "//div[@id='hipaatable']/div[3]/label").click()
        driver.find_element(By.XPATH, "//div[@id='hipaatable']/div[4]").click()
        driver.find_element(By.XPATH, "//div[@id='hipaatable']/div[4]/label").click()
        print("Hipaa selected successfully")
        # Gcc
        driver.find_element(By.ID, "pills-gcc-tab").click()
        driver.find_element(By.XPATH, "//div[@id='gcctable']/div/label").click()
        driver.find_element(By.XPATH, "//div[@id='gcctable']/div[2]/label").click()
        driver.find_element(By.XPATH, "//div[@id='gcctable']/div[3]/label").click()
        print("Gcc selected successfully")
        # Others
        driver.find_element(By.ID, "pills-other-tab").click()
        driver.find_element(By.XPATH, "//div[@id='otherpiitable']/div/div/div/label").click()
        driver.find_element(By.XPATH, "//div[@id='otherpiitable']/div/div/div[2]/label").click()
        print("Others selected successfully")
        # Filetypes
        driver.find_element(By.ID, "pills-profile-tab").click()
        driver.find_element(By.XPATH, "//div[@id='filesTable']/div[2]/div[2]/div/div/label").click()
        driver.find_element(By.XPATH, "//div[@id='filesTable']/div[2]/div[2]/div/div[2]/label").click()
        driver.find_element(By.XPATH, "//div[@id='filesTable']/div[2]/div[2]/div/div[3]/label").click()
        driver.find_element(By.XPATH, "//div[@id='filesTable']/div[2]/div[2]/div/div[4]/label").click()
        driver.find_element(By.XPATH, "//div[@id='filesTable']/div[2]/div[2]/div/div[5]/label").click()
        driver.find_element(By.XPATH, "//div[@id='filesTable']/div[2]/div[2]/div/div[6]/label").click()
        driver.find_element(By.XPATH, "//div[@id='filesTable']/div[2]/div[2]/div/div[7]/label").click()
        driver.find_element(By.XPATH, "//div[@id='filesTable']/div[2]/div[2]/div/div[8]/label").click()
        driver.find_element(By.ID, "pills-contact-tab").click()
        #driver.find_element(By.LINK_TEXT, "Create").click()
        #driver.find_element(By.XPATH, "//*[@id=\"createregex\"]/div/form/div[1]/button/span").click()
        print("Selected  Regular expression successful")
        driver.find_element(By.ID, "pills-advance-tab").click()
        print("Selected  setting successful")
        print("Configuration settings selected")

        # Logout
        driver.find_element(By.XPATH, "/html/body/div[1]/header/nav/ul/li[2]").click()
        driver.find_element(By.XPATH, "/html/body/div[1]/header/nav/ul/li[2]/div/div[3]/a").click()
        print("Logout successful")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        driver.quit()

if __name__ == "__main__":
    config()