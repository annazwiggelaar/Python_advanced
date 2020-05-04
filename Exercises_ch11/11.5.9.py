import cards as cards

from Exercises_ch11.CardGame import CardGame
from Exercises_ch11.Deck import Deck
from Exercises_ch11.Hand import Hand
from Exercises_ch11.OldMaidHand import OldMaidHand

deck = Deck()
deck.shuffle()
hand = Hand("Frank")
deck.deal([hand], 5)
print(hand)

game = CardGame()
hand_2 = OldMaidHand("Molly")
game.deck.deal([hand_2], 13)
print(hand_2)
hand_2.remove_matches()
print(hand_2)

