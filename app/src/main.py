from ..src.domain.DataLoaderCSV import DataLoaderCSV
from ..src.domain.Json.JsonFileHander import JsonFileHandler
from .application.DownloadGirlsCSV import DownloadGirlsCSV
from .application.DownloadGirlsJSON import DownloadGirlsJSON
from .application.DownloadGirlsRandom import DownloadGirlsRandom

from ..src.presentation.DownloadFromCSV import DownloadFromCSV
from ..src.presentation.DownloadFromJSON import DownloadFromJSON
from ..src.presentation.DownloadRandomly import DownloadRandomly

from ..src.presentation.Menu import Menu

options = {

    "Download using CSV file" : DownloadFromCSV(DownloadGirlsCSV, DataLoaderCSV),
    "Download randomly" : DownloadRandomly(DownloadGirlsRandom),
    "Download using JSON file" : DownloadFromJSON(DownloadGirlsJSON, JsonFileHandler),

}

'''options = [
    DownloadFromCSV(DownloadGirlsCSV, DataLoaderCSV),
    DownloadRandomly(DownloadGirlsRandom),
    DownloadFromJSON(DownloadGirlsJSON, JsonFileHandler),
]'''

if __name__ == "__main__":
    menu = Menu(options)
    menu.display()

'''Reader_CSV = DataLoaderCSV('app\src\data\Waifus_data_csv.csv')

W = DownloadGirlsSettings('app\src\data',Reader_CSV, 'app\src\data\Waifus_data_csv.csv'
)

W = DownloadGirlsRandom('app\src\data', 10, 10)

W.Download_images()'''