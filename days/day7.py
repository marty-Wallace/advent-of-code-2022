from days.day import Day

data = {}


class Day7(Day):

    def parse_input(self):
        current_dir = ['/']
        for line in self.input_stream:
            line = line.strip()
            if line.startswith('$ cd'):
                dir = line.split(' ')[2]
                if dir == '/':
                    current_dir = ['/']
                elif dir == '..':
                    if len(current_dir) == 1:
                        current_dir = ['/']
                    else:
                        current_dir = current_dir[:-1]
                else:
                    current_dir.append(dir)
            elif line.startswith('$ ls'):
                pass
            else:
                dir = data
                for d in current_dir:
                    if not d in dir:
                        dir[d] = {}
                    dir = dir[d]
                size, name = line.strip().split(' ')
                if size != 'dir':
                    size = int(size)
                    dir[name] = size

    def part_one(self):
        self.parse_input()

        list = []
        self.sizer1(data, list, )
        self.p(sum(list))

    def sizer1(self, data, list):
        sum = 0
        for k in data:
            if type(data[k]) == int:
                sum += data[k]
            else:
                sum += self.sizer1(data[k], list)
        if sum <= 100000:
            list.append(sum)
        return sum

    def sizer2(self, data, list, need):
        sum = 0
        for k in data:
            if type(data[k]) == int:
                sum += data[k]
            else:
                sum += self.sizer2(data[k], list, need=need)
        if sum >= need:
            list.append(sum)
        return sum

    def part_two(self):
        self.parse_input()
        ss = self.sizer2(data['/'], [], 0)
        need = 30000000 - (70000000 - ss)
        ll = []
        self.sizer2(data['/'], ll, need)
        self.p(min(ll))

