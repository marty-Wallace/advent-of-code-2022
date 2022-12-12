
from days.day import Day


class Day12(Day):

    def part_one(self):
        grid = []
        for line in self.input_stream:
            grid.append([c for c in line.strip()])

        for ii in range(len(grid)):
            for jj in range(len(grid[ii])):
                if grid[ii][jj] == 'S':
                    i = ii
                    j = jj
                    break

        queue = [(i, j, grid[i][j] + ",")]
        self.p(self.find_path(grid, queue))

    def find_path(self, grid, queue):
        seen = set()
        while len(queue) > 0:
            i, j, p = queue.pop(0)
            if grid[i][j] == 'E':
                return len(p[:-1].split(",")) - 1
            for ix, jx in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                ti = i + ix
                tj = j + jx
                if ti < 0 or tj < 0 or ti >= len(grid) or tj >= len(grid[i]):
                    continue
                if (ti, tj) in seen:
                    continue
                target = grid[ti][tj]
                if target == 'E':
                    target = 'z'
                source = grid[i][j]
                if source == 'S':
                    source = 'a'
                if ord(target) > ord(source) and abs(ord(source) - ord(target)) <= 1:
                    queue.append((ti, tj, p + grid[ti][tj] + ","))
                    seen.add((ti, tj))
                elif ord(target) <= ord(source):
                    queue.append((ti, tj, p + grid[ti][tj] + ","))
                    seen.add((ti, tj))

    def part_two(self):
        grid = []
        for line in self.input_stream:
            grid.append([c for c in line.strip()])
        a = []
        for ii in range(len(grid)):
            for jj in range(len(grid[ii])):
                queue = []
                if grid[ii][jj] == 'S' or grid[ii][jj] == 'a':
                    queue.append((ii, jj, grid[ii][jj] + ","))
                    res = self.find_path(grid, queue)
                    if res:
                        a.append(res)

        self.p(min(a))
