
from days.day import Day


class Day5(Day):

    def parse_input(self):
        lines, instructions = [], []
        ll = 0
        for line in self.input_stream:
            if line.strip().startswith('['):
                lines.append(line.strip('\n'))
            elif line.strip().startswith('1'):
                ll = int(line.strip().split(' ')[-1]) - 1
            elif line.strip() == '':
                pass
            else:
                instructions.append(line.strip())

        stacks = []
        for _ in range(ll + 1):
            stacks.append([])
        lines.reverse()
        for line in lines:
            for i in range(ll + 1):
                p = i * 4 + 1
                if p < len(line) and line[p] != ' ':
                    stacks[i].append(line[p])

        return lines, instructions, stacks

    def part_one(self):
        lines, instructions, stacks = self.parse_input()
        for move in instructions:
            c, s, d = map(int, move.split(' ')[1::2])
            for _ in range(c):
                stacks[d-1].append(stacks[s-1].pop())

        res = "".join(s.pop() for s in stacks)
        self.p(res)

    def part_two(self):
        lines, instructions, stacks = self.parse_input()
        for move in instructions:
            c, s, d = map(int, move.split(' ')[1::2])
            temp = []
            for _ in range(c):
                temp.append(stacks[s-1].pop())
            for _ in range(c):
                stacks[d-1].append(temp.pop())

        res = "".join(s.pop() for s in stacks)
        self.p(res)


