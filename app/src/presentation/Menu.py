
class Menu:
    def __init__(self, Options):
        self.Options = Options

        # * list out keys and values separately
        self._Options_text = list(self.Options.keys())
        self._Options_values = list(self.Options.values())

    def display(self):
        asterisk = 60
        print("\n")
        print("*" * asterisk)
        print('What do you want to do:')
        print("*" * asterisk)
        print('\n')

        for i, option in enumerate(self._Options_text):
            print(f'{i + 1}: {option}')

        print('\n')
        print("*" * asterisk)

        while True:
            print('\n')
            choice = input('Option: ')

            try:
                choice = int(choice)
            except ValueError:
                continue

            if choice < 1 or choice > len(self._Options_values):
                continue

            self._Options_values[choice - 1].execute()