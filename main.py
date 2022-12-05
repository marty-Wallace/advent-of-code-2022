import os
import sys
from io import StringIO
from timeit import default_timer as timer

from utils.day_loader import DayLoader
from utils.input_loader import InputLoader


def main():
    """
    Reads in args from command line. Loads correct day code via reflection and executes the
    correct part of the day
    :return: None
    """
    args = sys.argv[1:]
    test = False
    if len(args) < 1:
        print('No day supplied. \nExiting...')
        exit(1)

    if args[0] == '--test' or args[0] == '-t':
        test = True
        args = args[1:]

    day_num = int(args[0])
    if len(args) < 2:
        print("No part supplied. Defaulting to part 1")
        part = 1
    else:
        part = int(args[1])

    if test:
        print('Discovering tests for day: %d, part: %d' % (day_num, part))
        discover_tests(day_num, part)
    else:
        print('Running day: %d, part: %d' % (day_num, part))
        run(day_num, part)


def run(day_num, part):
    input_stream = InputLoader(day_num).load_input()
    day = DayLoader(day_num).load_day(input_stream, sys.stdout)
    if part == 1:
        day.part_one()
    else:
        day.part_two()


def test(day_num, part_num, test_num):
    start = timer()
    print()
    print('Testing day: %d, part %d, test_num: %d' % (day_num, part_num, test_num))
    input_stream = InputLoader(day_num, part_num=part_num, test=True, test_num=test_num).load_input()
    output_stream = StringIO()
    day = DayLoader(day_num).load_day(input_stream, output_stream)
    if part_num == 1:
        day.part_one()
    else:
        day.part_two()
    end = timer()
    print("Time taken: %.5f seconds" % (end-start))
    validate_output(day_num, part_num, test_num, output_stream.getvalue().split('\n'))


def validate_output(day_num, part_num, test_num, actual_lines):
    with open(InputLoader(day_num, part_num=part_num, test=True, test_num=test_num).get_output_filename()) as exp_file:
        expected_lines = "\n".join([line for line in exp_file]).split("\n")

    line = 1
    for lineA, lineE in zip(actual_lines, expected_lines):
        if lineA != lineE:
            print('ACTUAL different than expected at line: %d' % line)
            print('-----ACTUAL')
            print("\n".join([line for line in actual_lines]))
            print('-----EXPECTED')
            print("\n".join([line for line in expected_lines]))
            return
        line += 1
    print('Test matched exactly')


def discover_tests(day_num, part_num):
    i = 1
    tests = []
    while 1:
        if not os.path.isfile(InputLoader(day_num, part_num=part_num, test=True, test_num=i).get_input_filename()):
            break
        tests.append(i)
        i = i + 1
    print(str(len(tests)) + " test(s) found.")
    for i in tests:
        test(day_num, part_num, i)


if __name__ == '__main__':
    # use this for manually testing cmd line args
    # sys.argv = ['',  '6', '1']
    # sys.argv = ['',  '--test', '6', '1']
    main()
