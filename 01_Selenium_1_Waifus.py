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

#URL = r"https://make.girls.moe/#/"
#Cotta_user_name = 'aAa cutefatb0y#fat'

class MakeGirlMOE:

    def __init__(self, **kwargs) -> None:
        
        # * Instance attributes
        self.CSV = kwargs.get('csv', None)

        # * Folder attribute (ValueError, TypeError)
        if self.CSV == None:
            raise ValueError("Folder does not exist") #! Alert
            
        with open(self.CSV) as CSV:
        
            Data = pd.read_csv(CSV)

            self.Model = Data['Model'].tolist()
            self.Hair_color = Data['Hair color'].tolist()
            self.Hair_style = Data['Hair style'].tolist()
            self.Eye_color = Data['Eye color'].tolist()
            self.Dark_sin = Data['Dark sin'].tolist()
            self.Blush = Data['Blush'].tolist()
            self.Smile = Data['Smile'].tolist()
            self.Open_mouth = Data['Open mouth'].tolist()
            self.Hat = Data['Hat'].tolist()
            self.Ribbon = Data['Ribbon'].tolist()
            self.Glasses = Data['Glasses'].tolist()
            self.Folder = Data['Folder'].tolist()
            self.URL = Data['URL'].tolist()
            self.Epochs = Data['Epochs'].tolist()

            #self.Number = kwargs.get('waifus', 50)
            self.Time_interval = 0.05
            self.Initial = 5

    def __repr__(self):

        kwargs_info = "{}".format(self.CSV)

        return kwargs_info

    def __str__(self):
        pass
    
    # * CSV attribute
    @property
    def CSV_property(self):
        return self.CSV

    @CSV_property.setter
    def CSV_property(self, New_value):
        if not isinstance(New_value, str):
            raise TypeError("CSV must be a string") #! Alert
        self.CSV = New_value
    
    @CSV_property.deleter
    def Folder_property(self):
        print("Deleting CSV...")
        del self.CSV

    @staticmethod
    def model_dropdown(Driver, XPATH_path: string, XPATH_path_list: string, Option_picked: string) -> None:
        
        # *
        List_options = []

        # *
        Button = Driver.find_element(By.XPATH, XPATH_path)
        Button.click()

        # *
        Button_dropdown = Driver.find_elements(By.XPATH, XPATH_path_list)
        
        # *
        for i, Row in enumerate(Button_dropdown):

            Options = Button_dropdown[i].find_elements(By.TAG_NAME, 'span')

        for i, Option in enumerate(Options):

            List_options.append(Option.text)

        # *
        #print(List_options)

        print(List_options)

        Option_index = List_options.index(Option_picked)
        
        print('{}'.format(Option_picked))

        Options[Option_index].click()
    
    @staticmethod
    def model_on_off(Driver, XPATH_path_on: string, XPATH_path_random: string, XPATH_path_off: string, Option_picked: string) -> None:
        
        # *
        List_options = []

        # *
        if(Option_picked == 'ON'):
            Button = Driver.find_element(By.XPATH, XPATH_path_on)
            Button.click()

        elif(Option_picked == 'Random'):
            Button = Driver.find_element(By.XPATH, XPATH_path_random)
            Button.click()

        elif(Option_picked == 'OFF'):
            Button = Driver.find_element(By.XPATH, XPATH_path_off)
            Button.click()

        else:   
            pass

    def get_images_waifus(self) -> None:
        
        Path_chrome_driver:str = r"C:\Users\Cesar\Dropbox\PC\Desktop\chromedriver.exe"
        
        # *
        XPATH_image = '//*[@id="root"]/div/div/div/div/div[1]/div[2]/div[1]/div/div[1]/div/div/img'
        XPATH_button = '//*[@id="root"]/div/div/div/div/div[1]/div[2]/div[1]/div/button'

        # *
        Header_list = []

        # * Webdriver chrome activate
        Driver = webdriver.Chrome(Path_chrome_driver)
        Driver.get(self.URL)

        # * Waiting time
        Driver.implicitly_wait(self.Initial)
        
        time.sleep(self.Initial)
        
        for i in range(self.Number):

            Button_click = Driver.find_element(By.XPATH, XPATH_button)
            Button_click.click()
            # *
            time.sleep(self.Time_interval)

            Image = Driver.find_element(By.XPATH, XPATH_image)
            src = Image.get_attribute('src')
            
            Image_name = "Image_{}.png".format(i)
            Image_folder = os.path.join(r"C:\Users\Cesar\Dropbox\PC\Desktop\Waifus", Image_name)

            urllib.request.urlretrieve(src, Image_folder)

            # *
            time.sleep(self.Time_interval)

        Driver.close()
        
    def get_images_waifus_settings(self) -> None:
        
        Path_chrome_driver:str = r"C:\Users\Cesar\Dropbox\PC\Desktop\chromedriver.exe"
        
        # *
        XPATH_model_button = '//*[@id="root"]/div/div/div/div/div[1]/div[2]/div[2]/div/div[2]/div/div/button'
        XPATH_model_open = '//*[@id="root"]/div/div/div/div/div[1]/div[2]/div[2]/div/div[2]/div/div/ul'

        # *
        XPATH_hair_color_button = '//*[@id="root"]/div/div/div/div/div[1]/div[2]/div[2]/div/div[3]/div[1]/div/button'
        XPATH_hair_color_open = '//*[@id="root"]/div/div/div/div/div[1]/div[2]/div[2]/div/div[3]/div[1]/div/ul'

        XPATH_hair_style_button = '//*[@id="root"]/div/div/div/div/div[1]/div[2]/div[2]/div/div[3]/div[2]/div/button'
        XPATH_hair_style_open = '//*[@id="root"]/div/div/div/div/div[1]/div[2]/div[2]/div/div[3]/div[2]/div/ul'

        XPATH_Eye_color_button = '//*[@id="root"]/div/div/div/div/div[1]/div[2]/div[2]/div/div[3]/div[3]/div/button'
        XPATH_Eye_color_open = '//*[@id="root"]/div/div/div/div/div[1]/div[2]/div[2]/div/div[3]/div[3]/div/ul'

        # *
        XPATH_dark_skin_off_button = '//*[@id="root"]/div/div/div/div/div[1]/div[2]/div[2]/div/div[3]/div[4]/div/button[1]'
        XPATH_dark_skin_random_button = '//*[@id="root"]/div/div/div/div/div[1]/div[2]/div[2]/div/div[3]/div[4]/div/button[2]'
        XPATH_dark_skin_on_button = '//*[@id="root"]/div/div/div/div/div[1]/div[2]/div[2]/div/div[3]/div[4]/div/button[3]'

        XPATH_blush_off_button = '//*[@id="root"]/div/div/div/div/div[1]/div[2]/div[2]/div/div[3]/div[5]/div/button[1]'
        XPATH_blush_random_button = '//*[@id="root"]/div/div/div/div/div[1]/div[2]/div[2]/div/div[3]/div[5]/div/button[2]'
        XPATH_blush_on_button = '//*[@id="root"]/div/div/div/div/div[1]/div[2]/div[2]/div/div[3]/div[5]/div/button[3]'

        XPATH_smile_off_button = '//*[@id="root"]/div/div/div/div/div[1]/div[2]/div[2]/div/div[3]/div[6]/div/button[1]'
        XPATH_smile_random_button = '//*[@id="root"]/div/div/div/div/div[1]/div[2]/div[2]/div/div[3]/div[6]/div/button[2]'
        XPATH_smile_on_button = '//*[@id="root"]/div/div/div/div/div[1]/div[2]/div[2]/div/div[3]/div[6]/div/button[3]'

        XPATH_open_mouth_off_button = '//*[@id="root"]/div/div/div/div/div[1]/div[2]/div[2]/div/div[3]/div[7]/div/button[1]'
        XPATH_open_mouth_random_button = '//*[@id="root"]/div/div/div/div/div[1]/div[2]/div[2]/div/div[3]/div[7]/div/button[2]'
        XPATH_open_mouth_on_button = '//*[@id="root"]/div/div/div/div/div[1]/div[2]/div[2]/div/div[3]/div[7]/div/button[3]'

        XPATH_hat_off_button = '//*[@id="root"]/div/div/div/div/div[1]/div[2]/div[2]/div/div[3]/div[8]/div/button[1]'
        XPATH_hat_random_button = '//*[@id="root"]/div/div/div/div/div[1]/div[2]/div[2]/div/div[3]/div[8]/div/button[2]'
        XPATH_hat_on_button = '//*[@id="root"]/div/div/div/div/div[1]/div[2]/div[2]/div/div[3]/div[8]/div/button[3]'

        XPATH_ribbon_off_button = '//*[@id="root"]/div/div/div/div/div[1]/div[2]/div[2]/div/div[3]/div[9]/div/button[1]'
        XPATH_ribbon_random_button = '//*[@id="root"]/div/div/div/div/div[1]/div[2]/div[2]/div/div[3]/div[9]/div/button[2]'
        XPATH_ribbon_on_button = '//*[@id="root"]/div/div/div/div/div[1]/div[2]/div[2]/div/div[3]/div[9]/div/button[3]'

        XPATH_glasses_off_button = '//*[@id="root"]/div/div/div/div/div[1]/div[2]/div[2]/div/div[3]/div[10]/div/button[1]'
        XPATH_glasses_random_button = '//*[@id="root"]/div/div/div/div/div[1]/div[2]/div[2]/div/div[3]/div[10]/div/button[2]'
        XPATH_glasses_on_button = '//*[@id="root"]/div/div/div/div/div[1]/div[2]/div[2]/div/div[3]/div[10]/div/button[3]'

        XPATH_image = '//*[@id="root"]/div/div/div/div/div[1]/div[2]/div[1]/div/div[1]/div/div/img'
        XPATH_image_button = '//*[@id="root"]/div/div/div/div/div[1]/div[2]/div[1]/div/button'

        # *
        for k in range(len(self.Model)):
            
            # * Webdriver chrome activate
            Driver = webdriver.Chrome(Path_chrome_driver)
            Driver.get(self.URL[k])

            # * Waiting time
            Driver.implicitly_wait(self.Initial)

            # *
            self.model_dropdown(Driver, XPATH_model_button, XPATH_model_open, self.Model[k])
            self.model_dropdown(Driver, XPATH_hair_color_button, XPATH_hair_color_open, self.Hair_color[k])
            self.model_dropdown(Driver, XPATH_hair_style_button, XPATH_hair_style_open, self.Hair_style[k])
            self.model_dropdown(Driver, XPATH_Eye_color_button, XPATH_Eye_color_open, self.Eye_color[k])

            # *
            self.model_on_off(Driver, XPATH_dark_skin_off_button, XPATH_dark_skin_random_button, XPATH_dark_skin_on_button, self.Dark_sin[k])
            self.model_on_off(Driver, XPATH_blush_off_button, XPATH_blush_random_button, XPATH_blush_on_button,  self.Blush[k])
            self.model_on_off(Driver, XPATH_smile_off_button, XPATH_smile_random_button, XPATH_smile_on_button, self.Smile[k])
            self.model_on_off(Driver, XPATH_open_mouth_off_button, XPATH_open_mouth_random_button, XPATH_open_mouth_on_button, self.Open_mouth[k])
            self.model_on_off(Driver, XPATH_hat_off_button, XPATH_hat_random_button, XPATH_hat_on_button, self.Hat[k])
            self.model_on_off(Driver, XPATH_ribbon_off_button, XPATH_ribbon_random_button, XPATH_ribbon_on_button, self.Ribbon[k])
            self.model_on_off(Driver, XPATH_glasses_off_button, XPATH_glasses_random_button, XPATH_glasses_on_button, self.Glasses[k])

            time.sleep(self.Initial)

            for i in range(self.Epochs[k]):

                Button_click = Driver.find_element(By.XPATH, XPATH_image_button)
                Button_click.click()

                # *
                time.sleep(self.Time_interval)

                Image = Driver.find_element(By.XPATH, XPATH_image)
                src = Image.get_attribute('src')
                
                Exist_dir = os.path.isdir('{}/Girl_{}_{}_{}'.format(self.Folder[k], self.Hair_color[k], self.Hair_style[k], self.Eye_color[k])) 

                if Exist_dir == False:
                    New_folder = '{}/Girl_{}_{}_{}'.format(self.Folder[k], self.Hair_color[k], self.Hair_style[k], self.Eye_color[k])
                    os.mkdir(New_folder)
                else:
                    New_folder = '{}/Girl_{}_{}_{}'.format(self.Folder[k], self.Hair_color[k], self.Hair_style[k], self.Eye_color[k])

                Image_name = "Girl_Image_{}.png".format(i)
                Image_folder = os.path.join(New_folder, Image_name)

                urllib.request.urlretrieve(src, Image_folder)

                # *
                time.sleep(self.Time_interval)

            Driver.close()

def main():
    
    CSV_path = r"C:\Users\Cesar\Dropbox\PC\Desktop\Waifus_csv\Waifus_data_csv.csv"

    Waifu = MakeGirlMOE(csv = CSV_path)

    Waifu.get_images_waifus_settings()

if __name__ == "__main__":
    main()