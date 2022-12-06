
class Day:

    def __init__(self, input_stream, output_stream):
        self.input_stream = input_stream
        self.output_stream = output_stream

    def part(self, part_num):
        if part_num == 1:
            self.part_one()
        elif part_num == 2:
            self.part_two()

    def part_one(self):
        raise NotImplemented

    def part_two(self):
        raise NotImplemented

    def p(self, *args):
        print(*args, end='', file=self.output_stream)

