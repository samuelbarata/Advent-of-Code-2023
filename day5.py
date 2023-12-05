# Description: Advent of Code _ Day 5

import threading

class Mapper:
    def __init__(self, lines, name):
        self.name = name
        self.values = []
        self.parse(lines)

    def parse(self, lines):
        for line in lines:
            self.values.append([int(num) for num in line.strip().split(' ') if num])

    def map(self, num):
        for arr in self.values:
            if arr[1] <= num < arr[1]+arr[2]:
                diff = num - arr[1]
                return arr[0] + diff
        return num

seed_to_location = {}
min_location = 9999999999999999999999999999999
lock = threading.Lock()

def process_range(start, end, mappers, mappers_name):
    global min_location
    for seed in range(start, end):
        current = seed
        for mapper_name in mappers_name:
            current = mappers[mapper_name].map(current)
        with lock:
            min_location = min(min_location, current)
        #print(f"{((seed-start) /(end-start))*100}%")
        #seed_to_location[seed] = current

if __name__ == '__main__':
    chal1 = 9999999999999999999999999999999
    chal2 = 9999999999999999999999999999999
    mappers_name = ['seed_to_soil', 'soil_to_fertilizer', 'fertilizer_to_water', 'water_to_light', 'light_to_temperature', 'temperature_to_humidity', 'humidity_to_location']
    mappers = {}
    seeds = []
    with open('day5.input', 'r') as f:
        tmp = f.readline().strip().split(':')
        seeds = [int(num) for num in tmp[1].split(' ') if num]
        f.readline()
        lines = []
        for mapper_name in mappers_name:
            while True:
                line = f.readline()
                if line == '\n':
                    break
                if 'map' in line:
                    continue
                if line == '':
                    break
                lines.append(line.strip())
            mappers[mapper_name] = Mapper(lines, mapper_name)
            lines = []

    seed_to_location = {}
    for seed in seeds:
        current = seed
        for mapper_name in mappers_name:
            current = mappers[mapper_name].map(current)
        seed_to_location[seed] = current

    for location in seed_to_location:
        chal1 = min(chal1, seed_to_location[location])

    seed_to_location = {}
    threads = []
    for i in range(0, len(seeds), 2):
        t = threading.Thread(target=process_range, args=(seeds[i], seeds[i]+seeds[i+1], mappers, mappers_name))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    for location in seed_to_location:
        chal2 = min(chal2, seed_to_location[location])

    print(f"Challenge 1: {chal1}")
    print(f"Challenge 2: {min_location}")
