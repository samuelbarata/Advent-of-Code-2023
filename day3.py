# Description: Advent of Code - Day 3

class Position():
    def __init__(self, linha, coluna):
        self.x = coluna
        self.y = linha

    def __eq__(self, __value: object) -> bool:
        return self.x == __value.x and self.y == __value.y

    def __hash__(self) -> int:
        return hash((self.x, self.y))

    def __str__(self) -> str:
        return f"({self.x}, {self.y})"

    def __repr__(self) -> str:
        return f"({self.x}, {self.y})"

class Matrix():
    def __init__(self, bidimensional_array, gear):
        self.gear = gear
        self.bidimensional_array = bidimensional_array
        self.gears = []
        self.next_to_symbol = []
        self.adjacent_numbers = []
        self.products = []
        self.gear_ratios = 0
        self.analyse()
        self.calculate_adjacent_numbers()
        if self.gear:
            self.find_gears()
            self.calculate_gear_ratios()


    def is_symbol(self, char):
        if self.gear:
            return char == '*'
        return not char.isdigit() and char != '.'

    def get_next_to_symbol(self, linha, coluna):
        for li in range(linha-1, linha+2):
            tmp = 0
            for co in range(coluna-1, coluna+2):
                if tmp > 0:
                    tmp -= 1
                    continue
                if li >= len(self.bidimensional_array) or co >= len(self.bidimensional_array[li]):
                    continue
                if li == linha and co == coluna:
                    continue
                if self.is_symbol(self.bidimensional_array[li][co]):
                    return True
        return False

    def analyse(self):
        for linha in range(len(self.bidimensional_array)):
            self.next_to_symbol.append([])
            for coluna in range(len(self.bidimensional_array[linha])):
                self.next_to_symbol[-1].append(self.get_next_to_symbol(linha, coluna))

    def calculate_adjacent_numbers(self):
        tmp = 0
        for linha in range(len(self.bidimensional_array)):
            for coluna in range(len(self.bidimensional_array[linha])):
                if tmp > 0:
                    tmp -= 1
                    continue
                if self.bidimensional_array[linha][coluna].isdigit():
                    while coluna+tmp < len(self.bidimensional_array[linha]) and self.bidimensional_array[linha][coluna+tmp].isdigit():
                        tmp += 1

                    number = int(self.bidimensional_array[linha][coluna:coluna+tmp])
                    for k in range(tmp):
                        if self.next_to_symbol[linha][coluna+k]:
                            self.adjacent_numbers.append(number)
                            break

    def get_full_number(self, linha, coluna):
        esquerda = 0
        direita = 0
        while coluna+esquerda >=0 and self.bidimensional_array[linha][coluna+esquerda].isdigit():
            esquerda -= 1
        while coluna+direita < len(self.bidimensional_array[linha]) and self.bidimensional_array[linha][coluna+direita].isdigit():
            direita += 1
        esquerda += 1
        return int(self.bidimensional_array[linha][coluna+esquerda:coluna+direita])

    def get_numbers_arround(self, linha, coluna):
        """
            Has a position on a board, will check the cells arround it for numbers
        """
        res=[]
        for li in range(linha-1, linha+2):
            tmp = 0
            for co in range(coluna-1, coluna+2):
                if tmp > 0:
                    tmp -= 1
                    continue
                if li >= len(self.bidimensional_array) or co >= len(self.bidimensional_array[li]):
                    continue
                if li == linha and co == coluna:
                    continue
                if self.bidimensional_array[li][co].isdigit():
                    res.append(self.get_full_number(li, co))
                    while co+tmp < len(self.bidimensional_array[li]) and self.bidimensional_array[li][co+tmp].isdigit():
                        tmp += 1
        return res

    def find_gears(self):
        for linha in range(len(self.bidimensional_array)):
            for coluna in range(len(self.bidimensional_array[linha])):
                if self.bidimensional_array[linha][coluna] == '*':
                    numbers = self.get_numbers_arround(linha, coluna)
                    if len(numbers) == 2:
                        self.gears.append(numbers)

    def calculate_gear_ratios(self):
        for gear in self.gears:
            self.gear_ratios += gear[0]*gear[1]

if __name__ == '__main__':
    data = []
    with open('day3.input', 'r') as f:
        for line in f.readlines():
            data.append(line.strip())

    chal1 = Matrix(data,False)
    chal2 = Matrix(data,True)

    print(f"Challenge 1: {sum(chal1.adjacent_numbers)}")
    print(f"Challenge 2: {chal2.gear_ratios}")
