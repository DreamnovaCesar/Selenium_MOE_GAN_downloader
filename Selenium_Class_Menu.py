from Selenium_Class_MakeGirlMOE import MakeGirlMOE
from Selenium_Class_Utilities import Utilities

class Menu(Utilities):

    def __init__(self, **kwargs) -> None:
        
        self.__Images = r'Images';

    def __repr__(self):

        kwargs_info = '';

        return kwargs_info

    def __str__(self):
        pass
    
    @staticmethod
    def add_csv(Folder_2D_):

        while(True):

            CSV_path_ = input('Add CSV path: ');
            print('\n')

            print('This is the CSV path: {}'.format(CSV_path_));
            print('\n')

            Proceed = input('Do you want to proceed?: [y/n]: ');

            if(Proceed == 'y'):

                break;

            else:

                pass;

        Get_images = MakeGirlMOE(csv = CSV_path_);
        Get_images.get_images_waifus_settings()

    @Utilities.time_func  
    def menu(self):

        while(True):
            
            Asterisk = 60;

            print("\n");

            print("*" * Asterisk);
            print('What do you want to do: ');
            print("*" * Asterisk);
            print('\n');
            print('1: Get images from MAKEGIRL using CSV file');

            print('\n');
            print("*" * Asterisk);

            Options = input('Option: ');

            if(Options == '1'):
                self.add_csv(self.__Images)

            elif(Options == 'c'):

                break;

        return -1