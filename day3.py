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
        """
        467..114..
        ...*......
        ..35..633.
        ......#...
        617*......
        .....+.58.
        ..592.....
        ......755.
        ...$.*....
        .664.598..
        """
        self.gears = []
        self.next_to_symbol = []
        self.next_to_number = []
        self.adjacent_numbers = []
        self.products = []
        self.analyse()


    def get_next_to_number(self, linha, coluna):
        if self.bidimensional_array[linha][coluna] != '*':
            return False
        try:
            if self.bidimensional_array[linha-1][coluna-1].isdigit():
                return True
        except:
            pass
        try:
            if self.bidimensional_array[linha-1][coluna].isdigit():
                return True
        except:
            pass
        try:
            if self.bidimensional_array[linha-1][coluna+1].isdigit():
                return True
        except:
            pass
        try:
            if self.bidimensional_array[linha][coluna-1].isdigit():
                return True
        except:
            pass
        try:
            if self.bidimensional_array[linha][coluna+1].isdigit():
                return True
        except:
            pass
        try:
            if self.bidimensional_array[linha+1][coluna-1].isdigit():
                return True
        except:
            pass
        try:
            if self.bidimensional_array[linha+1][coluna].isdigit():
                return True
        except:
            pass
        try:
            if self.bidimensional_array[linha+1][coluna+1].isdigit():
                return True
        except:
            pass
        return False

    def is_symbol(self, char):
        if self.gear:
            return char == '*'
        return not char.isdigit() and char != '.'

    def get_next_to_symbol(self, linha, coluna):
        try:
            if self.is_symbol(self.bidimensional_array[linha-1][coluna-1]):
                return True
        except:
            pass
        try:
            if self.is_symbol(self.bidimensional_array[linha-1][coluna]):
                return True
        except:
            pass
        try:
            if self.is_symbol(self.bidimensional_array[linha-1][coluna+1]):
                return True
        except:
            pass
        try:
            if self.is_symbol(self.bidimensional_array[linha][coluna-1]):
                return True
        except:
            pass
        try:
            if self.is_symbol(self.bidimensional_array[linha][coluna+1]):
                return True
        except:
            pass
        try:
            if self.is_symbol(self.bidimensional_array[linha+1][coluna-1]):
                return True
        except:
            pass
        try:
            if self.is_symbol(self.bidimensional_array[linha+1][coluna]):
                return True
        except:
            pass
        try:
            if self.is_symbol(self.bidimensional_array[linha+1][coluna+1]):
                return True
        except:
            pass
        return False

    def analyse(self):
        for linha in range(len(self.bidimensional_array)):
            self.next_to_symbol.append([])
            self.next_to_number.append([])
            for coluna in range(len(self.bidimensional_array[linha])):
                self.next_to_number[-1].append(self.get_next_to_number(linha, coluna))
                self.next_to_symbol[-1].append(self.get_next_to_symbol(linha, coluna))

    def return_adjacent_numbers(self):
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
        if len(res) == 2:
            return res
        return None

    def find_gears(self):
        for linha in range(len(self.bidimensional_array)):
            for coluna in range(len(self.bidimensional_array[linha])):
                if self.next_to_number[linha][coluna]:
                    numbers = self.get_numbers_arround(linha, coluna)
                    if numbers is not None:
                        self.gears.append(numbers)


if __name__ == '__main__':
    chal1 = 0
    chal2 = 0
    data = []
    with open('day3.input', 'r') as f:
        for line in f.readlines():
            data.append(line.strip())

    a = Matrix(data, True)
    print(a.next_to_number)

    a.return_adjacent_numbers()
    a.find_gears()
    for i in a.gears:
        chal2 += i[0]*i[1]
    print(a.gears)

    print(f"Challenge 1: {sum(a.adjacent_numbers)}")
    print(f"Challenge 2: {chal2}")
