
from days.day import Day


class Day5(Day):

    def part_one(self):
        lines = []
        instructions = []
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
        for i in range(ll+1):
            stacks.append([])
        lines.reverse()
        for line in lines:
            for i in range(ll+1):
                p = i*4 + 1
                if p < len(line) and line[p] != ' ':
                    stacks[i].append(line[p])

        for move in instructions:
            _, c, _, s, _, d = move.split(' ')
            c = int(c)
            s = int(s)
            d = int(d)
            for _ in range(c):
                stacks[d-1].append(stacks[s-1].pop())

        res = "".join(s.pop() for s in stacks)
        self.p(res)

    def part_two(self):
        lines = []
        instructions = []
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
        for i in range(ll+1):
            stacks.append([])
        lines.reverse()
        for line in lines:
            for i in range(ll+1):
                p = i*4 + 1
                if p < len(line) and line[p] != ' ':
                    stacks[i].append(line[p])

        for move in instructions:
            _, c, _, s, _, d = move.split(' ')
            c = int(c)
            s = int(s)
            d = int(d)
            temp = []
            for _ in range(c):
                temp.append(stacks[s-1].pop())
            for _ in range(c):
                stacks[d-1].append(temp.pop())

        res = "".join(s.pop() for s in stacks)
        self.p(res)


