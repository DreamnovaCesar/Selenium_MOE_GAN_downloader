
import os
import time
import string
import pandas as pd

import urllib.request

from .Decorators.Timer import Timer
from .Decorators.Singleton import Singleton

from selenium import webdriver
from selenium.webdriver.common.by import By

#from memory_profiler import memory_usage
#from memory_profiler import profile

from .DropDownModel import DropdownModel
from .OnOFFEvent import OnOffEvent
from .DataLoaderCSV import DataLoaderCSV
from .DownloadGirlsMOE import DownloadGirlsMOE
from ..Utilities import Settings

from typing import Optional

class WaifusDownloadCSV(DownloadGirlsMOE):
  
    # * Initializing (Constructor)
    def __init__(self, 
                 Reader_CSV : DataLoaderCSV, 
                 CSV: str, 
                 Folder: str, 
                 Number_folders: Optional[int] = None) -> None:

        # * Instance attributes
        self._Reader_CSV = Reader_CSV
        self._CSV = CSV
        self._Folder_images = Folder
        self._Number_folders = Number_folders

        self._URL = 'https://make.girls.moe/#/'
        self._Time_interval = 0.05
        self._Initial = 5
        
        self._Data = Reader_CSV.Data
        self._Attributes = Reader_CSV.Attributes

        self._Model = Reader_CSV.Model
        self._Hair_color = Reader_CSV.Hair_color
        self._Hair_style = Reader_CSV.Hair_style
        self._Eye_color = Reader_CSV.Eye_color
        self._Dark_sin = Reader_CSV.Dark_sin
        self._Blush = Reader_CSV.Blush
        self._Smile = Reader_CSV.Smile
        self._Open_mouth = Reader_CSV.Open_mouth
        self._Hat = Reader_CSV.Hat
        self._Ribbon = Reader_CSV.Ribbon
        self._Glasses = Reader_CSV.Glasses
        self._Epochs = Reader_CSV.Epochs

    # ?
    @Timer.timer
    def Images_waifus_random(self) -> None:
    
        # * Webdriver chrome activate
        Driver = webdriver.Chrome()
        Driver.get(self._URL)

        # * Waiting time
        Driver.implicitly_wait(self._Initial)
        
        time.sleep(self._Initial)
        
        for i in range(self._Number_folders):

            Button_click = Driver.find_element(By.XPATH, 
                                               Settings._XPATH_BUTTON_)
            Button_click.click()
            # *
            time.sleep(self._Time_interval)

            Image = Driver.find_element(By.XPATH, 
                                        Settings._XPATH_IMAGE_)
            src = Image.get_attribute('src')
            
            Image_name = "Image_{}.png".format(i)
            Image_folder = os.path.join(self._Folder_images, Image_name)

            urllib.request.urlretrieve(src, Image_folder)

            # *
            time.sleep(self._Time_interval)

        Driver.close()
    
    @Timer.timer
    def Images_waifus_settings(self) -> None:
        
        Chrome_options = webdriver.ChromeOptions() 
        Chrome_options.add_experimental_option("prefs", {"profile.managed_default_content_settings.images": 2}) 
        Chrome_options.add_argument("--no-sandbox") 
        Chrome_options.add_argument("--disable-setuid-sandbox") 

        Chrome_options.add_argument("--remote-debugging-port=9222")  # this

        Chrome_options.add_argument("--disable-dev-shm-using") 
        Chrome_options.add_argument("--disable-extensions") 
        Chrome_options.add_argument("start-maximized") 
        Chrome_options.add_argument("disable-infobars")

        
        # *
        for k in range(len(self._Data.index)):
            
            Driver = webdriver.Chrome()
            Driver.maximize_window()
            Driver.get(self._URL)
            
            # * Waiting time
            Driver.implicitly_wait(self._Initial)

            for j in range(len(Settings._XPATH_BUTTON_LIST_)):

                Drop_down_model = DropdownModel(Driver, 
                                                Settings._XPATH_BUTTON_LIST_[j], 
                                                Settings._XPATH_OPEN_LIST_[j])

                Drop_down_model.select_option(self._Attributes[j][k])

            # * Function on off used
            for j in range(len(Settings._XPATH_OFF_BUTTON_)):
            
                ON_OFF_event = OnOffEvent(Driver, 
                                        Settings._XPATH_OFF_BUTTON_[j], 
                                        Settings._XPATH_RANDOM_BUTTON_[j], 
                                        Settings._XPATH_ON_BUTTON_[j])

                ON_OFF_event.select_option(self._Attributes[j][k])
            
            # * Initial time
            time.sleep(self._Initial)

            # * Instance epoch
            for i in range(self._Epochs[k]):
                
                # *
                Button_click = Driver.find_element(By.XPATH, Settings._XPATH_BUTTON_)
                Button_click.click()

                # * Interval times
                time.sleep(self._Time_interval)

                # * Read image
                Image = Driver.find_element(By.XPATH, Settings._XPATH_IMAGE_)
                src = Image.get_attribute('src')
                
                # * Direction exist
                Exist_dir = os.path.isdir('{}/Girl_{}_{}_{}'.format(self._Folder_images, 
                                                                    self._Hair_color[k], 
                                                                    self._Hair_style[k], 
                                                                    self._Eye_color[k])) 

                if Exist_dir == False:
                    New_folder = '{}/Girl_{}_{}_{}'.format(self._Folder_images, 
                                                           self._Hair_color[k], 
                                                           self._Hair_style[k], 
                                                           self._Eye_color[k])
                    os.mkdir(New_folder)
                else:
                    New_folder = '{}/Girl_{}_{}_{}'.format(self._Folder_images, 
                                                           self._Hair_color[k], 
                                                           self._Hair_style[k], 
                                                           self._Eye_color[k])

                # * Name girl images
                Image_name = "Girl_Image_{}.png".format(i)
                Image_folder = os.path.join(New_folder, Image_name)
                
                # * Download image from website
                urllib.request.urlretrieve(src, Image_folder)

                # * Interval times
                time.sleep(self._Time_interval)

            # * Close Google chrome 
            Driver.close()