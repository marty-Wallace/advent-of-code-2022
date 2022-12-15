from days.day import Day


class Day15(Day):

    def parse_input(self):
        sensors = {}
        for line in self.input_stream:
            left, right = line.strip().split(':')

            lx, ly = left.split(',')
            x1 = int(lx.split('=')[1])
            y1 = int(ly.split('=')[1])

            rx, ry = right.split(',')
            x2 = int(rx.split('=')[1])
            y2 = int(ry.split('=')[1])
            sensors[(x1, y1)] = (x2, y2)

        return sensors

    def m_dist(self, a, b):
        return abs(a[0] - b[0]) + abs(a[1] - b[1])

    def part_one(self):
        sensors = self.parse_input()
        count = 0
        for i in range(-10000000, 10000000):
            for s in sensors:
                max_dist = self.m_dist(s, sensors[s])

                if self.m_dist((i, 2000000), s) <= max_dist:
                    if (i, 2000000) not in sensors.values():
                        # print(s, sensors[s], (i, 2000000))
                        count += 1
                        break

        self.p(count)

    def part_two(self):
        MAX = 4_000_000
        sensors = self.parse_input()

        for s in sensors:
            max_dist = self.m_dist(s, sensors[s])
            m = max_dist + 1
            pos = [
                [s[0] + m, s[1]],
                [s[0] - m, s[1]],
                [s[0], s[1] + m],
                [s[0], s[1] - m]]
            print(s, m, pos)
            for i in range(m):
                for p in pos:
                    if p[0] < 0 or p[0] > MAX or p[1] < 0 or p[1] > MAX:
                        continue
                    all = True
                    for s in sensors:
                        m_dist = self.m_dist(s, sensors[s])
                        if self.m_dist(p, s) <= m_dist:
                            all = False
                            break
                    if all:
                        print(p)
                        self.p(p[0] * MAX + p[1])
                        return
                a, b, c, d = pos
                a[0] -= 1
                a[1] += 1
                b[0] += 1
                b[1] -= 1
                c[0] += 1
                c[1] -= 1
                d[0] -= 1
                d[1] += 1
