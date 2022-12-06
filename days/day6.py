from days.day import Day


class Day6(Day):

    def part_one(self):
        for line in self.input_stream:
            a, b, c = line[:3]
            count = 3
            line = line[3:]
            while True:
                d = line[0]
                line = line[1:]
                count += 1
                if len({a, b, c, d}) == 4:
                    self.p(count)
                    break
                a, b, c, = b, c, d

    def part_two(self):
        for line in self.input_stream:
            chars = line[:13]
            count = 13
            line = line[13:]
            while True:
                d = line[0]
                line = line[1:]
                count += 1
                if len({*chars, d}) == 14:
                    self.p(count)
                    break
                chars = chars[1:]
                chars += d

