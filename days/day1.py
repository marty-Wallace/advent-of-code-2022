
from days.day import Day


class Day1(Day):

    def part_one(self):
        m = 0
        s = 0
        for line in self.input_stream:
            if len(line.strip()) == 0:
                s = 0
            else:
                s += int(line)
                m = max(m, s)
        self.p(m)

    def part_two(self):
        s = 0
        e = []
        for line in self.input_stream:
            if len(line.strip()) == 0:
                e.append(s)
                s = 0
            else:
                s += int(line)
        e.append(s)

        self.p(sum(sorted(e, reverse=True)[:3]))


