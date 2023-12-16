# Description: Advent of Code - Day 11


class Universe:
    def __init__(self):
        self.lines = []
        self.galaxies = []
        self.chal1 = 0

    def add(self, line):
        self.lines.append(line)

    def finish(self):
        new_lines = []
        for line in self.lines:
            new_lines.append(line)
            if '#' not in line:
                new_lines.append('.' * len(line))
        self.lines = new_lines
        new_lines = ['' for _ in self.lines]
        for i in range(len(self.lines[0])): # Iterate over columns
            galaxies = True
            if '#' not in [k[i] for k in self.lines]:
                galaxies = False
            for j in range(len(self.lines)):
                new_lines[j] += self.lines[j][i]
                if not galaxies:
                    new_lines[j] += '.'

        self.lines = new_lines
        self.create_galaxies()

    def finish(self):
        new_lines = []
        for line in self.lines:
            new_lines.append(line)
            if '#' not in line:
                new_lines.append('.' * len(line))
        self.lines = new_lines
        new_lines = ['' for _ in self.lines]
        for i in range(len(self.lines[0])): # Iterate over columns
            galaxies = True
            if '#' not in [k[i] for k in self.lines]:
                galaxies = False
            for j in range(len(self.lines)):
                new_lines[j] += self.lines[j][i]
                if not galaxies:
                    new_lines[j] += '.'

        self.lines = new_lines
        self.create_galaxies()

    def create_galaxies(self):
        for y, line in enumerate(self.lines):
            for x, char in enumerate(line):
                if char == '#':
                    self.galaxies.append(Galaxy(x, y))

    def challenge1(self):
        for galaxy in self.galaxies:
            for other in self.galaxies:
                if galaxy == other:
                    continue
                self.chal1 += galaxy.distance(other)



class Galaxy:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def distance(self, other):
        return abs(self.x - other.x) + abs(self.y - other.y)

if __name__ == '__main__':
    chal1 = 0
    chal2 = 0
    u = Universe()
    with open('day11.input', 'r') as f:
        for line in f.readlines():
            u.add(line.strip())
    u.finish()
    u.challenge1()



    print(f"Challenge 1: {int(u.chal1/2)}")
    print(f"Challenge 2: {chal2}")
