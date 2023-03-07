
import pandas as pd

class DataLoaderCSV(object):

    def __init__(self, CSV_file):
        with open(CSV_file, 'r', encoding='utf_8_sig') as CSV:
            self.Data = pd.read_csv(CSV)

        self.Attributes = []

        self.Model = self.Data['Model'].tolist()
        self.Hair_color = self.Data['Hair_color'].tolist()
        self.Hair_style = self.Data['Hair_style'].tolist()
        self.Eye_color = self.Data['Eye_color'].tolist()
        self.Dark_sin = self.Data['Dark_sin'].tolist()
        self.Blush = self.Data['Blush'].tolist()
        self.Smile = self.Data['Smile'].tolist()
        self.Open_mouth = self.Data['Open_mouth'].tolist()
        self.Hat = self.Data['Hat'].tolist()
        self.Ribbon = self.Data['Ribbon'].tolist()
        self.Glasses = self.Data['Glasses'].tolist()
        self.Epochs = self.Data['Epochs'].tolist()
    
        self.Attributes.append(self.Model)
        self.Attributes.append(self.Hair_color)
        self.Attributes.append(self.Hair_style)
        self.Attributes.append(self.Eye_color)
        self.Attributes.append(self.Dark_sin)
        self.Attributes.append(self.Blush)
        self.Attributes.append(self.Smile)
        self.Attributes.append(self.Open_mouth)
        self.Attributes.append(self.Hat)
        self.Attributes.append(self.Ribbon)
        self.Attributes.append(self.Glasses)
        self.Attributes.append(self.Epochs)



 
