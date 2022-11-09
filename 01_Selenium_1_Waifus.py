from Selenium_Class_Libraries import *
from Selenium_Class_Utilities import Utilities



def main():
    
    # *
    config = Menu()

    # *
    config.menu()

    # * Waifu CSV with data
    CSV_path = "Waifus_data_csv.csv"

    # * Class instance
    Waifu = MakeGirlMOE(csv = CSV_path)
    
    # * Class instance functions settings
    Waifu.get_images_waifus_settings()

if __name__ == "__main__":
    main()