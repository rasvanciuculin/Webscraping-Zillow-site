import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


Chrome_Driver_Path = "F:/Python/chromedriver.exe"
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
service = Service(Chrome_Driver_Path)

class UpdateForm:
    """ This class fill in the form / save data to google sheet with Selenium. """

    def __init__(self, link):
        self.link = link
        self.driver = webdriver.Chrome(service=service, options=options)

    def update_form(self, link_list, price_list, address_list):
        """ Fill in google form with data parsed from Zillow page """

        driver = self.driver
        for i in range(len(address_list)):
            time.sleep(0.5)
            driver.get(self.link)

            address = driver.find_element(By.XPATH, "//*[@id='mG61Hd']/div[2]/div/div[2]/div[1]/div/div/div[2]/div/"
                                                    "div[1]/div/div[1]/input")
            address.send_keys(address_list[i])

            price = driver.find_element(By.XPATH, "//*[@id='mG61Hd']/div[2]/div/div[2]/div[2]/div/div/div[2]/"
                                                  "div/div[1]/div/div[1]/input")
            price.send_keys(price_list[i])

            link = driver.find_element(By.XPATH,"//*[@id='mG61Hd']/div[2]/div/div[2]/div[3]/div/div/div[2]"
                                                "/div/div[1]/div/div[1]/input")
            link.send_keys(link_list[i])

            submit = driver.find_element(By.XPATH, "//*[@id='mG61Hd']/div[2]/div/div[3]/div[1]/div[1]/div/span/span")
            submit.click()

