from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Dropdown(object):
    """
    Class representing a dropdown menu in a web page.

    Attributes:
    -----------
    Driver: webdriver.Chrome
        An instance of the Chrome web driver.
    XPATH: str
        XPath of the dropdown button on the web page.
    XPATH_list: str
        XPath of the dropdown options list on the web page.

    Methods:
    --------
    select_option(Option_picked: str) -> None:
        Select the given option from the dropdown list.

    """

    def __init__(self, 
                 Driver: webdriver.Chrome, 
                 XPATH : str, 
                 XPATH_list: str) -> None:
        """
        Initialize the DropdownModel object.

        Returns:
        --------
        None
        """

        self.Driver = Driver;
        self.XPATH = XPATH;
        self.XPATH_list = XPATH_list;
    
    def select_option(self, Option_picked: str) -> None:
        """
        Select the given option from the dropdown list.

        Parameters:
        -----------
        Option_picked: str
            The option to be selected.

        Returns:
        --------
        None
        """

        # * List of options
        Options_list = [];
        
        # * Waits until the dropdown button is present on the page
        Button = WebDriverWait(self.Driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.XPATH)));
        
        '''button = self.driver.find_element(By.XPATH, self.XPATH)'''
        Button.click();

        # * Find the dropdown options list
        Dropdown = WebDriverWait(self.Driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.XPATH_list)));
        
        Dropdown = self.Driver.find_elements(By.XPATH, self.XPATH_list);
        
        # * Find the span elements inside each option and add them to the list of options
        for i, _ in enumerate(Dropdown):
            Options = Dropdown[i].find_elements(By.TAG_NAME, 'span');
        
        # * Find the index of the selected option in the list of options
        for _, Option in enumerate(Options):
            Options_list.append(Option.text);
        
        print('--------- {}'.format(Options_list));

        # * Find the index of the selected option in the list of options
        Option_index = Options_list.index(Option_picked);
        
        print('/// {}'.format(Option_picked));

        # * Click the selected option
        Options[Option_index].click();
        