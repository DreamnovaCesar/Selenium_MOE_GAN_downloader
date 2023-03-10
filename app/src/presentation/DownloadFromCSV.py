from .MenuOption import MenuOption
from ..domain.DataLoaderCSV import DataLoaderCSV
from ..application.DownloadGirlsCSV import DownloadGirlsCSV
from ...src.Utilities import Settings

class DownloadFromCSV(MenuOption):
    def __init__(self, 
                 Downloader : DownloadGirlsCSV,
                 CSV_reader : DataLoaderCSV):
        
        self.Downloader = Downloader;
        self.CSV_reader = CSV_reader;

    def execute(self):
        CSV_path = input('Add CSV file: ');
        CSV_reader = self.CSV_reader(CSV_path);
        Downloader = self.Downloader(Settings._RELATIVE_PATH_DATA_, CSV_path , CSV_reader);
        Downloader.Download_images();
