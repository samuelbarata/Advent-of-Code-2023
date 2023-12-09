# Description: Advent of Code - Day 9

class Oasis:
    def __init__(self):
        self.lines = []
        self.chal1 = 0
        self.chal2 = 0

    def add(self, line):
        self.lines.append(Value(line))
        new_values =  self.lines[-1].extrapolate()
        self.chal1 += new_values[1]
        self.chal2 += new_values[0]

class Value:
    def __init__(self, line):
        self.line = line
        self.history = [[int(i) for i in line.split(' ')]]
        self.get_diference()

    def get_diference(self):
        tmp = self.history[-1][0]
        res = []
        for i in self.history[-1][1::]:
            res.append(i - tmp)
            tmp = i
        self.history.append(res)

        if not all(i == 0 for i in self.history[-1]):
            self.get_diference()

    def extrapolate(self):
        last = self.history[-1][-1]
        first = self.history[-1][0]
        del self.history[-1]
        self.history[-1] = [self.history[-1][0]-first] + self.history[-1] + [last+self.history[-1][-1]]
        if len(self.history) != 1:
            return self.extrapolate()
        return (self.history[0][0], self.history[0][-1])

if __name__ == '__main__':
    oasis = Oasis()
    with open('day9.input', 'r') as f:
        for line in f.readlines():
            oasis.add(line)

    print(f"Challenge 1: {oasis.chal1}")
    print(f"Challenge 2: {oasis.chal2}")
