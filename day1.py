# Description: Advent of Code - Day 1

def replace_words(line):
    """
    Replaces words with numbers
    """
    number = ''
    new_line = ''
    for char in line:
        if char in ['0','1','2','3','4','5','6','7','8','9']:
            number += char
        new_line += char
        if 'one' in new_line[-3::]:
            number += '1'
        elif 'two' in new_line[-3::]:
            number += '2'
        elif 'three' in new_line[-5::]:
            number += '3'
        elif 'four' in new_line[-4::]:
            number += '4'
        elif 'five' in new_line[-4::]:
            number += '5'
        elif 'six' in new_line[-3::]:
            number += '6'
        elif 'seven' in new_line[-5::]:
            number += '7'
        elif 'eight' in new_line[-5::]:
            number += '8'
        elif 'nine' in new_line[-4::]:
            number += '9'
    return number

def parse_line(line, find_words = False) -> int:
    """
    Recieves a line of text
    Return an int formed by the first digit in the string and the last digit in the string
    """
    first = None
    last = None
    line = line.strip()
    original = line

    if find_words:
        line = replace_words(line)

    for char in line:
        if(char in ['0','1','2','3','4','5','6','7','8','9']):
            if first is None:
                first = char
                last = char
            else:
                last = char
    print(f"{original} -> {line}: {first+last}")
    return int(first+last)

if __name__ == '__main__':
    value = 0
    with open('day1.input', 'r') as f:
        for line in f.readlines():
            value += parse_line(line, True)
    print(value)
