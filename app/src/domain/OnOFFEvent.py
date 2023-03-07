from selenium import webdriver
from selenium.webdriver.common.by import By

class OnOffEvent:
    def __init__(self, 
                 driver: webdriver.Chrome, 
                 xpath_path_on: str, xpath_path_random: str, 
                 xpath_path_off: str):
        
        self.driver = driver
        self.xpath_path_on = xpath_path_on
        self.xpath_path_random = xpath_path_random
        self.xpath_path_off = xpath_path_off
    
    def select_option(self, option_picked: str) -> None:
        
        if option_picked == 'ON':
            button = self.driver.find_element(By.XPATH, self.xpath_path_on)
            button.click()

        elif option_picked == 'Random':
            button = self.driver.find_element(By.XPATH, self.xpath_path_random)
            button.click()

        elif option_picked == 'OFF':
            button = self.driver.find_element(By.XPATH, self.xpath_path_off)
            button.click()

        else:   
            pass