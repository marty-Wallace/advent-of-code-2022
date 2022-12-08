from days.day import Day


class Day8(Day):

    def part_one(self):
        grid = []
        for line in self.input_stream:
            row = [int(i) for i in line.strip()]
            grid.append(row)

        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if i == 0 or j == 0 or i == len(grid)-1 or j == len(grid)-1:
                    count += 1
                    continue
                if max(grid[x][j] for x in range(i+1, len(grid))) < grid[i][j]:
                    count += 1
                    continue
                if max(grid[x][j] for x in range(i-1, -1, -1)) < grid[i][j]:
                    count += 1
                    continue
                if max(grid[i][x] for x in range(j+1, len(grid[i]))) < grid[i][j]:
                    count += 1
                    continue
                if max(grid[i][x] for x in range(j-1, -1, -1)) < grid[i][j]:
                    count += 1
                    continue
        self.p(count)

    def part_two(self):
        grid = []
        for line in self.input_stream:
            row = [int(i) for i in line.strip()]
            grid.append(row)

        best = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                num = 1
                c = 0
                for x in range(i + 1, len(grid)):
                    c += 1
                    if grid[x][j] >= grid[i][j]:
                        break
                num *= c
                c = 0
                for x in range(i - 1, -1, -1):
                    c += 1
                    if grid[x][j] >= grid[i][j]:
                        break
                num *= c
                c = 0
                for x in range(j + 1, len(grid[i])):
                    c += 1
                    if grid[i][x] >= grid[i][j]:
                        break
                num *= c
                c = 0
                for x in range(j - 1, -1, -1):
                    c += 1
                    if grid[i][x] >= grid[i][j]:
                        break
                num *= c
                best = max(best, num)
        self.p(best)
