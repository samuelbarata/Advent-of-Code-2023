AVAILABLE_CUBES = {'red': 12, 'green': 13, 'blue': 14}

class Game:
    def __init__(self, line):
        self.line = line
        self.sets = []
        self.id = int(line.split(':')[0][5::])
        sets = line.split(':')[1].strip().split('; ')
        for u in sets:
            try:
                spli = u.split(', ')
            except:
                spli = [u,]
            tmp = {'red': 0, 'green': 0, 'blue': 0}
            for i in spli:
                vals = i.split(' ')
                tmp[vals[1]] = int(vals[0])
            self.sets.append(tmp)

    def is_possible(self):
        for i in self.sets:
            for color in AVAILABLE_CUBES.keys():
                if i[color] > AVAILABLE_CUBES[color]:
                    return False
        return True

    def get_fewest(self):
        few = {'red': 0, 'green': 0, 'blue': 0}
        for i in self.sets:
            for k in i.keys():
                if i[k] > few[k]:
                    few[k] = i[k]
        return few

    def get_power(self):
        power = 1
        for _, val in self.get_fewest().items():
            power *= val
        return power

    def get_id(self):
        return self.id

if __name__ == '__main__':
    chal1 = 0
    chal2 = 0
    with open('day2.input', 'r') as f:
        for line in f.readlines():
            a = Game(line)
            if a.is_possible():
                chal1 += a.get_id()
            chal2 += a.get_power()

    print(f"Challenge 1: {chal1}")
    print(f"Challenge 2: {chal2}")
