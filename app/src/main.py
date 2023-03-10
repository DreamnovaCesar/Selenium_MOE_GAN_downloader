__author__ = "Cesar Eduardo Munoz Chavez"
__license__ = "Feel free to copy"

# ? Import necessary modules
from ..src.domain.DataLoaderCSV import DataLoaderCSV
from ..src.domain.Json.JsonFileHander import JsonFileHandler
from .application.DownloadGirlsCSV import DownloadGirlsCSV
from .application.DownloadGirlsJSON import DownloadGirlsJSON
from .application.DownloadGirlsRandom import DownloadGirlsRandom

from ..src.presentation.DownloadFromCSV import DownloadFromCSV
from ..src.presentation.DownloadFromJSON import DownloadFromJSON
from ..src.presentation.DownloadRandomly import DownloadRandomly

from ..src.presentation.Menu import Menu

# ? Define the options for the menu
options = {

    "Download using CSV file" : DownloadFromCSV(DownloadGirlsCSV, DataLoaderCSV),
    "Download randomly" : DownloadRandomly(DownloadGirlsRandom),
    "Download using JSON file" : DownloadFromJSON(DownloadGirlsJSON, JsonFileHandler),

};

'''options = [
    DownloadFromCSV(DownloadGirlsCSV, DataLoaderCSV),
    DownloadRandomly(DownloadGirlsRandom),
    DownloadFromJSON(DownloadGirlsJSON, JsonFileHandler),
]'''

# ? If the script is being run directly, create and display the menu
if __name__ == "__main__":
    menu = Menu(options);
    menu.display();
