from .MenuOption import MenuOption
from ..domain.DataLoaderCSV import DataLoaderCSV
from ..application.DownloadGirlsCSV import DownloadGirlsCSV
from ...src.Utilities import Settings

class DownloadFromCSV(MenuOption):
    """
    A menu option for downloading images from a CSV file.

    Parameters
    ----------
    Downloader : DownloadGirlsCSV
        An instance of the DownloadGirlsCSV class for downloading images.
    CSV_reader : DataLoaderCSV
        An instance of the DataLoaderCSV class for reading data from a CSV file.

    Methods
    -------
    execute()
        Prompts the user for a CSV file path and the number of images to download,
        creates an instance of the DownloadGirlsCSV class with the given parameters,
        and downloads the images.

    """
    def __init__(self, 
                 Downloader : DownloadGirlsCSV,
                 CSV_reader : DataLoaderCSV):
        
        """
        Constructs a new DownloadCSV object.
        """

        self.Downloader = Downloader;
        self.CSV_reader = CSV_reader;

    def execute(self):
        """
        Prompts the user for a CSV file path and the number of images to download,
        creates an instance of the DownloadGirlsCSV class with the given parameters,
        and downloads the images.
        """

        CSV_path = input('Add CSV file: ');
        CSV_reader = self.CSV_reader(CSV_path);
        Downloader = self.Downloader(Settings._RELATIVE_PATH_DATA_, CSV_path , CSV_reader);
        Downloader.Download_images();
