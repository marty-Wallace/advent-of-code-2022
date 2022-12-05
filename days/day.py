
class Day:

    def __init__(self, input_stream, output_stream):
        self.input_stream = input_stream
        self.output_stream = output_stream

    def part_one(self):
        raise NotImplemented

    def part_two(self):
        raise NotImplemented

    def p(self, *args):
        print(*args, file=self.output_stream)

