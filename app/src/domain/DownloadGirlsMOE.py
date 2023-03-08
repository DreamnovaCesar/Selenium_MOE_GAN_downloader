from abc import ABC
from abc import abstractmethod

from .Decorators.Timer import Timer
from .Decorators.Singleton import Singleton

# ?
#@Singleton.singleton
class DownloadGirlsMOE(ABC):
    
    @Timer.timer
    @abstractmethod
    def Download_images(self) -> None:
        pass
