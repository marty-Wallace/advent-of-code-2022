
from days.day import Day


class Day4(Day):

    def part_one(self):
        count = 0
        for line in self.input_stream:
            left, right = line.strip().split(',')

            l0, l1 = left.split('-')
            r0, r1 = right.split('-')

            if int(l0) <= int(r0) and int(l1) >= int(r1):
                print(l0, l1, r0, r1)
                count += 1
            elif int(r0) <= int(l0) and int(r1) >= int(l1):
                print(r0, r1, l0, l1)
                count += 1
        self.p(count)

    def part_two(self):
        count = 0
        for line in self.input_stream:
            left, right = line.strip().split(',')

            l0, l1 = left.split('-')
            r0, r1 = right.split('-')
            l0 = int(l0)
            r0 = int(r0)
            l1 = int(l1)
            r1 = int(r1)

            if len(set(range(l0, l1+1)).intersection(set(range(r0, r1+1)))) > 0:
                count += 1
        self.p(count)


