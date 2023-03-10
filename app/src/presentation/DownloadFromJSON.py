from .MenuOption import MenuOption
from ..domain.Json.JsonFileHander import JsonFileHandler
from ..application.DownloadGirlsJSON import DownloadGirlsJSON
from ...src.Utilities import Settings

class DownloadFromJSON(MenuOption):
    """
    A class representing the menu option to download images from a JSON file.

    Attributes
    ----------
    Downloader : DownloadGirlsJSON
        The object that handles the downloading of the images.
    CSV_reader : JsonFileHandler
        The object that handles the reading of the JSON file.

    Methods
    -------
    execute()
        Prompts the user to input a path to a JSON file and the number of images to download. 
        It then uses the `CSV_reader` object to read the JSON file and pass the resulting data 
        to the `Downloader` object's constructor to initiate the download of the specified number of images.
    """

    def __init__(self, 
                 Downloader : DownloadGirlsJSON, 
                 CSV_reader : JsonFileHandler):
        """
        Constructs a new DownloadJSON object.
        """

        self.Downloader = Downloader;
        self.CSV_reader = CSV_reader;

    def execute(self):
        """
        Prompts the user to input a path to a JSON file and the number of images to download. 
        It then uses the `CSV_reader` object to read the JSON file and pass the resulting data 
        to the `Downloader` object's constructor to initiate the download of the specified number of images.
        """
        
        JSON_path = input('Add JSON file: ');
        self.Images = input('Number of images: ');
        JSON_reader = self.CSV_reader.read_json_file(JSON_path);
        Downloader = self.Downloader(Settings._RELATIVE_PATH_DATA_, JSON_reader, self.Images);
        Downloader.Download_images();