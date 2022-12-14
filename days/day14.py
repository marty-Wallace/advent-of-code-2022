from days.day import Day

from collections import defaultdict

class Day14(Day):

    def parse_input(self, part_two=False):
        vmap = defaultdict(set)
        max_i, max_j = 0, 0
        min_j = 10**10
        for line in self.input_stream:
            coords = []
            for x in line.strip().split(' -> '):
                a, b = x.split(',')
                coords.append([int(a), int(b)])
                min_j = min(min_j, int(a))
                max_j = max(max_j, int(a))
                max_i = max(max_i, int(b))

            c1 = coords[0]
            for coord in coords[1:]:
                y1, x1 = c1
                y2, x2 = coord

                for j in range(min(y1, y2), max(y1, y2) + 1):
                    for i in range(min(x1, x2), max(x1, x2) + 1):
                        vmap[j].add(i)

                c1 = coord

        if part_two:
            for j in range(-10000, 10000):
                vmap[j].add(max_i+2)
        return vmap, max_i, min_j, max_j

    def drop_sand(self, vmap, i, j):
        if 0 in vmap[500] or not any(x > i for x in vmap[j]):
            return True
        if i+1 not in vmap[j]: # can move sand down
            return self.drop_sand(vmap, i+1, j)
        if (i + 1) not in vmap[j - 1]: # can move sand left
            return self.drop_sand(vmap, i+1, j-1)
        if (i + 1) not in vmap[j + 1]: # can move sand right
            return self.drop_sand(vmap, i+1, j+1)
        vmap[j].add(i)
        return False

    def print_vmap(self, vmap, max_i, min_j, max_j):
        for i in range(max_i+3):
            line = str(i) + ": "
            for j in range(min_j - 1, max_j + 2):
                if i in vmap[j]:
                    line += '#'
                else:
                    line += '.'
            print(line)
        print()

    def part_one(self):
        vmap, max_i, min_j, max_j = self.parse_input()
        count = 0
        while not self.drop_sand(vmap, 0, 500):
            count += 1
        self.p(count)

    def part_two(self):
        vmap, max_i, min_j, max_j = self.parse_input(part_two=True)
        count = 0
        # self.print_vmap(vmap, max_i, min_j, max_j)
        while not self.drop_sand(vmap, 0, 500):
            count += 1
            # self.print_vmap(vmap, max_i, min_j, max_j)
        self.p(count)
