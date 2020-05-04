from Exercises_ch11.Deck import Deck


class CardGame:

    def __init__(self):
        self.deck = Deck()
        self.deck.shuffle()

