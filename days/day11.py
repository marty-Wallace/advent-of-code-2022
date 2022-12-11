from days.day import Day


class Day11(Day):

    def parse_input(self):
        monkeys = {}
        cur = {}
        for line in self.input_stream:
            if line.startswith('Monkey'):
                cur = {'count': 0}
                n = int(line.split(' ')[1].split(':')[0])
                monkeys[n] = cur
            if line.strip().startswith('Starting items:'):
                items = list(map(int, line.split(':')[1].split(',')))
                cur['i'] = items
            if line.strip().startswith('Oper'):
                op = line.strip().split(':')[1].strip()
                cur['op'] = op
            if line.strip().startswith('Test'):
                test = line.strip().split(':')[1].strip().split(' ')[-1]
                cur['test'] = test
            if line.strip().startswith('If true'):
                true = int(line.strip().split(':')[1].strip().split(' ')[-1])
                cur['true'] = true
            if line.strip().startswith('If false'):
                true = int(line.strip().split(':')[1].strip().split(' ')[-1])
                cur['false'] = true
        return monkeys

    def part_one(self):
        monkeys = self.parse_input()
        common = self.find_common(monkeys)
        for i in range(20):
            self.tick(monkeys, common, part='1')

        most = sorted([monkeys[m]['count'] for m in monkeys])
        self.p(most[-1] * most[-2])

    def part_two(self):
        monkeys = self.parse_input()
        common = 1
        for m in monkeys:
            common *= int(monkeys[m]['test'])
        for i in range(10_000):
            self.tick(monkeys, common, part='2')

        most = sorted([monkeys[m]['count'] for m in monkeys])
        self.p(most[-1] * most[-2])

    def tick(self, monkeys, common, part='1'):
        for k in monkeys:
            monkey = monkeys[k]
            new_items = [self.calc_value(item, monkey, common, part) for item in monkey['i']]
            for value, m_id in new_items:
                monkeys[m_id]['i'].append(value)
            monkey['i'] = []

    def calc_value(self, item, monkey, common, part):
        monkey['count'] += 1
        o1, op, o2 = monkey['op'].split('=')[1].strip().split(' ')
        oo1 = item if o1 == 'old' else int(o1)
        oo2 = item if o2 == 'old' else int(o2)
        eq = eval(str(oo1) + ' ' + op + ' ' + str(oo2))
        if part == '1':
            eq //= 3
        else:
            eq %= common
        if eq % int(monkey['test']) == 0:
            return eq, monkey['true']
        else:
            return eq, monkey['false']

    def find_common(self, monkeys):
        common = 1
        for m in monkeys:
            common *= int(monkeys[m]['test'])
        return common
