import os
import sys
from io import StringIO
from timeit import default_timer as timer

from utils.day_loader import DayLoader
from utils.io_loader import IOLoader


def main():
    """
    Reads in args from command line. Loads day code and executes the chosen part of the day
    :return: None
    """
    def check_args(argv):
        if len(argv) < 1:
            print('No day supplied. \nExiting...')
            exit(1)

    args = sys.argv[1:]
    test_flag, submit_flag = False, False

    check_args(args)
    if args[0] == '--test' or args[0] == '-t':
        test_flag = True
        args = args[1:]

    check_args(args)
    if args[0] == '--submit' or args[0] == '-s':
        submit_flag = True
        args = args[1:]

    check_args(args)
    day_num = int(args[0])
    if len(args) < 2:
        print("No part supplied. Defaulting to part 1")
        part = 1
    else:
        part = int(args[1])

    if test_flag:
        print('Discovering tests for day: %d, part: %d' % (day_num, part))
        discover_tests(day_num, part)
    else:
        print('Running day: %d, part: %d' % (day_num, part))
        run(day_num, part, submit_flag)


def run(day_num, part, submit):
    io_loader = IOLoader(day=day_num, part_num=part, submit=submit)
    input_stream = io_loader.load_input()
    day = DayLoader(day_num).load_day(input_stream, io_loader.get_output_stream())
    day.part(part)
    io_loader.finish()


def test(day_num, part_num, test_num):
    start = timer()
    print()
    print('Testing day: %d, part %d, test_num: %d' % (day_num, part_num, test_num))
    input_stream = IOLoader(day=day_num, part_num=part_num, test=True, test_num=test_num).load_input()
    output_stream = StringIO()
    day = DayLoader(day_num).load_day(input_stream, output_stream)
    day.part(part_num)
    end = timer()
    print("Time taken: %.5f seconds" % (end-start))
    validate_output(day_num, part_num, test_num, output_stream.getvalue().split('\n'))


def validate_output(day_num, part_num, test_num, actual_lines):
    with open(IOLoader(day=day_num, part_num=part_num, test=True, test_num=test_num).get_output_filename()) as exp_file:
        expected_lines = "\n".join(exp_file).split("\n")

    line = 1
    for lineA, lineE in zip(actual_lines, expected_lines):
        if lineA != lineE:
            print("ACTUAL different than expected at line: %d" % line)
            print("-----ACTUAL")
            print("\n".join(actual_lines))
            print("-----EXPECTED")
            print("\n".join(expected_lines))
            return
        line += 1
    print("Test matched exactly")


def discover_tests(day_num, part_num):
    i = 1
    tests = []
    while 1:
        if not os.path.isfile(IOLoader(day=day_num, part_num=part_num, test=True, test_num=i).get_input_filename()):
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
