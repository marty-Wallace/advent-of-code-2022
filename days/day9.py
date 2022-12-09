from days.day import Day


class Day9(Day):

    def parse_input(self):
        pass

    def part_one(self):
        head = [0, 0]
        tail = [0, 0]
        tails = set()
        tails.add((tail[0], tail[1]))
        for line in self.input_stream:
            direction, dist = self.parse_line(line)

            for _ in range(dist):
                head[0] += direction[0]
                head[1] += direction[1]

                self.move_tail(head, tail, tails)
        self.p(len(tails))

    def part_two(self):
        parts = []
        for i in range(10):
            parts.append([0, 0])
        head = parts[0]
        tails = set()
        tails.add((0, 0))
        for line in self.input_stream:
            direction, dist = self.parse_line(line)

            for _ in range(dist):
                head[0] += direction[0]
                head[1] += direction[1]

                h = head
                for index, part in enumerate(parts[1:]):
                    ts = set()
                    if index == 8:
                        ts = tails
                    self.move_tail(h, part, ts)
                    h = part
        self.p(len(tails))

    def parse_line(self, line):
        line = line.strip()
        dire, dist = line.split(' ')
        dist = int(dist)
        direction = {
            'R': [0, 1],
            'U': [-1, 0],
            'D': [1, 0],
            'L': [0, -1]
        }[dire]
        return direction, dist

    def move_tail(self, head, tail, tails):
        while abs(tail[0] - head[0]) > 1 or abs(tail[1] - head[1]) > 1:
            if abs(tail[0] - head[0]) > 0:
                if tail[0] < head[0]:
                    tail[0] += 1
                else:
                    tail[0] -= 1
            if abs(tail[1] - head[1]) > 0:
                if tail[1] < head[1]:
                    tail[1] += 1
                else:
                    tail[1] -= 1
            tails.add((tail[0], tail[1]))
