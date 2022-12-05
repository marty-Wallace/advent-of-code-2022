

def my_import(module, className):
    """
    dynamically loads a python module
    :param module: the module the class is in
    :param clazz:
    :return:
    """
    mod = __import__(module, fromlist=[className])

    return getattr(mod, className)


class DayLoader:

    def __init__(self, day):
        self.day = day

    def load_day(self, input_stream, output_stream):
        try:
            return my_import('days.day%d' % self.day, 'Day%d' % self.day)(input_stream, output_stream)
        except ModuleNotFoundError:
            filename = "days/day%d.py" % self.day
            template = """
from days.day import Day


class Day%d(Day):

    def part_one(self):
        for line in self.input_stream:
            pass

    def part_two(self):
        for line in self.input_stream:
            pass

""" % self.day
            with open(filename, 'w') as f:
                f.write(template)

            return my_import('days.day%d' % self.day, 'Day%d' % self.day)(input_stream, output_stream)





