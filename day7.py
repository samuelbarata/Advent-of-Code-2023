# Description: Advent of Code - Day 7

class Card:
    def __init__(self, card, joker=False):
        SCORE = {'A': 14, 'K': 13, 'Q': 12, 'J': 11, 'T': 10, '9': 9, '8': 8, '7': 7, '6': 6, '5': 5, '4':4, '3':3, '2':2}
        if joker:
            SCORE['J'] = 1
        self.card = card
        self.score = SCORE[card]
    def __eq__(self, other: object) -> bool:
        return self.score == other.score
    def __lt__(self, other: object) -> bool:
        return self.score < other.score
    def __hash__(self) -> int:
        return self.score
    def __str__(self) -> str:
        return self.card
    def __repr__(self) -> str:
        return self.__str__()
    def getScore(self):
        return self.score

class Hand:
    def __init__(self, line, jokers=False):
        self.jokers = jokers
        self.line = line
        self.cards_string = line.split(' ')[0]
        self.bid = int(line.split(' ')[1])
        self.cards = {}
        self.cards_mod = {}
        self.ordered_cards = []
        for card in self.cards_string:
            self.ordered_cards.append(Card(card, self.jokers))
            self.cards[Card(card, self.jokers)] = self.cards.get(Card(card, self.jokers), 0) + 1
        self.score=0
        self.type = ''

        if self.jokers:
            self.analyseHandWithJokers()
        else:
            self.analyseHand()

    def analyseHand(self):
        if(len(self.cards_mod.keys())==1):
            self.type = 'Five of a kind'
            self.score = 10
        elif(len(self.cards_mod.keys())==2):
            if(4 in self.cards_mod.values()):
                self.type = 'Four of a kind'
                self.score = 9
            else:
                self.type = 'Full house'
                self.score = 8
        elif(len(self.cards_mod.keys())==3):
            if(3 in self.cards_mod.values()):
                self.type = 'Three of a kind'
                self.score = 7
            else:
                self.type = 'Two pair'
                self.score = 6
        elif(len(self.cards_mod.keys())==4):
            self.type = 'One pair'
            self.score = 5
        else:
            self.type = 'High card'
            self.score = 4

        for card in self.ordered_cards:
            self.score = (self.score*100) + card.getScore()
    def analyseHandWithJokers(self):
        if Card('J', self.jokers) not in self.cards.keys() or self.jokers == False:
            self.cards_mod = self.cards
            self.analyseHand()
            return
        if(self.cards[Card('J', self.jokers)] == 5):
            self.cards_mod = {Card('A', self.jokers): 5}
            self.analyseHand()
            return

        # Get the card with the most number of cards
        max_card = None
        number_of_cards = 0
        for card in self.cards:
            if card == Card('J', self.jokers):
                continue
            if self.cards[card] > number_of_cards:
                number_of_cards = self.cards[card]
                max_card = card
            if self.cards[card] == number_of_cards:
                if(card > max_card):
                    max_card = card

        # replace the jokers with that card on the original deck
        self.cards_mod = self.cards.copy()
        self.cards_mod[max_card] += self.cards[Card('J', self.jokers)]
        del(self.cards_mod[Card('J', self.jokers)])

        self.analyseHand()

    def __eq__(self, other: object) -> bool:
        return self.score == other.score
    def __lt__(self, other: object) -> bool:
        return self.score < other.score
    def __str__(self) -> str:
        if self.jokers:
            return f"{self.cards_string} - {self.type} {self.score} {self.bid} JOKERS {self.cards_mod}"
        return f"{self.cards_string} - {self.type} {self.score} {self.bid}"
    def __repr__(self) -> str:
        return self.__str__()

if __name__ == '__main__':
    chal1 = 0
    chal2 = 0
    hands = []
    hands_2 = []
    with open('day7.input', 'r') as f:
        for line in f.readlines():
            hands.append(Hand(line.strip()))
            hands_2.append(Hand(line.strip(), True))

        hands.sort()
        for rank in range(len(hands)):
            chal1 += int(hands[rank].bid * (rank+1))

        hands_2.sort()
        for rank in range(len(hands_2)):
            chal2 += int(hands_2[rank].bid * (rank+1))

    print(f"Challenge 1: {chal1}")
    print(f"Challenge 2: {chal2}")
