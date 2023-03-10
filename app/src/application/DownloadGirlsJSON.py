
import os
import time
import urllib.request

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#from memory_profiler import memory_usage
#from memory_profiler import profile

from ..domain.Json.JsonFileHander import JsonFileHandler
from ..domain.DropDown import Dropdown
from ..domain.OnOFFEvent import OnOffEvent

from .DownloadGirlsMOE import DownloadGirlsMOE
from ..Utilities import Settings

from typing import Dict

class DownloadGirlsJSON(DownloadGirlsMOE):
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
                 Folder: str,
                 JSON_file : dict, 
                 Epochs : int
                 ) -> None:

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
        self._Folder_images = Folder
        self._JSON_file = JSON_file
        self._Epochs = int(Epochs)

        self._URL = 'https://make.girls.moe/#/'
        self._Time_interval_chooses = 0.5
        self._Time_interval = 0.01
        self._implicitly = 20
        self._Initial = 5
        
        # * list out keys and values separately
        self._JSON_file_keys_list = list(self._JSON_file.keys())
        self._JSON_file_vals_list = list(self._JSON_file.values())

        self.Chrome_options = webdriver.ChromeOptions() 
        self.Chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])

    def Download_images(self) -> None:
        """
        Downloads images of waifus with specified attributes from the MakeGirlsMoe website.
        """

        Driver = webdriver.Chrome(options = self.Chrome_options)
        #Driver.maximize_window()
        Driver.get(self._URL)
        Driver.implicitly_wait(self._implicitly)
        
        # * Interval times
        time.sleep(self._Initial)

        for j in range(len(Settings._XPATH_BUTTON_LIST_)):

            Drop_down_model = Dropdown(Driver, 
                                        Settings._XPATH_BUTTON_LIST_[j], 
                                        Settings._XPATH_OPEN_LIST_[j])

            Drop_down_model.select_option(self._JSON_file_vals_list[j])

            # * Interval times
            time.sleep(self._Time_interval_chooses) 

        if(self._JSON_file_vals_list[0] == 'Amaryllis 128x128 Ver.170716 (3.8MB)'):
            Settings._XPATH_OFF_BUTTON_.pop()
            Settings._XPATH_RANDOM_BUTTON_.pop()
            Settings._XPATH_ON_BUTTON_.pop()

        # * Function on off used
        for n in range(len(Settings._XPATH_OFF_BUTTON_)):

            ON_OFF_event = OnOffEvent(Driver, 
                                        Settings._XPATH_ON_BUTTON_[n], 
                                        Settings._XPATH_RANDOM_BUTTON_[n], 
                                        Settings._XPATH_OFF_BUTTON_[n])

            ON_OFF_event.select_option(self._JSON_file_vals_list[n + len(Settings._XPATH_BUTTON_LIST_)])
        
        # * Path name
        New_folder = '{}/Girl_{}_{}_{}'.format(self._Folder_images, 
                                                    self._JSON_file_vals_list[1], 
                                                    self._JSON_file_vals_list[2], 
                                                    self._JSON_file_vals_list[3])
        # * Path exist
        Exist_dir = os.path.isdir(New_folder) 

        if Exist_dir == False:
            os.mkdir(New_folder)
        else:
            New_folder
            
        # * Interval times
        time.sleep(self._Initial)

        # * Instance epoch
        for i in range(self._Epochs):
            
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
                                        Settings._XPATH_IMAGE_)
            
            Image1 = Driver.find_element(By.XPATH, Settings._XPATH_IMAGE_);'''

            src = Image.get_attribute('src')
            
            # * Json file name
            File_json = "Data_{}_{}_{}.json".format(self._JSON_file_vals_list[1], 
                                                    self._JSON_file_vals_list[2], 
                                                    self._JSON_file_vals_list[3])
            
            File_json_folder = os.path.join(New_folder, File_json)

            # * Name girl images
            Image_name = "Girl_Image_{}.png".format(i)
            Image_folder = os.path.join(New_folder, Image_name)
            
            # * Download image from website
            urllib.request.urlretrieve(src, Image_folder)

            # * Interval times
            time.sleep(self._Time_interval)

        # * Save the Json file inside each new folder created
        JsonFileHandler.create_json_file(self._JSON_file, File_json_folder)

        # * Close Google chrome 
        Driver.close()