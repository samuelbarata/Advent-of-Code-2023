# Description: Advent of Code - Day 8
import math

if __name__ == '__main__':
    chal1 = 0
    chal2 = 0
    with open('day8.input', 'r') as f:
        instructions = f.readline().strip()
        f.readline()
        nodes = {}
        for line in f.readlines():
            line = line.strip()
            name = line.split(' = ')[0].strip()
            pseudo_tuple = line.split(' = ')[1]
            value = {'L':pseudo_tuple[1::].split(', ')[0], 'R': pseudo_tuple.split(', ')[1][:-1:]}
            nodes[name] = value

    current_node = [key for key in nodes.keys() if key.endswith('A')]
    Zs_found = [0 for _ in range(len(current_node))]
    instructions_length = len(instructions)
    while not all([zs != 0 for zs in Zs_found]):
        for k in range(len(current_node)):
            current_node[k] = nodes[current_node[k]][instructions[chal2 % instructions_length]]
            if current_node[k][-1] == 'Z':
                if current_node[k] == 'ZZZ' and chal1 == 0:
                    chal1 = chal2+1
                if Zs_found[k] == 0:
                    Zs_found[k] = chal2+1
        chal2 += 1


    print(f"Challenge 1: {chal1}")
    print(f"Challenge 2: {math.lcm(*Zs_found)}")
