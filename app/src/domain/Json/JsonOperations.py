from abc import ABC
from abc import abstractmethod

class JsonOperations(ABC):
    @abstractmethod
    def create_json_file(self, data: dict, file_path: str) -> None:
        pass

    @abstractmethod
    def read_json_file(self, file_path: str) -> dict:
        pass