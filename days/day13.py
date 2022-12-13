import functools

from days.day import Day


class Day13(Day):

    def part_one(self):
        c = 1
        count = 0
        for line in self.input_stream:
            if line.strip() == '':
                continue
            if c % 2 == 1:
                exec("global left; left = " + line.strip())
            else:
                exec("global right; right = " + line.strip())
                if self.is_in_order(left, right):
                    count += c//2
            c += 1

        self.p(count)

    def is_in_order(self, left, right):
        if type(left) == int and type(right) == int:
            if left == right:
                return None
            return left < right
        if type(left) == int:
            left = [left]
        if type(right) == int:
            right = [right]
        for ll, rr in zip(left, right):
            res = self.is_in_order(ll, rr)
            if res is not None:
                return res
        if len(left) == len(right):
            return None
        return len(left) < len(right)

    def part_two(self):
        def compare_packets(left, right):
            res = self.is_in_order(left, right)
            if res is None:
                return 0
            if res:
                return -1
            else:
                return 1
        packets = []
        for line in self.input_stream:
            if line.strip() == '':
                continue
            exec("global left; left = " + line.strip())
            packets.append(left)

        packets += [[2], [6]]
        packets.sort(key=functools.cmp_to_key(compare_packets))

        i1 = packets.index([2]) + 1
        i2 = packets.index([6]) + 1
        self.p(i1 * i2)
