"""
Class Guitar create for composition. If i destroy guitar instance,
the guitar strings are also destroyed
"""


class Guitar:
    def __init__(self):
        print('Guitar created')

    @staticmethod
    def guitar_music():
        print('Play song')


class StringGuitar:
    def __init__(self, number_of_stings):
        self.number_of_strings = number_of_stings
        self.obj = Guitar()

    def get_number_of_strings(self):
        print(f'This guitar have {self.number_of_strings} strings')

    def get_music_of_guitar(self):
        self.obj.guitar_music()


if __name__ == '__main__':
    strings = StringGuitar(3)
    strings.get_number_of_strings()
    strings.get_music_of_guitar()
