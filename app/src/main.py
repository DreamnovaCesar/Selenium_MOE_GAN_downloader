from ..src.domain.DataLoaderCSV import DataLoaderCSV
from .domain.DownloadGirlsSettings import DownloadGirlsSettings
from .domain.DownloadGirlsRandom import DownloadGirlsRandom

'''Reader_CSV = DataLoaderCSV('app\src\data\Waifus_data_csv.csv')

W = DownloadGirlsSettings(Reader_CSV, 
                        'app\src\data\Waifus_data_csv.csv', 
                        'app\src\data')'''

W = DownloadGirlsRandom('app\src\data', 15, 30)

W.Download_images()