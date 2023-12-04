# Description: Advent of Code - Day 4

class Card:
    def __init__(self, line):
        self.line = line
        tmp = line.strip().split(':')
        self.id = int(tmp[0][5::])
        winning = tmp[1].split('|')[0].split(' ')
        current = tmp[1].split('|')[1].split(' ')
        self.winning = []
        for k in range(len(winning)):
            if winning[k] != '':
                self.winning.append(winning[k])
        self.current = []
        for k in range(len(current)):
            if current[k] != '':
                self.current.append(current[k])

    def get_matches(self):
        winning_numbers = 0
        for i in self.current:
            if i in self.winning:
                winning_numbers += 1
        return winning_numbers

    def get_points(self):
        winning_numbers = self.get_matches()
        if(winning_numbers == 0):
            return 0
        else:
            return 2**(winning_numbers-1)


if __name__ == '__main__':
    chal1 = 0
    chal2 = 0
    cards = {}
    max_card = 0
    with open('day4.input', 'r') as f:
        for line in f.readlines():
            card = Card(line)
            chal1 += card.get_points()
            matches = card.get_matches()
            max_card = max(max_card, card.id)
            if card.id in cards:
                cards[card.id] += 1
            else:
                cards[card.id] = 1
            for k in range(card.id+1, card.id+matches+1):
                if k in cards:
                    cards[k] += cards[card.id]
                else:
                    cards[k] = cards[card.id]

    for k in cards:
        if k <= max_card:
            chal2 += cards[k]

    print(f"Challenge 1: {chal1}")
    print(f"Challenge 2: {chal2}")
