from pandas import *
from random import randint

CSV_File = "Resources/data/language.csv"

class FlashCardData:
    def __init__(self):
        self.flashCard_data_dict = {}
        self.known_cards = []
        self.current_english_word = ""
        self.current_french_word = ""

    def load_data(self):
        raw_data = read_csv(CSV_File)
        self.flashCard_data_dict = raw_data.to_dict()


    def AcquireNewFlashCardData(self):
        unknown_card = False
        data_str = ""
        number = 0


        while unknown_card == False:

            number = randint(0, 100)

            print(self.known_cards.count(number))
            if self.known_cards.count(number)== 0:
                unknown_card = True

        try:
            print(number)
            self.current_french_word= self.flashCard_data_dict["French"][number]
            self.current_english_word= self.flashCard_data_dict["English"][number]



            return data_str
        except:
            print(f"Oh no!!!")


