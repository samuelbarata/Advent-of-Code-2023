# Description: Advent of Code - Day 10
from shapely.geometry import Point, Polygon

class Map:
    def __init__(self):
        self.nodes = {}
        self.dimensions = [0, 0]
        self.start = None
        self.paths = []

    def add(self, y:int, line: str):
        self.dimensions[1] = max(self.dimensions[1], y)
        for x, char in enumerate(line):
            self.nodes[(x, y)] = Node(x, y, char)
            self.dimensions[0] = max(self.dimensions[0], x)

    def find_path(self):
        for node in self.nodes.values():
            if node.visited:
                self.start = node
                break

        for path in self.start.next:
            if 0 <= path[0] < self.dimensions[0] and 0 <= path[1] < self.dimensions[1]:
                self.paths.append([self.start, self.nodes[path]])

        finished = 0
        while finished != len(self.paths):
            finished = 0
            for path in self.paths:
                if path[-1].visited:
                    finished += 1
                    continue
                next_coord = path[-1].visit(path[-2])
                if len(next_coord) == 0:
                    finished += 1
                    continue
                path.append(self.nodes[next_coord[0]])
        self.paths = [k[1:-1:] for k in self.paths if len(k) > 2]
        return max(self.paths, key=len)

    def find_inner_tiles(self):
        big_path = [self.start] + self.paths[0] + self.paths[1][::-1] + [self.start]
        polygon = Polygon([(k.x, k.y) for k in big_path])
        inner_tiles = 0
        for i in self.nodes.values():
            if i in big_path:
                continue
            if Point(i.x, i.y).within(polygon):
                inner_tiles += 1
        return inner_tiles

    def __str__(self) -> str:
        return '\n'.join([''.join([self.nodes[(x, y)].char for x in range(self.dimensions[0] + 1)]) for y in range(self.dimensions[1] + 1)])


class Node:
    def __init__(self, x, y, char):
        self.x = x
        self.y = y
        self.visited = False
        self.char = char
        self.next = None

        if char == '-':
            self.next = ((self.x + 1, self.y), (self.x - 1, self.y))
        elif char == '|':
            self.next = ((self.x, self.y + 1), (self.x, self.y - 1))
        elif char == 'L':
            self.next = ((self.x + 1, self.y), (self.x, self.y - 1))
        elif char == 'J':
            self.next = ((self.x - 1, self.y), (self.x, self.y - 1))
        elif char == '7':
            self.next = ((self.x - 1, self.y), (self.x, self.y + 1))
        elif char == 'F':
            self.next = ((self.x + 1, self.y), (self.x, self.y + 1))
        elif char == '.':
            self.next = tuple()
        elif char == 'S':
            self.visited = True
            self.next = ((self.x - 1, self.y), (self.x + 1, self.y), (self.x, self.y - 1), (self.x, self.y + 1))

    def visit(self, node):
        tmp = []
        valid_path = False
        for i in self.next:
            if i == (node.x, node.y):
                valid_path = True
            else:
                tmp.append(i)
        if valid_path:
            self.visited = True
            return tmp
        else:
            return []


    def __hash__(self) -> int:
        return hash((self.x, self.y))
    def __repr__(self) -> str:
        return f"(X:{self.x}, Y:{self.y}, {self.char})"


if __name__ == '__main__':
    chal1 = 0
    chal2 = 0
    m = Map()
    with open('day10.input.test1', 'r') as f:
        for y, line in enumerate(f):
            m.add(y, line.strip())

        chal1 = m.find_path()

    print(f"Challenge 1: {len(chal1)}")
    print(f"Challenge 2: {m.find_inner_tiles()}")
