
import os
import time
import string
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

class DownloadGirlsSettings(DownloadGirlsMOE):
    
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
        self._implicitly = 20
        self._Initial = 3
        
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

        self.Chrome_options = webdriver.ChromeOptions() 
        self.Chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])

    def Download_images(self) -> None:
        """
        Downloads images of waifus with specified attributes from the MakeGirlsMoe website.
        """

        Driver = webdriver.Chrome(options = self.Chrome_options)
        Driver.maximize_window()
        Driver.get(self._URL)
        Driver.implicitly_wait(self._implicitly)
        
        for k in range(len(self._Data.index)):
                  
            for j in range(len(Settings._XPATH_BUTTON_LIST_)):

                Drop_down_model = Dropdown(Driver, 
                                           Settings._XPATH_BUTTON_LIST_[j], 
                                           Settings._XPATH_OPEN_LIST_[j])

                Drop_down_model.select_option(self._Attributes[j][k])

            # * Function on off used
            for n in range(len(Settings._XPATH_OFF_BUTTON_)):
            
                ON_OFF_event = OnOffEvent(Driver, 
                                          Settings._XPATH_ON_BUTTON_[n], 
                                          Settings._XPATH_RANDOM_BUTTON_[n], 
                                          Settings._XPATH_OFF_BUTTON_[n])

                ON_OFF_event.select_option(self._Attributes[n + len(Settings._XPATH_BUTTON_LIST_)][k])
            
            # * Interval times
            time.sleep(self._Initial)

            # * Instance epoch
            for i in range(self._Epochs[k]):
                
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
                                                        self._Hair_color[k], 
                                                        self._Hair_style[k], 
                                                        self._Eye_color[k])
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