from abc import ABC
from abc import abstractmethod

from ..domain.Decorators.Timer import Timer
from ..domain.Decorators.Singleton import Singleton

#@Singleton.singleton
class DownloadGirlsMOE(ABC):
    """
    An abstract class for downloading images from GirlsMOE website.

    Attributes
    ----------
    None

    Methods
    -------
    Download_images(self) -> None:
        Abstract method to download images from GirlsMOE website.
        This method must be implemented by the child classes.

    """

    @Timer.timer
    @abstractmethod
    def Download_images(self) -> None:
        """
        Abstract method to download images from GirlsMOE website.

        Parameters
        ----------
        self : object
            An instance of the child class.

        Returns
        -------
        None
        """
        pass
