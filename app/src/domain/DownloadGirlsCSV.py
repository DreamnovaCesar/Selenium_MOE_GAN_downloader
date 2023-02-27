
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

from .DownloadGirlsMOE import DownloadGirlsMOE
from ..Utilities import Settings

# ?
@Singleton.singleton
class WaifusDownloadCSV(DownloadGirlsMOE):
    """
    Utilities inheritance

    A class used to crop Mini-MIAS images using the coordinates from the website.

    Methods:

        data_dic():

        data_dic_row():

        model_dropdown(): description

        model_on_off(): description

        get_images_waifus_random(): description

    """

    # * Initializing (Constructor)
    def __init__(self, **kwargs) -> None:
        """
        Keyword Args:

        """

        # * Instance attributes
        self.__Folder_CSV = kwargs.get('csv', None)
        self.__Folder_images = kwargs.get('FI', None)

        self.__Number_images = kwargs.get('NI', None)

        # * chromedriver path
        self.__Path_chrome_driver = r"chromedriver.exe"

        #self.Number = kwargs.get('waifus', 50)
        self.__Time_interval = 0.05
        self.__Initial = 5

        # * utf_8_sig
        with open(self.__Folder_CSV, 'r', encoding = 'utf_8_sig') as CSV:
        
            Data = pd.read_csv(CSV)

            print(Data.columns.tolist())
            print(Data.columns[0])
            
            self.__Model = Data['Model'].tolist()
            self.__Hair_color = Data['Hair color'].tolist()
            self.__Hair_style = Data['Hair style'].tolist()
            self.__Eye_color = Data['Eye color'].tolist()
            self.__Dark_sin = Data['Dark sin'].tolist()
            self.__Blush = Data['Blush'].tolist()
            self.__Smile = Data['Smile'].tolist()
            self.__Open_mouth = Data['Open mouth'].tolist()
            self.__Hat = Data['Hat'].tolist()
            self.__Ribbon = Data['Ribbon'].tolist()
            self.__Glasses = Data['Glasses'].tolist()
            self.__Folder = Data['Folder'].tolist()
            self.__URL = Data['URL'].tolist()
            self.__Epochs = Data['Epochs'].tolist()


    # * Deleting (Calling destructor)
    def __del__(self):
        print('');

    # ?
    @staticmethod
    def model_dropdown(Driver : webdriver.Chrome(), 
                       XPATH_path: string, 
                       XPATH_path_list: string, 
                       Option_picked: string) -> None:
        
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

        Option_index = List_options.index(Option_picked)
        
        print('{}'.format(Option_picked))

        Options[Option_index].click()
    
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

        Option_index = List_options.index(Option_picked)
        
        print('{}'.format(Option_picked))

        Options[Option_index].click()

    # ?
    @staticmethod
    def model_on_off(Driver : webdriver.Chrome(), 
                     _XPATH_PATH_ON_ : string, 
                     _XPATH_PATH_RANDOM_ : string, 
                     _XPATH_PATH_OFF_ : string, 
                     Option_picked : string) -> None:

        # *
        if(Option_picked == 'ON'):
            Button = Driver.find_element(By.XPATH, _XPATH_PATH_ON_)
            Button.click()

        elif(Option_picked == 'Random'):
            Button = Driver.find_element(By.XPATH, _XPATH_PATH_RANDOM_)
            Button.click()

        elif(Option_picked == 'OFF'):
            Button = Driver.find_element(By.XPATH, _XPATH_PATH_OFF_)
            Button.click()

        else:   
            pass
        
    # ?
    @Timer.timer
    def get_images_waifus_random(self) -> None:
    
        # * Webdriver chrome activate
        Driver = webdriver.Chrome()
        Driver.get(self.__URL)

        # * Waiting time
        Driver.implicitly_wait(self.__Initial)
        
        time.sleep(self.__Initial)
        
        for i in range(self.__Number_images):

            Button_click = Driver.find_element(By.XPATH, Settings._XPATH_BUTTON_)
            Button_click.click()
            # *
            time.sleep(self.__Time_interval)

            Image = Driver.find_element(By.XPATH, Settings._XPATH_IMAGE_)
            src = Image.get_attribute('src')
            
            Image_name = "Image_{}.png".format(i)
            Image_folder = os.path.join(self.__Folder_images, Image_name)

            urllib.request.urlretrieve(src, Image_folder)

            # *
            time.sleep(self.__Time_interval)

        Driver.close()
    
    @Timer.timer
    def get_images_waifus_settings(self) -> None:
        
        # *
        for k in range(len(self.__Model)):
            
            # * Webdriver chrome activate

            chromeOptions = webdriver.ChromeOptions() 
            chromeOptions.add_experimental_option("prefs", {"profile.managed_default_content_settings.images": 2}) 
            chromeOptions.add_argument("--no-sandbox") 
            chromeOptions.add_argument("--disable-setuid-sandbox") 

            chromeOptions.add_argument("--remote-debugging-port=9222")  # this

            chromeOptions.add_argument("--disable-dev-shm-using") 
            chromeOptions.add_argument("--disable-extensions") 
            chromeOptions.add_argument("start-maximized") 
            chromeOptions.add_argument("disable-infobars")

            Driver = webdriver.Chrome()
            Driver.maximize_window()
            Driver.get(self.__URL[k])
            

            # * Waiting time
            Driver.implicitly_wait(self.__Initial)

            # * Function dropdown used
            self.model_dropdown(Driver, 
                                Settings._XPATH_MODEL_BUTTON_, 
                                Settings._XPATH_MODEL_OPEN_, 
                                self.__Model[k])
            
            self.model_dropdown(Driver, 
                                Settings._XPATH_HAIR_COLOR_BUTTON_, 
                                Settings._XPATH_HAIR_COLOR_OPEN_, 
                                self.__Hair_color[k])
            
            self.model_dropdown(Driver, 
                                Settings._XPATH_HAIR_STYLE_BUTTON_, 
                                Settings._XPATH_HAIR_STYLE_OPEN_, 
                                self.__Hair_style[k])
            
            self.model_dropdown(Driver, 
                                Settings._XPATH_EYE_COLOR_BUTTON_, 
                                Settings._XPATH_EYE_COLOR_OPEN_, 
                                self.__Eye_color[k])

            # * Function on off used
            self.model_on_off(Driver, 
                              Settings._XPATH_DARK_SKIN_OFF_BUTTON_, 
                              Settings._XPATH_DARK_SKIN_RANDOM_BUTTON_, 
                              Settings._XPATH_DARK_SKIN_ON_BUTTON_, 
                              self.__Dark_sin[k])
            
            self.model_on_off(Driver, 
                              Settings._XPATH_BLUSH_OFF_BUTTON_, 
                              Settings._XPATH_BLUSH_RANDOM_BUTTON_, 
                              Settings._XPATH_BLUSH_ON_BUTTON_,  
                              self.__Blush[k])
            
            self.model_on_off(Driver, 
                              Settings._XPATH_SMILE_OFF_BUTTON_, 
                              Settings._XPATH_SMILE_RANDOM_BUTTON_, 
                              Settings._XPATH_SMILE_ON_BUTTON_, 
                              self.__Smile[k])
            
            self.model_on_off(Driver, 
                              Settings._XPATH_OPEN_MOUTH_OFF_BUTTON_, 
                              Settings._XPATH_OPEN_MOUTH_RANDOM_BUTTON_, 
                              Settings._XPATH_OPEN_MOUTH_ON_BUTTON_, 
                              self.__Open_mouth[k])
            
            self.model_on_off(Driver, 
                              Settings._XPATH_HAT_OFF_BUTTON_, 
                              Settings._XPATH_HAT_RANDOM_BUTTON_, 
                              Settings._XPATH_HAT_ON_BUTTON_, 
                              self.__Hat[k])
            
            self.model_on_off(Driver, 
                              Settings._XPATH_RIBBON_OFF_BUTTON_, 
                              Settings._XPATH_RIBBON_RANDOM_BUTTON_, 
                              Settings._XPATH_RIBBON_ON_BUTTON_, 
                              self.__Ribbon[k])
            
            self.model_on_off(Driver, 
                              Settings._XPATH_GLASSES_OFF_BUTTON_, 
                              Settings._XPATH_GLASSES_RANDOM_BUTTON_, 
                              Settings._XPATH_GLASSES_ON_BUTTON_, 
                              self.__Glasses[k])

            # * Initial time
            time.sleep(self.__Initial)

            # * Instance epoch
            for i in range(self.__Epochs[k]):
                
                # *
                Button_click = Driver.find_element(By.XPATH, Settings._XPATH_BUTTON_)
                Button_click.click()

                # * Interval times
                time.sleep(self.__Time_interval)

                # * Read image
                Image = Driver.find_element(By.XPATH, Settings._XPATH_IMAGE_)
                src = Image.get_attribute('src')
                
                # * Direction exist
                Exist_dir = os.path.isdir('{}/Girl_{}_{}_{}'.format(self.__Folder_images, self.__Hair_color[k], self.__Hair_style[k], self.__Eye_color[k])) 

                if Exist_dir == False:
                    New_folder = '{}/Girl_{}_{}_{}'.format(self.__Folder_images, self.__Hair_color[k], self.__Hair_style[k], self.__Eye_color[k])
                    os.mkdir(New_folder)
                else:
                    New_folder = '{}/Girl_{}_{}_{}'.format(self.__Folder_images, self.__Hair_color[k], self.__Hair_style[k], self.__Eye_color[k])

                # * Name girl images
                Image_name = "Girl_Image_{}.png".format(i)
                Image_folder = os.path.join(New_folder, Image_name)
                
                # * Download image from website
                urllib.request.urlretrieve(src, Image_folder)

                # * Interval times
                time.sleep(self.__Time_interval)

            # * Close Google chrome 
            Driver.close()