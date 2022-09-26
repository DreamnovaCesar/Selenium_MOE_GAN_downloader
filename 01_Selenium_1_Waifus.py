import os
import string
from tkinter import Button
from jmespath import search
from matplotlib.pyplot import text

import requests
from bs4 import BeautifulSoup
import pandas as pd

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import datetime
import numpy as np

import time

import urllib.request

from selenium import webdriver

#URL:str  = "https://dak.gg/valorant/en/profile/DSP%20KimGyuTae-1111"
#URL:str  = r"https://dak.gg/valorant/en/profile/walle-cotta"
#URL:str  = r"https://dak.gg/valorant/en/profile/ilsoto-beth3"
URL:str  = r"https://make.girls.moe/#/"

#Cotta_user_name:str = 'aAa cutefatb0y#fat'

class MakeGirlMOE:

    def __init__(self, **kwargs) -> None:

        # * Instance attributes
        self.URL = kwargs.get('url', None)
        self.Number = kwargs.get('waifus', 50)

        # * Folder attribute (ValueError, TypeError)
        if self.URL == None:
            raise ValueError("Folder does not exist") #! Alert

    def __repr__(self):

        kwargs_info = "{}".format(self.URL)

        return kwargs_info

    def __str__(self):
        pass
    
    def get_images_waifus(self) -> None:
        
        Path_chrome_driver:str = r"C:\Users\Cesar\Dropbox\PC\Desktop\chromedriver.exe"
        
        # *
        XPATH_image = '//*[@id="root"]/div/div/div/div/div[1]/div[2]/div[1]/div/div[1]/div/div/img'
        XPATH_button = '//*[@id="root"]/div/div/div/div/div[1]/div[2]/div[1]/div/button'

        # *
        Time_wait_value:int = 10
        Header_list:list = []

        # * Webdriver chrome activate
        Driver = webdriver.Chrome(Path_chrome_driver)
        Driver.get(self.URL)

        # * Waiting time
        Driver.implicitly_wait(Time_wait_value)
        
        time.sleep(10)
        
        for i in range(self.Number):

            Button_click = Driver.find_element(By.XPATH, XPATH_button)
            Button_click.click()
            # *
            time.sleep(0.2)

            Image = Driver.find_element(By.XPATH, XPATH_image)
            src = Image.get_attribute('src')
            
            Image_name = "Image_{}.png".format(i)
            Image_folder = os.path.join(r"C:\Users\Cesar\Dropbox\PC\Desktop\Waifus", Image_name)

            urllib.request.urlretrieve(src, Image_folder)

            # *
            time.sleep(0.1)

        Driver.close()

    def get_images_waifus_settings(self) -> None:
        
        Path_chrome_driver:str = r"C:\Users\Cesar\Dropbox\PC\Desktop\chromedriver.exe"
        
        # *
        XPATH_image = '//*[@id="root"]/div/div/div/div/div[1]/div[2]/div[1]/div/div[1]/div/div/img'
        XPATH_button = '//*[@id="root"]/div/div/div/div/div[1]/div[2]/div[1]/div/button'

        # *
        Time_wait_value:int = 10
        Header_list:list = []

        # * Webdriver chrome activate
        Driver = webdriver.Chrome(Path_chrome_driver)
        Driver.get(self.URL)

        # * Waiting time
        Driver.implicitly_wait(Time_wait_value)
        
        time.sleep(10)
        
        for i in range(self.Number):

            Button_click = Driver.find_element(By.XPATH, XPATH_button)
            Button_click.click()
            # *
            time.sleep(0.2)

            Image = Driver.find_element(By.XPATH, XPATH_image)
            src = Image.get_attribute('src')
            
            Image_name = "Image_{}.png".format(i)
            Image_folder = os.path.join(r"C:\Users\Cesar\Dropbox\PC\Desktop\Waifus", Image_name)

            urllib.request.urlretrieve(src, Image_folder)

            # *
            time.sleep(0.1)

        Driver.close()

def main():
    
    Waifu = MakeGirlMOE(url = URL, waifus = 1000)

    Waifu.get_images_waifus()

if __name__ == "__main__":
    main()