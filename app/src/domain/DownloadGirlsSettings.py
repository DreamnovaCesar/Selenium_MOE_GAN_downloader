
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
    Downloads images of waifus with specified attributes from the MakeGirlsMoe website.

    Parameters
    ----------
    Reader_CSV : DataLoaderCSV
        An instance of `DataLoaderCSV` containing the data to use for downloading the images.
    CSV : str
        The path to the CSV file used to load the data.
    Folder : str
        The path to the folder where the downloaded images will be stored.
    Number_folders : int, optional
        The number of folders to create in the `Folder` directory. If not specified, one folder will be created for each row in the CSV file.

    Attributes
    ----------
    Chrome_options : webdriver.ChromeOptions
        The Chrome options used to configure the Chrome driver.
    _Reader_CSV : DataLoaderCSV
        The instance of `DataLoaderCSV` used to load the data.
    _CSV : str
        The path to the CSV file used to load the data.
    _Folder_images : str
        The path to the folder where the downloaded images will be stored.
    _Number_folders : int
        The number of folders to create in the `Folder` directory.
    _URL : str
        The URL of the MakeGirlsMoe website.
    _Time_interval_chooses : float
        The time interval in seconds between selecting dropdown options.
    _Time_interval : float
        The time interval in seconds between clicking buttons and waiting for the page to load.
    _implicitly : int
        The maximum time in seconds to wait for an element to be found on the page.
    _Initial : int
        The initial time in seconds to wait before starting to select dropdown options.
    _Data : np.ndarray
        The data loaded from the CSV file.
    _Attributes : List[List[str]]
        The list of attribute values for each row of the CSV file.
    _Model : str
        The model used to generate the images.
    _Hair_color : List[str]
        The list of hair colors for each row of the CSV file.
    _Hair_style : List[str]
        The list of hair styles for each row of the CSV file.
    _Eye_color : List[str]
        The list of eye colors for each row of the CSV file.
    _Dark_sin : List[str]
        The list of dark skin options for each row of the CSV file.
    _Blush : List[str]
        The list of blush options for each row of the CSV file.
    _Smile : List[str]
        The list of smile options for each row of the CSV file.
    _Open_mouth : List[str]
        The list of open mouth options for each row of the CSV file.
    _Hat : List[str]
        The list of hat options for each row of the CSV file.
    _Ribbon : List[str]
        The list of ribbon options for each row of the CSV file.
    _Glasses : List[str]
        The list of glasses options for each row of the CSV file.
    _Epochs : List[int]
        The list of number of images to download for each row of the CSV file.

    Methods
    -------
    Download_images()
        Downloads the images of waifus with specified attributes from the MakeGirlsMoe website.

    """

    # * Initializing (Constructor)
    def __init__(self, 
                 Reader_CSV : DataLoaderCSV, 
                 CSV: str, 
                 Folder: str, 
                 Number_folders: Optional[int] = None) -> None:

        """
        Initializes a new DownloadGirlsRandom instance.

        Parameters
        ----------
        Reader_CSV : DataLoaderCSV
            A DataLoaderCSV instance.
        CSV : str
            The path of the csv file.
        Folder : str
            The folder where the downloaded images will be saved.
        Number_folders : int, optional
            The number of different combinations of attributes to use. Default is None.
        """
        
        # * Instance attributes
        self._Reader_CSV = Reader_CSV
        self._CSV = CSV
        self._Folder_images = Folder
        self._Number_folders = Number_folders

        self._URL = 'https://make.girls.moe/#/'
        self._Time_interval_chooses = 0.5
        self._Time_interval = 0.01
        self._implicitly = 20
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
            
            # * Interval times
            time.sleep(self._Initial)

            for j in range(len(Settings._XPATH_BUTTON_LIST_)):

                Drop_down_model = Dropdown(Driver, 
                                           Settings._XPATH_BUTTON_LIST_[j], 
                                           Settings._XPATH_OPEN_LIST_[j])

                Drop_down_model.select_option(self._Attributes[j][k])

                # * Interval times
                time.sleep(self._Time_interval_chooses) 

            if(self._Model == 'Amaryllis 128x128 Ver.170716 (3.8MB)'):
                Settings._XPATH_OFF_BUTTON_.pop()
                Settings._XPATH_RANDOM_BUTTON_.pop()
                Settings._XPATH_ON_BUTTON_.pop()

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