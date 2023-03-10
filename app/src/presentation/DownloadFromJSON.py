from .MenuOption import MenuOption
from ..domain.Json.JsonFileHander import JsonFileHandler
from ..application.DownloadGirlsJSON import DownloadGirlsJSON
from ...src.Utilities import Settings

class DownloadFromJSON(MenuOption):
    def __init__(self, 
                 Downloader : DownloadGirlsJSON, 
                 CSV_reader : JsonFileHandler):
        
        self.Downloader = Downloader;
        self.CSV_reader = CSV_reader;

    def execute(self):
        JSON_path = input('Add JSON file: ');
        self.Images = input('Number of images: ');
        JSON_reader = self.CSV_reader.read_json_file(JSON_path);
        Downloader = self.Downloader(Settings._RELATIVE_PATH_DATA_, JSON_reader, self.Images);
        Downloader.Download_images();