
# ?
import os
import time
import string
import pandas as pd

# ?
import urllib.request

# ?
from selenium import webdriver
from selenium.webdriver.common.by import By

# ?
from functools import wraps

# ?
from memory_profiler import memory_usage
from memory_profiler import profile

from ..Utilities import Settings

# ?
class WaifusDownloadCSV(object):
    """
    Utilities inheritance

    A class used to crop Mini-MIAS images using the coordinates from the website.

    Methods:

        data_dic():
    
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
        self.__Model = kwargs.get('model', None)
        self.__Hair_color = kwargs.get('haircolor', None)
        self.__Hair_style = kwargs.get('hairstyle', None)
        self.__Eye_color = kwargs.get('eyecolor', None)
        self.__Dark_sin = kwargs.get('darksin', None)
        self.__Blush = kwargs.get('blush', None)
        self.__Smile = kwargs.get('smile', None)
        self.__Open_mouth = kwargs.get('openmouth', None)
        self.__Hat = kwargs.get('hat', None)
        self.__Ribbon = kwargs.get('ribbon', None)
        self.__Glasses = kwargs.get('Glasses', None)
        self.__Folder = kwargs.get('Folder', None)
        self.__URL = kwargs.get('URL', None)
        self.__Epochs = kwargs.get('epochs', None)

        self.__Folder_images = kwargs.get('FI', None)
        self.__Number_images = kwargs.get('NI', None)

        # * chromedriver path
        self.__Path_chrome_driver = r"chromedriver.exe"

        #self.Number = kwargs.get('waifus', 50)
        self.__Time_interval = 0.05
        self.__Initial = 5

    # * Class variables
    def __repr__(self):
            return f"""[{self.__Folder_images},
                        {self.__Number_images},
                        {self.__Time_interval},
                        {self.__Initial}]""";

    # * Class description
    def __str__(self):
        return  f'';
    
    # * Deleting (Calling destructor)
    def __del__(self):
        print('');

    # * Get data from a dic
    def data_dic(self):

        return {'Folder_CSV': str(self.__Folder_CSV),
                'Folder_images': str(self.__Folder_images),
                'Number_images': str(self.__Number_images)
                };
    
    # * Get data from a dic row
    def data_dic_row(self):

        return {'Model': str(self.__Model),
                'Hair_color': str(self.__Hair_color),
                'Hair_style': str(self.__Hair_style),
                'Eye_color': str(self.__Eye_color),
                'Dark_sin': str(self.__Dark_sin),
                'Blush': str(self.__Blush),
                'Smile': str(self.__Smile),
                'Open_mouth': str(self.__Open_mouth),
                'Hat': str(self.__Hat),
                'Ribbon': str(self.__Ribbon),
                'Glasses': str(self.__Glasses),
                'Folder': str(self.__Folder),
                'URL': str(self.__URL),
                'Epochs': str(self.__Epochs)
                };
    
    # * __Folder_CSV attribute
    @property
    def __Folder_CSV_property(self):
        return self.__Folder_CSV

    @__Folder_CSV_property.setter
    def __Folder_CSV_property(self, New_value):
        if not isinstance(New_value, str):
            raise TypeError("CSV must be a string") #! Alert
        self.__Folder_CSV = New_value
    
    @__Folder_CSV_property.deleter
    def __Folder_CSV_property(self):
        print("Deleting CSV...")
        del self.__Folder_CSV

    # * __Folder_images attribute
    @property
    def __Folder_images_property(self):
        return self.__Folder_images

    @__Folder_images_property.setter
    def __Folder_images_property(self, New_value):
        if not isinstance(New_value, str):
            raise TypeError("folder images must be a string") #! Alert
        self.__Folder_images = New_value
    
    @__Folder_images_property.deleter
    def __Folder_images_property(self):
        print("Deleting folder images...")
        del self.__Folder_CSV
        
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

        Option_index = List_options.index(Option_picked)
        
        print('{}'.format(Option_picked))

        Options[Option_index].click()
    
    @staticmethod
    def model_on_off(Driver, XPATH_path_on: string, XPATH_path_random: string, XPATH_path_off: string, Option_picked: string) -> None:

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
    
    def get_images_waifus_random(self) -> None:
    
        # *
        XPATH_image = '//*[@id="root"]/div/div/div/div/div[1]/div[2]/div[1]/div/div[1]/div/div/img'
        XPATH_button = '//*[@id="root"]/div/div/div/div/div[1]/div[2]/div[1]/div/button'

        # * Webdriver chrome activate
        Driver = webdriver.Chrome()
        Driver.get(self.__URL)

        # * Waiting time
        Driver.implicitly_wait(self.__Initial)
        
        time.sleep(self.__Initial)
        
        for i in range(self.__Number_images):

            Button_click = Driver.find_element(By.XPATH, XPATH_button)
            Button_click.click()
            # *
            time.sleep(self.__Time_interval)

            Image = Driver.find_element(By.XPATH, XPATH_image)
            src = Image.get_attribute('src')
            
            Image_name = "Image_{}.png".format(i)
            Image_folder = os.path.join(self.__Folder_images, Image_name)

            urllib.request.urlretrieve(src, Image_folder)

            # *
            time.sleep(self.__Time_interval)

        Driver.close()
    
    def get_images_waifus_settings(self) -> None:
        
        
        # * Dropdown items model
        XPATH_model_button = '//*[@id="root"]/div/div/div/div/div[1]/div[2]/div[2]/div/div[2]/div/div/button'
        XPATH_model_open = '//*[@id="root"]/div/div/div/div/div[1]/div[2]/div[2]/div/div[2]/div/div/ul'

        # * Dropdown items
        XPATH_hair_color_button = '//*[@id="root"]/div/div/div/div/div[1]/div[2]/div[2]/div/div[3]/div[1]/div/button'
        XPATH_hair_color_open = '//*[@id="root"]/div/div/div/div/div[1]/div[2]/div[2]/div/div[3]/div[1]/div/ul'

        XPATH_hair_style_button = '//*[@id="root"]/div/div/div/div/div[1]/div[2]/div[2]/div/div[3]/div[2]/div/button'
        XPATH_hair_style_open = '//*[@id="root"]/div/div/div/div/div[1]/div[2]/div[2]/div/div[3]/div[2]/div/ul'

        XPATH_Eye_color_button = '//*[@id="root"]/div/div/div/div/div[1]/div[2]/div[2]/div/div[3]/div[3]/div/button'
        XPATH_Eye_color_open = '//*[@id="root"]/div/div/div/div/div[1]/div[2]/div[2]/div/div[3]/div[3]/div/ul'

        # * On, off and random buttons.
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
        #XPATH_image = '//*[@id="root"]/div/div/div/div/div[1]/div[2]/div[1]/div/div[1]'
        XPATH_image_button = '//*[@id="root"]/div/div/div/div/div[1]/div[2]/div[1]/div/button'

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
            self.model_dropdown(Driver, XPATH_model_button, XPATH_model_open, self.__Model[k])
            self.model_dropdown(Driver, XPATH_hair_color_button, XPATH_hair_color_open, self.__Hair_color[k])
            self.model_dropdown(Driver, XPATH_hair_style_button, XPATH_hair_style_open, self.__Hair_style[k])
            self.model_dropdown(Driver, XPATH_Eye_color_button, XPATH_Eye_color_open, self.__Eye_color[k])

            # * Function on off used
            self.model_on_off(Driver, XPATH_dark_skin_off_button, XPATH_dark_skin_random_button, XPATH_dark_skin_on_button, self.__Dark_sin[k])
            self.model_on_off(Driver, XPATH_blush_off_button, XPATH_blush_random_button, XPATH_blush_on_button,  self.__Blush[k])
            self.model_on_off(Driver, XPATH_smile_off_button, XPATH_smile_random_button, XPATH_smile_on_button, self.__Smile[k])
            self.model_on_off(Driver, XPATH_open_mouth_off_button, XPATH_open_mouth_random_button, XPATH_open_mouth_on_button, self.__Open_mouth[k])
            self.model_on_off(Driver, XPATH_hat_off_button, XPATH_hat_random_button, XPATH_hat_on_button, self.__Hat[k])
            self.model_on_off(Driver, XPATH_ribbon_off_button, XPATH_ribbon_random_button, XPATH_ribbon_on_button, self.__Ribbon[k])
            self.model_on_off(Driver, XPATH_glasses_off_button, XPATH_glasses_random_button, XPATH_glasses_on_button, self.__Glasses[k])

            # * Initial time
            time.sleep(self.__Initial)

            # * Instance epoch
            for i in range(self.__Epochs[k]):
                
                # *
                Button_click = Driver.find_element(By.XPATH, XPATH_image_button)
                Button_click.click()

                # * Interval times
                time.sleep(self.__Time_interval)

                # * Read image
                Image = Driver.find_element(By.XPATH, XPATH_image)
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