import os
import sys
from io import StringIO
from bs4 import BeautifulSoup

import requests

BASE_URL = 'https://adventofcode.com'
YEAR = 2022
DAY = 'day'
INPUT = 'input'
OUTPUT = 'output'
ANSWER = 'answer'
LEADERBOARD = 'leaderboard/private/view/'
SHOPIFY_BOARD = LEADERBOARD + '179752.json'
INPUT_DIR = './input/day'
PART_DIR = 'part'
TEST_INPUT_DIR = './input/test'
SECRETS_FILE = '.secrets'


class IOLoader:

    def __init__(self, year=YEAR, day=1, part_num=1, test=False, test_num=1, submit=False):
        self.year = year
        self.day = day
        self.cookies = None
        self.part_num = part_num
        self.test = test
        self.test_num = test_num
        self.submit = submit
        self.output_buffer = None

    def load_input(self):
        if not self.test and not self.input_exists():
            self.save_input_from_web()
        return self.load_input_from_file()

    def input_exists(self):
        return os.path.isfile(self.get_input_filename())

    def save_input_from_web(self):
        self.load_session_token()
        url = '%s/%d/%s/%d/%s' % (BASE_URL, self.year, DAY, self.day, INPUT)
        print('Reading input from location: ' + url)
        r = requests.get(url, cookies=self.cookies)
        if r.status_code != 200:
            print('Advent of Code returned code: %d \nExiting...' % r.status_code)
            exit(1)
        print('Creating new file ' + self.get_input_filename())
        with open(self.get_input_filename(), 'w') as file:
            file.write(r.text)

    def load_input_from_file(self):
        print('Loading file: ' + self.get_input_filename())
        return open(self.get_input_filename())

    def load_session_token(self):
        if self.cookies:
            return
        with open(SECRETS_FILE) as file:
            for line in file:
                if line.split('=')[0] == 'session':
                    self.cookies = {'session': line.split('=')[1].strip()}
                    return
        raise Exception('Session token not provided')

    def get_input_filename(self):
        if self.test:
            return '%s/%d/%s%d/%s%d' % (TEST_INPUT_DIR, self.day, PART_DIR, self.part_num, INPUT, self.test_num)
        return INPUT_DIR + '/' + INPUT + str(self.day)

    def get_output_filename(self):
        if not self.test:
            raise ValueError('Output directory is only for running tests')
        return '%s/%d/%s%d/%s%d' % (TEST_INPUT_DIR, self.day, PART_DIR, self.part_num, OUTPUT, self.test_num)

    def get_output_stream(self):
        if self.submit:
            self.output_buffer = StringIO()
            return self.output_buffer
        return sys.stdout

    def submit_answer(self):
        self.load_session_token()
        url = '%s/%d/%s/%d/%s' % (BASE_URL, self.year, DAY, self.day, ANSWER)
        print('Submitting answer to url: ' + url)
        payload = {
            'answer': self.output_buffer.getvalue(),
            'level': self.part_num
        }
        r = requests.post(url, data=payload, cookies=self.cookies)
        if r.status_code != 200:
            print('Advent of Code returned code: %d \nExiting...' % r.status_code)
            print(r.text)
            exit(1)
        result = r.text
        soup = BeautifulSoup(result, features="html.parser")
        print("\n".join(soup.main.article.p.text.split('.')))

    def get_ranking(self, board='shopify'):
        boards = {
            'shopify': SHOPIFY_BOARD
        }
        board_to_load = boards[board]
        if board_to_load is None:
            exit('Board ' + board + ' not found')
        self.load_session_token()
        url = '%s/%d/%s' % (BASE_URL, self.year, board_to_load)
        r = requests.get(url, cookies=self.cookies)
        return r.json()

    def finish(self):
        if not self.submit:
            return
        self.submit_answer()


if __name__ == '__main__':
    io = IOLoader(year=2021)
    res = io.get_ranking()
    print('')
