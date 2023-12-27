class Alphabet:
    def __init__(self, language):
        self.language = language
        self.letters = {'en': 'abcdefghijklmnopqrstuvwxyz', 'ru': 'абвгдежзийклмнопрстуфхцчшщъыьэюя'}
        self.index = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.index += 1
        if self.index == len(self.letters[self.language]):
            self.index = 0
        return self.letters[self.language][self.index]
