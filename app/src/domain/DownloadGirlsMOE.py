from abc import ABC
from abc import abstractmethod

from .Decorators.Timer import Timer
from .Decorators.Singleton import Singleton

# ?
#@Singleton.singleton
class DownloadGirlsMOE(ABC):
    
    # ?
    @Timer.timer
    @abstractmethod
    def Images_waifus_random(self) -> None:
        pass

    @Timer.timer
    @abstractmethod
    def Images_waifus_settings(self) -> None:
        pass