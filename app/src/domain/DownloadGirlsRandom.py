
import os
import time
import string
import random
import pandas as pd

import urllib.request

from .Decorators.Timer import Timer
from .Decorators.Singleton import Singleton

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#from memory_profiler import memory_usage
#from memory_profiler import profile

from .DropDown import Dropdown
from .OnOFFEvent import OnOffEvent
from .DataLoaderCSV import DataLoaderCSV
from .DownloadGirlsMOE import DownloadGirlsMOE
from ..Utilities import Settings

from typing import Optional

class DownloadGirlsRandom(DownloadGirlsMOE):
    
    """
    A class for downloading waifu images using Girls Moe, based on attributes specified in a CSV file.
    
    Parameters
    ----------
    Reader_CSV : DataLoaderCSV
        An instance of `DataLoaderCSV` containing the CSV data.
    CSV : str
        The path to the CSV file containing the waifu attributes.
    Folder : str
        The path to the folder where the images will be saved.
    Number_folders : int or None, optional
        The number of image folders to download. If `None`, all folders in the CSV file will be downloaded.
    
    Attributes
    ----------
    _Reader_CSV : DataLoaderCSV
        An instance of `DataLoaderCSV` containing the CSV data.
    _CSV : str
        The path to the CSV file containing the waifu attributes.
    _Folder_images : str
        The path to the folder where the images will be saved.
    _Number_folders : int or None, optional
        The number of image folders to download. If `None`, all folders in the CSV file will be downloaded.
    _URL : str
        The URL for the Girls Moe website.
    _Time_interval : float
        The time interval between each image download.
    _Initial : int
        The initial waiting time before starting the download process.
    _Data : pandas DataFrame
        The data in the CSV file.
    _Attributes : list of str
        The list of attribute names in the CSV file.
    _Model : list of str
        The list of model names in the CSV file.
    _Hair_color : list of str
        The list of hair color names in the CSV file.
    _Hair_style : list of str
        The list of hair style names in the CSV file.
    _Eye_color : list of str
        The list of eye color names in the CSV file.
    _Dark_sin : list of str
        The list of dark skin attributes in the CSV file.
    _Blush : list of str
        The list of blush attributes in the CSV file.
    _Smile : list of str
        The list of smile attributes in the CSV file.
    _Open_mouth : list of str
        The list of open mouth attributes in the CSV file.
    _Hat : list of str
        The list of hat attributes in the CSV file.
    _Ribbon : list of str
        The list of ribbon attributes in the CSV file.
    _Glasses : list of str
        The list of glasses attributes in the CSV file.
    _Epochs : list of int
        The list of epoch numbers in the CSV file.
    Chrome_options : webdriver.ChromeOptions
        The Chrome options for the web driver.
    
    Methods
    -------
    Images_waifus_random() -> None
        Downloads random waifu images and saves them to the specified folder.
    Images_waifus_settings() -> None
        Downloads waifu images based on the specified attributes and saves them to the specified folder.
    
    """

    # * Initializing (Constructor)
    def __init__(self, 
                 Folder: str, 
                 Number_images : int = 20,
                 Number_folders : int = 2) -> None:

        # * Instance attributes
        self._Folder_images = Folder
        self._Number_images = Number_images
        self._Number_folders = Number_folders

        self._URL = 'https://make.girls.moe/#/'
        self._Time_interval_chooses = 0.2
        self._Time_interval = 0.01
        self._implicitly = 20
        self._Initial = 5
        
        self.Chrome_options = webdriver.ChromeOptions() 
        self.Chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])


    def Download_images(self) -> None:
        """
        Downloads images of waifus with specified attributes from the MakeGirlsMoe website.
        """
        Dropdowns = []

        self.Models = ('Amaryllis 128x128 Ver.170716 (3.8MB)', 
                       'Bouvardia 128x128 Ver.171123 (9.8MB)', 
                       'Bouvardia 256x256 Ver.171125 (9.9MB)', 
                       'Camellia 256x256 Ver.171219 (9.9MB)')
        
        self.Hair_colors = ('Random',
                            'Blonde',
                            'Brown',
                            'Black',
                            'Blue',
                            'Pink',
                            'Purple',
                            'Green',
                            'Red',
                            'Silver',
                            'White',
                            'Orange',
                            'Aqua',
                            'Grey')
        
        self.Hair_styles = ('Random',
                            'Long Hair',
                            'Short Hair',
                            'Twin Tail',
                            'Drill Hair',
                            'Ponytail')
        
        
        self.Eye_color = ('Random',
                          'Blue',
                          'Red',
                          'Brown',
                          'Green',
                          'Purple',
                          'Yellow',
                          'Pink',
                          'Aqua',
                          'Black',
                          'Orange')
        
        Dropdowns.append(self.Models)
        Dropdowns.append(self.Hair_colors)
        Dropdowns.append(self.Hair_styles)
        Dropdowns.append(self.Eye_color)

        self.Toggle = ('ON',
                       'Random',
                       'OFF')
        

        Driver = webdriver.Chrome(options = self.Chrome_options)
        #Driver.maximize_window()
        Driver.get(self._URL)
        Driver.implicitly_wait(self._implicitly)
        
        for k in range(self._Number_folders):
            
            Choices_dropdowns = []     

            # * Interval times
            time.sleep(self._Initial)

            for j in range(len(Settings._XPATH_BUTTON_LIST_)):
                
                for l in range(len(Settings._XPATH_BUTTON_LIST_)):

                    Choices_dropdowns.append(random.choice(Dropdowns[l]))
                              
                Drop_down_model = Dropdown(Driver, 
                                           Settings._XPATH_BUTTON_LIST_[j], 
                                           Settings._XPATH_OPEN_LIST_[j])

                Drop_down_model.select_option(Choices_dropdowns[j])    

                # * Interval times
                time.sleep(self._Time_interval_chooses)   

            # * Function on off used
            for j in range(len(Settings._XPATH_OFF_BUTTON_)):
                
                Toggle = random.choice(self.Toggle)

                ON_OFF_event = OnOffEvent(Driver, 
                                          Settings._XPATH_OFF_BUTTON_[j], 
                                          Settings._XPATH_RANDOM_BUTTON_[j], 
                                          Settings._XPATH_ON_BUTTON_[j])

                ON_OFF_event.select_option(Toggle)

            # * Interval times
            time.sleep(self._Initial)

            # * Instance epoch
            for i in range(self._Number_images):
                
                # * Waits until the search box is present on the page
                Button_click = WebDriverWait(Driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, Settings._XPATH_BUTTON_)))

                '''Button_click = Driver.find_element(By.XPATH, 
                                                   Settings._XPATH_BUTTON_)'''
                
                Button_click.click()

                # * Interval times
                time.sleep(self._Time_interval)

                # * Read image
                Image = WebDriverWait(Driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, Settings._XPATH_IMAGE_)))
                
                '''Image = Driver.find_element(By.XPATH, 
                                            Settings._XPATH_IMAGE_)'''
                
                src = Image.get_attribute('src')
                
                New_folder = '{}/Girl_{}_{}_{}'.format(self._Folder_images,
                                                        Choices_dropdowns[1], 
                                                        Choices_dropdowns[2], 
                                                        Choices_dropdowns[3])

                # * Direction exist
                Exist_dir = os.path.isdir(New_folder) 

                if Exist_dir == False:
                    os.mkdir(New_folder)
                else:
                    New_folder

                # * Name girl images
                Image_name = "Girl_Image_{}.png".format(i)
                Image_folder = os.path.join(New_folder, Image_name)
                
                # * Download image from website
                urllib.request.urlretrieve(src, Image_folder)

                # * Interval times
                time.sleep(self._Time_interval)

        # * Close Google chrome 
        Driver.close()