
from days.day import Day


class Day2(Day):
    ROCK = 'A'
    PAPER2 = 'Y'
    PAPER = 'B'
    ROCK2 = 'X'
    SCISSORS = 'C'
    SCISSORS2 = 'Z'

    m = {
        ROCK: 'ROCK',
        SCISSORS: 'SCISSORS',
        PAPER: 'PAPER',
        ROCK2: 'ROCK',
        SCISSORS2: 'SCISSORS',
        PAPER2: 'PAPER',
    }

    score = {
        PAPER2: 2,
        ROCK2: 1,
        SCISSORS2: 3,
        'ROCK': 1,
        'PAPER': 2,
        'SCISSORS': 3
    }
    DRAW = 3
    WIN = 6

    def part_one(self):
        score = 0
        for line in self.input_stream:
            opp, me = line.strip().split(' ')
            score += self.x(self.m[opp], self.m[me]) + self.score[me]
        self.p(score)

    def x(self, opp, me):
        if opp == me:
            return 3
        if opp == 'ROCK':
            if me == 'SCISSORS':
                return 0
            else:
                return 6
        if opp == 'SCISSORS':
            if me == 'PAPER':
                return 0
            else:
                return 6
        if opp == 'PAPER':
            if me == 'ROCK':
                return 0
            else:
                return 6

    def part_two(self):
        score = 0
        for line in self.input_stream:
            opp, exp = line.strip().split(' ')

            me = self.choose_shape(self.m[opp], exp)
            score += self.x(self.m[opp], me) + self.score[me]
            print(self.m[opp], me, exp, score)

        self.p(score)

    def choose_shape(self, opp, expected):
        m = {
            'ROCK': {
                'Y': 'ROCK',
                'X': 'SCISSORS',
                'Z': 'PAPER'
            },

            'SCISSORS': {
                'Z': 'ROCK',
                'Y': 'SCISSORS',
                'X': 'PAPER'
            },
            'PAPER': {
                'Y': 'PAPER',
                'Z': 'SCISSORS',
                'X': 'ROCK'
            }
        }
        return m[opp][expected]

