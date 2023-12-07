

class Card:
    def __init__(self, card):
        SCORE = {'A': 14, 'K': 13, 'Q': 12, 'J': 11, 'T': 10, '9': 9, '8': 8, '7': 7, '6': 6, '5': 5, '4':4, '3':3, '2':2}
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
    def __init__(self, line):
        self.line = line
        self.cards_string = line.split(' ')[0]
        self.bid = int(line.split(' ')[1])
        self.cards = {}
        self.ordered_cards = []
        for card in self.cards_string:
            self.ordered_cards.append(Card(card))
            self.cards[Card(card)] = self.cards.get(Card(card), 0) + 1
        self.score=0
        self.type = ''

        self.analyseHand()

    def analyseHand(self):
        if(len(self.cards.keys())==1):
            self.type = 'Five of a kind'
            self.score = 10
        elif(len(self.cards.keys())==2):
            if(4 in self.cards.values()):
                self.type = 'Four of a kind'
                self.score = 9
            else:
                self.type = 'Full house'
                self.score = 8
        elif(len(self.cards.keys())==3):
            if(3 in self.cards.values()):
                self.type = 'Three of a kind'
                self.score = 7
            else:
                self.type = 'Two pair'
                self.score = 6
        elif(len(self.cards.keys())==4):
            self.type = 'One pair'
            self.score = 5
        else:
            self.type = 'High card'
            self.score = 4

        for card in self.ordered_cards:
            self.score = (self.score*100) + card.getScore()
    def __eq__(self, other: object) -> bool:
        return self.score == other.score
    def __lt__(self, other: object) -> bool:
        return self.score < other.score
    def __str__(self) -> str:
        return f"{self.cards_string} - {self.type} {self.score} {self.bid}"
    def __repr__(self) -> str:
        return self.__str__()

if __name__ == '__main__':
    chal1 = 0
    chal2 = 0
    hands = []
    with open('day7.input.test', 'r') as f:
        for line in f.readlines():
            hands.append(Hand(line.strip()))
            print (hands[-1])
        hands.sort()
        for rank in range(len(hands)):
            chal1 += int(hands[rank].bid * (rank+1))




    print(f"Challenge 1: {chal1}")
    print(f"Challenge 2: {chal2}")
