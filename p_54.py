from collections import Counter
from itertools import izip

''' How many hands does Player 1 win? '''

class PokerHand:

    def __init__(self, cards):
        self.sort = {
            '2': 1, '3': 2, '4': 3, '5': 4,
            '6': 5, '7': 6, '8': 7, '9': 8,
            'T': 9, 'J': 10, 'Q': 11, 'K': 12,
            'A': 13
        }
        suits = {card[1] for card in cards}
        self.flush = len(suits) == 1

        self.cards = sorted((card[0] for card in cards), key=lambda x: self.sort[x[0]])

        card_counts = Counter(self.cards)
        self.four = [self.sort[x] for x, y in card_counts.iteritems() if y == 4]
        if self.four:
            self.four = self.four[0]
        self.triple = [self.sort[x] for x, y in card_counts.iteritems() if y == 3]
        if self.triple:
            self.triple = self.triple[0]
        self.pairs = sorted((self.sort[x] for x, y in card_counts.iteritems() if y == 2), reverse=True)
        self.singles = sorted((self.sort[x] for x, y in card_counts.iteritems() if y == 1), reverse=True)
        self.full_house = self.triple and self.pairs

        self.straight = True
        prev_card = self.cards[0]
        for card in self.cards[1:]:
            if (self.sort[prev_card] + 1) % 13 != self.sort[card] % 13:
                self.straight = False
                break
            prev_card = card

        if self.flush and self.straight:
            if self.cards[0] == 'T':
                self.score = 10
            else:
                self.score = 9
        elif self.four:
            self.score = 8
        elif self.full_house:
            self.score = 7
        elif self.flush:
            self.score = 6
        elif self.straight:
            self.score = 5
        elif self.triple:
            self.score = 4
        elif self.pairs:
            if len(self.pairs) == 2:
                self.score = 3
            else:
                self.score = 2
        else:
            self.score = 1

    def win(self, other_hand):
        if self.score != other_hand.score:
            return 1 if self.score > other_hand.score else 0
        
        if self.score == 10:
            return 0
        if self.score == 9:
            return 1 if self.cards[-1] > other_hand.cards[-1] else 0
        if self.score == 8:
            if self.four > other_hand.four:
                return 1
            elif self.four < other_hand.four:
                return 0
            self.score = 1
        if self.score == 7:
            if self.triple > other_hand.triple:
                return 1
            elif self.triple < other_hand.triple:
                return 0
            self.score = 2
        if self.score == 6 or self.score == 5:
            for card1, card2 in izip(reversed(self.cards), reversed(other_hand.cards)):
                if self.sort[card1] > self.sort[card2]:
                    return 1
                elif self.sort[card1] < self.sort[card2]:
                    return 0
            return 0
        if self.score == 4:
            if self.triple > other_hand.triple:
                return 1
            elif self.triple < other_hand.triple:
                return 0
            self.score = 1
        if self.score == 3 or self.score == 2:
            if self.pairs[0] > other_hand.pairs[0]:
                return 1
            if self.pairs[0] < other_hand.pairs[0]:
                return 0
        for card1, card2 in izip(self.singles, other_hand.singles):
            if card1 > card2:
                return 1
            elif card1 < card2:
                return 0
        return 0


player_1 = []
player_2 = []
with open("p054_poker.txt") as hands:
    for line in hands:
        cards = line.split()
        player_1.append(PokerHand(cards[:5]))
        player_2.append(PokerHand(cards[5:]))

print sum(hand1.win(hand2) for hand1, hand2 in izip(player_1, player_2))
