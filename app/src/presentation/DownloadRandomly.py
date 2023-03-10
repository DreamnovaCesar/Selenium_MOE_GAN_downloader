from .MenuOption import MenuOption
from ..application.DownloadGirlsRandom import DownloadGirlsRandom
from ...src.Utilities import Settings

class DownloadRandomly(MenuOption):
    def __init__(self, 
                 Downloader : DownloadGirlsRandom):

        self.Downloader = Downloader

    def execute(self):
        self.Folders = input('Number of folders: ');
        self.Images = input('Number of images: ');
        Downloader = self.Downloader(Settings._RELATIVE_PATH_DATA_, self.Folders, self.Images);
        Downloader.Download_images();