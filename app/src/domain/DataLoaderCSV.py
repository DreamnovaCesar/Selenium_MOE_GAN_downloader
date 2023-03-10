
import pandas as pd

class DataLoaderCSV(object):
    """
    A class for loading data from a CSV file.

    Parameters
    ----------
    CSV_file : str
        The path to the CSV file.

    Attributes
    ----------
    Data : pandas.DataFrame
        The data loaded from the CSV file.
    Attributes : list
        A list containing the attributes of the data.
    Model : list
        A list containing the 'Model' attribute of the data.
    Hair_color : list
        A list containing the 'Hair_color' attribute of the data.
    Hair_style : list
        A list containing the 'Hair_style' attribute of the data.
    Eye_color : list
        A list containing the 'Eye_color' attribute of the data.
    Dark_sin : list
        A list containing the 'Dark_sin' attribute of the data.
    Blush : list
        A list containing the 'Blush' attribute of the data.
    Smile : list
        A list containing the 'Smile' attribute of the data.
    Open_mouth : list
        A list containing the 'Open_mouth' attribute of the data.
    Hat : list
        A list containing the 'Hat' attribute of the data.
    Ribbon : list
        A list containing the 'Ribbon' attribute of the data.
    Glasses : list
        A list containing the 'Glasses' attribute of the data.
    Epochs : list
        A list containing the 'Epochs' attribute of the data.

    Methods
    -------
    None

    Examples
    --------
    >>> loader = DataLoaderCSV('data.csv')
    >>> print(loader.Model)
    ['model1', 'model2', 'model3', ...]
    >>> print(loader.Hair_color)
    ['black', 'blonde', 'red', ...]
    """

    def __init__(self, CSV_file):
        # * Load data from CSV file using pandas
        with open(CSV_file, 'r', encoding='utf_8_sig') as CSV:
            self.Data = pd.read_csv(CSV);

        # * Initialize attributes as empty lists
        self.Attributes = [];

        # * Extract attributes from the data
        self.Model = self.Data['Model'].tolist();
        self.Hair_color = self.Data['Hair_color'].tolist();
        self.Hair_style = self.Data['Hair_style'].tolist();
        self.Eye_color = self.Data['Eye_color'].tolist();
        self.Dark_sin = self.Data['Dark_sin'].tolist();
        self.Blush = self.Data['Blush'].tolist();
        self.Smile = self.Data['Smile'].tolist();
        self.Open_mouth = self.Data['Open_mouth'].tolist();
        self.Hat = self.Data['Hat'].tolist();
        self.Ribbon = self.Data['Ribbon'].tolist();
        self.Glasses = self.Data['Glasses'].tolist();
        self.Epochs = self.Data['Epochs'].tolist();

        # * Add attributes to the Attributes list
        self.Attributes.append(self.Model);
        self.Attributes.append(self.Hair_color);
        self.Attributes.append(self.Hair_style);
        self.Attributes.append(self.Eye_color);
        self.Attributes.append(self.Dark_sin);
        self.Attributes.append(self.Blush);
        self.Attributes.append(self.Smile);
        self.Attributes.append(self.Open_mouth);
        self.Attributes.append(self.Hat);
        self.Attributes.append(self.Ribbon);
        self.Attributes.append(self.Glasses);
        self.Attributes.append(self.Epochs);



 
