
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
    A class for downloading images of waifus with specified attributes from the MakeGirlsMoe website.

    Parameters
    ----------
    Folder : str
        The folder where the downloaded images will be saved.
    Number_images : int, optional
        The number of images to download for each combination of attributes. Default is 20.
    Number_folders : int, optional
        The number of different combinations of attributes to use. Default is 2.

    Attributes
    ----------
    _Folder_images : str
        The folder where the downloaded images will be saved.
    _Number_images : int
        The number of images to download for each combination of attributes.
    _Number_folders : int
        The number of different combinations of attributes to use.
    _URL : str
        The URL of the MakeGirlsMoe website.
    _Time_interval_chooses : float
        The time interval (in seconds) to wait after selecting an attribute from a dropdown list.
    _Time_interval : float
        The time interval (in seconds) to wait after clicking a button or downloading an image.
    _implicitly : int
        The implicit wait time (in seconds) for the webdriver.
    _Initial : int
        The initial wait time (in seconds) before starting to select attributes and download images.
    Chrome_options : webdriver.ChromeOptions
        The options for the Google Chrome browser.
    Models : tuple
        The available models for waifus.
    Hair_colors : tuple
        The available colors for waifu hair.
    Hair_styles : tuple
        The available styles for waifu hair.
    Eye_color : tuple
        The available colors for waifu eyes.
    Toggle : tuple
        The available options for the on/off toggles.
    
    Methods
    -------
    Download_images()
        Downloads images of waifus with specified attributes from the MakeGirlsMoe website.
    """

    # * Initializing (Constructor)
    
    def __init__(self, 
                 Folder: str, 
                 Number_images : int = 20,
                 Number_folders : int = 2) -> None:

        """
        Initializes a new DownloadGirlsRandom instance.

        Parameters
        ----------
        Folder : str
            The folder where the downloaded images will be saved.
        Number_images : int, optional
            The number of images to download for each combination of attributes. Default is 20.
        Number_folders : int, optional
            The number of different combinations of attributes to use. Default is 2.
        """

        # * Instance attributes
        self._Folder_images = Folder
        self._Number_images = Number_images
        self._Number_folders = Number_folders

        self._URL = 'https://make.girls.moe/#/'
        self._Time_interval_chooses = 0.5
        self._Time_interval = 0.01
        self._implicitly = 20
        self._Initial = 5
        
        self.Chrome_options = webdriver.ChromeOptions() 
        self.Chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])


    def Download_images(self) -> None:
        """
        Downloads images of waifus with specified attributes from the MakeGirlsMoe website.
        """

        # * Create lists of dropdown options for each attribute
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
        
        # * Add each list of dropdown options to a larger list
        Dropdowns.append(self.Models)
        Dropdowns.append(self.Hair_colors)
        Dropdowns.append(self.Hair_styles)
        Dropdowns.append(self.Eye_color)

        # * Create list of toggle options
        self.Toggle = ('ON',
                       'Random',
                       'OFF')
        
        # * Launch Google Chrome browser using specified options
        Driver = webdriver.Chrome(options = self.Chrome_options)
        #Driver.maximize_window()
        Driver.get(self._URL)
        Driver.implicitly_wait(self._implicitly)
        
        # * Loop through the specified number of folders
        for _ in range(self._Number_folders):
            
            # * Interval times
            time.sleep(self._Initial)

            # * Create list of randomly selected dropdown options for each attribute
            Choices_dropdowns = []     
            
            # * Loop through each dropdown element on the page
            for j in range(len(Settings._XPATH_BUTTON_LIST_)):
                
                # * Add a randomly selected option from each dropdown to the list
                for l in range(len(Settings._XPATH_BUTTON_LIST_)):

                    Choices_dropdowns.append(random.choice(Dropdowns[l]))

                # * Select the chosen option for the dropdown
                Drop_down_model = Dropdown(Driver, 
                                           Settings._XPATH_BUTTON_LIST_[j], 
                                           Settings._XPATH_OPEN_LIST_[j])

                Drop_down_model.select_option(Choices_dropdowns[j])    

                # * Interval times
                time.sleep(self._Time_interval_chooses)   

            # If the chosen model is Amaryllis, remove the toggle buttons
            if(Choices_dropdowns[0] == 'Amaryllis 128x128 Ver.170716 (3.8MB)'):
                Settings._XPATH_OFF_BUTTON_.pop()
                Settings._XPATH_RANDOM_BUTTON_.pop()
                Settings._XPATH_ON_BUTTON_.pop()
            
            # * Loop through each toggle button element on the page
            for j in range(len(Settings._XPATH_OFF_BUTTON_)):
                
                # * Select a randomly chosen toggle option
                Toggle = random.choice(self.Toggle)

                # * Click the corresponding toggle button
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