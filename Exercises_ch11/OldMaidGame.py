from Exercises_ch11.Card import Card
from Exercises_ch11.CardGame import CardGame
from Exercises_ch11.OldMaidHand import OldMaidHand


class OldMaidGame(CardGame):

    def play(self, names):
        # remove Queen of Clubs
        self.deck.remove(Card(0, 12))

        # make a hand for each player
        self.hands = []
        for name in names:
            self.hands.append(OldMaidHand(name))

        # deal the cards
        self.deck.deal(self.hands)
        print("---------- Cards have been dealt")

        # remove initial matches
        matches = self.remove_all_matches()
        print("---------- Matches discarded, play begins")
        self.print_hands()

        # play until all 50 cards are matched
        turn = 0
        num_hands = len(self.hands)
        while matches < 25:
            matches += self.play_one_turn(turn)
            turn = (turn + 1) % num_hands

        print("---------- Game is Over")
        self.print_hands()

    def remove_all_matches(self):
        count = 0
        for hand in self.hands:
            count += hand.remove_matches()
        return count

    def play_one_turn(self, i):
        if self.hands[i].is_empty():
            return 0
        neighbour = self.find_neighbour(i)
        picked_card = self.hands[neighbour].pop()
        self.hands[i].add(picked_card)
        print("Hand", self.hands[i].name, "picked", picked_card)
        count = self.hands[i].remove_matches()
        self.hands[i].shuffle()
        return count

    def find_neighbour(self, i):
        num_hands = len(self.hands)
        for next in range (1, num_hands):
            neighbour = (i + next) % num_hands
            if not self.hands[neighbour].is_empty():
                return neighbour

    def print_hands(self):
        for hand in self.hands:
            print(hand)

