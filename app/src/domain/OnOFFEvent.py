from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class OnOffEvent(object):
    def __init__(self, 
                 Driver: webdriver.Chrome, 
                 XPATH_ON: str, 
                 XPATH_Random: str, 
                 XPATH_OFF: str):
        
        self.Driver = Driver
        self.XPATH_ON = XPATH_ON
        self.XPATH_Random = XPATH_Random
        self.XPATH_OFF = XPATH_OFF

    def select_option(self, Option_picked: str) -> None:
        
        print(Option_picked)

        if Option_picked == 'ON':
            button = WebDriverWait(self.Driver, 0.2).until(
                EC.presence_of_element_located((By.XPATH, self.XPATH_ON)))
            
            button = self.Driver.find_element(By.XPATH, self.XPATH_ON)
            button.click()
            print('ON clicked {}'.format(self.XPATH_ON))

        elif Option_picked == 'Random':
            button = WebDriverWait(self.Driver, 0.2).until(
                EC.presence_of_element_located((By.XPATH, self.XPATH_Random)))
            
            button = self.Driver.find_element(By.XPATH, self.XPATH_Random)
            button.click()
            print('Random clicked {}'.format(self.XPATH_Random))

        elif Option_picked == 'OFF':
            button = WebDriverWait(self.Driver, 0.2).until(
                EC.presence_of_element_located((By.XPATH, self.XPATH_OFF)))
            
            button = self.Driver.find_element(By.XPATH, self.XPATH_OFF)
            button.click()
            print('OFF clicked {}'.format(self.XPATH_OFF))

        else:   
            pass