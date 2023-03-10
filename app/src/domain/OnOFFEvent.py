from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class OnOffEvent(object):
    """
    A class for performing on-off events on a web page.

    Attributes
    ----------
    Driver : webdriver.Chrome
        The Chrome webdriver instance.
    XPATH_ON : str
        The XPath of the "ON" button.
    XPATH_Random : str
        The XPath of the "Random" button.
    XPATH_OFF : str
        The XPath of the "OFF" button.

    Methods
    -------
    select_option(self, Option_picked: str) -> None:
        Selects an option depending on the value of Option_picked.
    """

    def __init__(self, 
                 Driver: webdriver.Chrome, 
                 XPATH_ON: str, 
                 XPATH_Random: str, 
                 XPATH_OFF: str):
        
        """
        Constructs the necessary attributes for the OnOffEvent object.

        Parameters
        ----------
        Driver : webdriver.Chrome
            The Chrome webdriver instance.
        XPATH_ON : str
            The XPath of the "ON" button.
        XPATH_Random : str
            The XPath of the "Random" button.
        XPATH_OFF : str
            The XPath of the "OFF" button.
        """

        self.Driver = Driver
        self.XPATH_ON = XPATH_ON
        self.XPATH_Random = XPATH_Random
        self.XPATH_OFF = XPATH_OFF

    def select_option(self, Option_picked: str) -> None:
        """
        Selects an option depending on the value of Option_picked.

        Parameters
        ----------
        Option_picked : str
            The option that needs to be selected. It can be 'ON', 'Random' or 'OFF'.

        Returns
        -------
        None
        """

        # * Print the option that was picked
        print(Option_picked)

        # * If ON is selected
        if Option_picked == 'ON':
            # * Wait for the element to be present
            button = WebDriverWait(self.Driver, 0.2).until(
                EC.presence_of_element_located((By.XPATH, self.XPATH_ON)))
            
            #button = self.Driver.find_element(By.XPATH, self.XPATH_ON)
            button.click()
            print('ON clicked {}'.format(self.XPATH_ON))

        # * If Random is selected
        elif Option_picked == 'Random':
            # * Wait for the element to be present
            button = WebDriverWait(self.Driver, 0.2).until(
                EC.presence_of_element_located((By.XPATH, self.XPATH_Random)))
            
            #button = self.Driver.find_element(By.XPATH, self.XPATH_Random)
            button.click()
            print('Random clicked {}'.format(self.XPATH_Random))

        # * If OFF is selected
        elif Option_picked == 'OFF':
            # * Wait for the element to be present
            button = WebDriverWait(self.Driver, 0.2).until(
                EC.presence_of_element_located((By.XPATH, self.XPATH_OFF)))
            
           # button = self.Driver.find_element(By.XPATH, self.XPATH_OFF)
            button.click()
            print('OFF clicked {}'.format(self.XPATH_OFF))

        else:   
            pass