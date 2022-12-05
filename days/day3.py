
from days.day import Day


class Day3(Day):

    def part_one(self):
        sum = 0
        for line in self.input_stream:
            half = int(len(line)/2)
            left = line[:half]
            right = line[half:]
            l = set(left)
            r = set(right)
            matches = l.intersection(r)

            print(matches)
            for a in matches:
                if a == a.upper():
                    sum += (ord(a) - ord('A') ) + 27
                else:
                    sum += ord(a) - ord('a') + 1
            print(sum)
        self.p(sum)

    def part_two(self):
        c = 0
        s = []
        sum = 0
        for line in self.input_stream:
            c += 1
            s.append(set(line.strip()))
            print(c, s)

            if c == 3:
                s1, s2, s3 = s[0], s[1], s[2]

                match = s1.intersection(s2).intersection(s3)
                print(len(match))
                for a in match:
                    if a == a.upper():
                        sum += (ord(a) - ord('A')) + 27
                    else:
                        sum += ord(a) - ord('a') + 1

                s = []
                c = 0
        self.p(sum)




