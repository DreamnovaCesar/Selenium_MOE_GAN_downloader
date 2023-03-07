from selenium import webdriver
from selenium.webdriver.common.by import By

class DropdownModel:
    def __init__(self, driver: webdriver.Chrome, xpath_path: str, xpath_path_list: str):
        self.driver = driver
        self.xpath_path = xpath_path
        self.xpath_path_list = xpath_path_list
    
    def select_option(self, option_picked: str) -> None:

        list_options = []
        
        button = self.driver.find_element(By.XPATH, self.xpath_path)
        button.click()
        
        button_dropdown = self.driver.find_elements(By.XPATH, self.xpath_path_list)
        
        for i, row in enumerate(button_dropdown):
            options = button_dropdown[i].find_elements(By.TAG_NAME, 'span')
        
        for j, option in enumerate(options):
            list_options.append(option.text)
        
        option_index = list_options.index(option_picked)
        
        print('{}'.format(option_picked))

        options[option_index].click()
        list_options = []
        button = self.driver.find_element(By.XPATH, self.xpath_path)
        button.click()
        button_dropdown = self.driver.find_elements(By.XPATH, self.xpath_path_list)
        
        for i, row in enumerate(button_dropdown):
            options = button_dropdown[i].find_elements(By.TAG_NAME, 'span')

        for i, option in enumerate(options):
            list_options.append(option.text)
        
        option_index = list_options.index(option_picked)
        
        print('{}'.format(option_picked))

        options[option_index].click()