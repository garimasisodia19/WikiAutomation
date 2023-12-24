from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class WikipediaAutomation:
    def __init__(self, driver):
        self.driver = driver

    def select_language(self):
        language_button = self.driver.find_element(By.XPATH, '/html/body/div[3]/form/fieldset/div/div[1]/div/select')
        language_button.click()

        # Selecting a specific language (e.g., English)
        language_option = self.driver.find_element(By.XPATH, '/html/body/div[3]/form/fieldset/div/div[1]/div/select/option[24]')
        language_option.click()

    def perform_search(self, query):
        search_box = self.driver.find_element(By.XPATH, '/html/body/div[3]/form/fieldset/div/input')
        search_box.send_keys(query)

        search_button = self.driver.find_element(By.XPATH, '/html/body/div[3]/form/fieldset/button/i')
        search_button.click()

    def navigate_to_page(self):
        hyperlink = self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div[3]/main/div[3]/div[3]/div[1]/p[2]/a[2]')
        hyperlink.click()

# Example usage
try:
    driver = webdriver.Chrome()
    wikipedia_automation = WikipediaAutomation(driver)
    wikipedia_automation.driver.get('https://www.wikipedia.org/')

    # Functionality 1: Language Selection
    wikipedia_automation.select_language()

    # Functionality 2: Searching for a Topic
    wikipedia_automation.perform_search('India')

    # Functionality 3: Clicking on a Hyperlink to Navigate to a New Page
    wikipedia_automation.navigate_to_page()

    # Additional verification or interaction can be added here

except Exception as e:
    print(f"An error occurred: {str(e)}")

finally:
    # Adding a delay before closing the browser for visual verification
    time.sleep(5)
    # Close the browser window
    driver.quit()