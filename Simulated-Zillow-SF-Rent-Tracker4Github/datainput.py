from selenium import webdriver
from selenium.webdriver.common.by import By
from zillowscraper import ZillowScraper

#Form should include 3 short answer questions for 1. address, 2. monthly price, 3. house listing
GOOGLE_FORM = ("your google forms link")


class DataInput:
    def __init__(self):
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=self.chrome_options)
        self.driver.get(url=GOOGLE_FORM)
        self.z_scrape = ZillowScraper()
        self.address_list = self.z_scrape.get_all_addresses()
        self.price_list = self.z_scrape.get_all_prices()
        self.link_list = self.z_scrape.get_all_links()

    def fill_form(self):
        for (address, price, link) in zip(self.address_list, self.price_list, self.link_list):
            form_inputs = self.driver.find_elements(By.CSS_SELECTOR, 'div div div div div div input')
            submit_button = self.driver.find_element(By.XPATH, '//*[text()="Submit"]')
            form_inputs[0].send_keys(address)
            form_inputs[1].send_keys(price)
            form_inputs[2].send_keys(link)
            submit_button.click()
            submit_another = self.driver.find_element(By.XPATH, '//*[text()="Submit another response"]')
            submit_another.click()
