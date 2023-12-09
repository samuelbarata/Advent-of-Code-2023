# Description: Advent of Code - Day 9

from typing import Any


class Oasis:
    def __init__(self):
        self.lines = []
        self.chal1 = 0
        self.chal2 = 0

    def add(self, line):
        self.lines.append(Value(line))
        self.chal1 += self.lines[-1].extrapolate()
        self.chal2 += self.lines[-1].extrapolate_back()



class Value:
    def __init__(self, line):
        self.line = line
        self.history = [[int(i) for i in line.split(' ')]]
        self.get_diference()
        self.history_2 = self.history.copy()

    def get_diference(self):
        tmp = self.history[-1][0]
        res = []
        for i in self.history[-1][1::]:
            res.append(i - tmp)
            tmp = i
        self.history.append(res)
        print(res)

        if not all(i == 0 for i in self.history[-1]):
            self.get_diference()

    def extrapolate(self):
        last = self.history[-1][-1]
        del self.history[-1]
        self.history[-1].append(last+self.history[-1][-1])
        if len(self.history) != 1:
            return self.extrapolate()
        return self.history[0][-1]

    def extrapolate_back(self):
        first = self.history_2[-1][0]
        del self.history_2[-1]
        self.history_2[-1] = [self.history_2[-1][0]-first] + self.history_2[-1]
        print(self.history_2[-1])
        if len(self.history_2) != 1:
            return self.extrapolate_back()
        return self.history_2[0][0]

if __name__ == '__main__':
    chal1 = Oasis()
    with open('day9.input', 'r') as f:
        for line in f.readlines():
            chal1.add(line)



    print(f"Challenge 1: {chal1.chal1}")
    print(f"Challenge 2: {chal1.chal2}")
