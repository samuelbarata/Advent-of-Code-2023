class race:
    def __init__(self, time, distance):
        self.time = int(time)
        self.distance = int(distance)
        self.winning = []
        self.get_values()

    def get_values(self):
        for i in range(self.time+1):
            diff = self.time - i
            if i*diff > self.distance:
                self.winning.append(i*diff)

    def return_values(self):
        return len(self.winning)

if __name__ == '__main__':
    chal1 = 1
    chal2 = 0
    races = []
    with open('day6.input', 'r') as f:
        time_r = f.readline().strip()
        distance_r = f.readline().strip()
        time = []
        for x in time_r.split(':')[1].split(' '):
            if x != '':
                time.append(int(x))

        distance = []
        for x in distance_r.split(':')[1].split(' '):
            if x != '':
                distance.append(int(x))

        for i in range(len(time)):
            races.append(race(time[i], distance[i]))

        for k in races:
            chal1 *= k.return_values()

        time_2 = time_r.replace(' ', '').split(':')[1]
        distance_2 = distance_r.replace(' ', '').split(':')[1]

    print(f"Challenge 1: {chal1}")
    print(f"Challenge 2: {race(time_2, distance_2).return_values()}")
