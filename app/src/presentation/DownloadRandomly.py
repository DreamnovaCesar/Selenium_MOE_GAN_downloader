from .MenuOption import MenuOption
from ..application.DownloadGirlsRandom import DownloadGirlsRandom
from ...src.Utilities import Settings

class DownloadRandomly(MenuOption):
    """
    A MenuOption class that allows the user to download random images of girls.

    Attributes:
    -----------
    Downloader : DownloadGirlsRandom
        The downloader object used to download the images.
    
    Methods
    -------
    execute()
        Prompts the user to input a path to a number of folders and the Nnumber of images to download. 
    """

    def __init__(self, 
                 Downloader : DownloadGirlsRandom):

        """
        Constructs a new DownloadRandomly object.
        """
        
        self.Downloader = Downloader;

    def execute(self):
        """
        Executes the DownloadRandomly option by prompting the user for the number of folders and images to download,
        and then downloading the random images using the downloader object.
        """
        
        self.Folders = input('Number of folders: ');
        self.Images = input('Number of images: ');
        Downloader = self.Downloader(Settings._RELATIVE_PATH_DATA_, self.Folders, self.Images);
        Downloader.Download_images();