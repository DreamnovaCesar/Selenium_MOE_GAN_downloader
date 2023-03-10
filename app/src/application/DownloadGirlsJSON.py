
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
    A class for downloading images of anime girls from the website
    https://make.girls.moe/#/ using a JSON file that specifies the
    attributes of the girls to download.

    Parameters
    ----------
    Folder : str
        The folder path to save the downloaded images.
    JSON_file : dict
        A dictionary that specifies the attributes of the girls to download.
    Epochs : int
        The number of epochs to run the program.

    Attributes
    ----------
    _Folder_images : str
        The folder path to save the downloaded images.
    _JSON_file : dict
        A dictionary that specifies the attributes of the girls to download.
    _Epochs : int
        The number of epochs to run the program.
    _URL : str
        The URL of the website to download images from.
    _Time_interval_chooses : float
        The time interval to wait before making a selection.
    _Time_interval : float
        The time interval to wait before performing the next action.
    _implicitly : int
        The amount of time in seconds to wait for a page to load.
    _Initial : int
        The number of images to start with.
    _JSON_file_keys_list : list
        A list of keys in the JSON file.
    _JSON_file_vals_list : list
        A list of values in the JSON file.
    Chrome_options : webdriver.ChromeOptions
        The Chrome options for the Selenium webdriver.

    Returns
    -------
    None

    Notes
    -----
    This class inherits from DownloadGirlsMOE.

    Examples
    --------
    >>> JSON_file = {"hair": ["blonde", "pink"], "attribute": ["smiling"]}
    >>> dl = DownloadGirlsJSON('images', JSON_file, 5)
    >>> dl.download()
    """

    # * Initializing (Constructor)
    def __init__(self, 
                 Folder: str,
                 JSON_file : dict, 
                 Epochs : int
                 ) -> None:

        """
        Initializes a new DownloadGirlsJSON instance.

        Parameters
        ----------
        JSON_file : str
            The path of the JSON file.
        Folder : str
            The folder where the downloaded images will be saved.
        Epochs : int
            The number of different combinations of attributes to use.
        """

        # * Instance attributes
        self._Folder_images = Folder;
        self._JSON_file = JSON_file;
        self._Epochs = int(Epochs);

        self._URL = 'https://make.girls.moe/#/';
        self._Time_interval_chooses = 0.5;
        self._Time_interval = 0.2;
        self._implicitly = 20;
        self._Initial = 3;
        
        # * list out keys and values separately
        self._JSON_file_keys_list = list(self._JSON_file.keys());
        self._JSON_file_vals_list = list(self._JSON_file.values());

        self.Chrome_options = webdriver.ChromeOptions();
        self.Chrome_options.add_experimental_option('excludeSwitches', ['enable-logging']);

    def Download_images(self) -> None:
        """
        Downloads images of waifus with specified attributes from the MakeGirlsMoe website.
        """

        Driver = webdriver.Chrome(options = self.Chrome_options);
        #Driver.maximize_window();
        Driver.get(self._URL);
        Driver.implicitly_wait(self._implicitly);
        
        # * Interval times
        time.sleep(self._Initial);

        for j in range(len(Settings._XPATH_BUTTON_LIST_)):

            Drop_down_model = Dropdown(Driver, 
                                        Settings._XPATH_BUTTON_LIST_[j], 
                                        Settings._XPATH_OPEN_LIST_[j])

            Drop_down_model.select_option(self._JSON_file_vals_list[j])

            # * Interval times
            time.sleep(self._Time_interval_chooses); 

        if(self._JSON_file_vals_list[0] == 'Amaryllis 128x128 Ver.170716 (3.8MB)'):
            Settings._XPATH_OFF_BUTTON_.pop();
            Settings._XPATH_RANDOM_BUTTON_.pop();
            Settings._XPATH_ON_BUTTON_.pop();

        # * Function on off used
        for n in range(len(Settings._XPATH_OFF_BUTTON_)):

            ON_OFF_event = OnOffEvent(Driver, 
                                        Settings._XPATH_ON_BUTTON_[n], 
                                        Settings._XPATH_RANDOM_BUTTON_[n], 
                                        Settings._XPATH_OFF_BUTTON_[n])

            ON_OFF_event.select_option(self._JSON_file_vals_list[n + len(Settings._XPATH_BUTTON_LIST_)]);
        
        # * Path name
        New_folder = '{}/Girl_{}_{}_{}'.format(self._Folder_images, 
                                                    self._JSON_file_vals_list[1], 
                                                    self._JSON_file_vals_list[2], 
                                                    self._JSON_file_vals_list[3]);
        # * Path exist
        Exist_dir = os.path.isdir(New_folder);

        if(Exist_dir) == False:
            os.mkdir(New_folder);
        else:
            New_folder;
        
        # * Json file name
        File_json = "Data_{}_{}_{}.json".format(self._JSON_file_vals_list[1], 
                                                self._JSON_file_vals_list[2], 
                                                self._JSON_file_vals_list[3]);
        
        # * Interval times
        time.sleep(self._Initial);

        # * Instance epoch
        for i in range(self._Epochs):
               
            # * Waits until the search box is present on the page
            Button_click = WebDriverWait(Driver, 10).until(
                EC.presence_of_element_located((By.XPATH, Settings._XPATH_BUTTON_)));

            '''Button_click = Driver.find_element(By.XPATH, 
                                                Settings._XPATH_BUTTON_)'''
            
            Button_click.click();

            # * Interval times
            time.sleep(self._Time_interval);

            # * Read image
            Image = WebDriverWait(Driver, 10).until(
                EC.presence_of_element_located((By.XPATH, Settings._XPATH_IMAGE_)));
            
            '''Image = Driver.find_element(By.XPATH, 
                                        Settings._XPATH_IMAGE_)
            
            Image1 = Driver.find_element(By.XPATH, Settings._XPATH_IMAGE_);'''

            src = Image.get_attribute('src');
            
            # * Interval times
            time.sleep(self._Time_interval);

            # * Name girl images
            Image_name = "Girl_Image_{}.png".format(i);
            Image_folder = os.path.join(New_folder, Image_name);
            
            # * Download image from website
            urllib.request.urlretrieve(src, Image_folder);

            # * Interval times
            time.sleep(self._Time_interval);

        # * Create path for the JSON file
        File_json_folder = os.path.join(New_folder, File_json);

        # * Save the Json file inside each new folder created
        JsonFileHandler.create_json_file(self._JSON_file, File_json_folder);

        # * Close Google chrome 
        Driver.close();