from ..src.domain.DataLoaderCSV import DataLoaderCSV
from ..src.domain.DownloadGirlsCSV import WaifusDownloadCSV

Reader_CSV = DataLoaderCSV('app\src\data\Waifus_data_csv.csv')

W = WaifusDownloadCSV(Reader_CSV, 
                  'app\src\data\Waifus_data_csv.csv', 
                  'app\src\data')

W.Images_waifus_settings()