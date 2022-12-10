
from days.day import Day


class Day10(Day):

    def part_one(self):
        cycle = 0
        x = 1
        s = 0
        for line in self.input_stream:
            cycle += 1
            if cycle % 40 == 20:
                s += cycle * x
            line = line.strip()
            if line == 'noop':
                pass
            else:
                cycle += 1

                op, num = line.split(' ')
                num = int(num)

                if cycle % 40 == 20:
                    s += cycle * x
                x += num
        self.p(s)

    def part_two(self):
        cycle = 0
        x = 1
        s = 0
        buf = ""
        for line in self.input_stream:
            cycle += 1
            if abs(x - ((cycle-1) % 40)) < 2:
                buf += "#"
            else:
                buf += "."
            if cycle % 40 == 0:
                print(buf)
                buf = ""
            line = line.strip()
            if line == 'noop':
                pass
            else:
                cycle += 1
                if abs(x - ((cycle-1) % 40)) < 2:
                    buf += "#"
                else:
                    buf += "."

                op, num = line.split(' ')
                num = int(num)
                if cycle % 40 == 0:
                    print(buf)
                    buf = ""
                x += num
        self.p(s)

