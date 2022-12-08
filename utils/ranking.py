from utils.io_loader import IOLoader

USER = 'Martin Wallace'


class Ranking:

    def __init__(self, board='shopify'):
        self.board = board

    def _load_rankings(self, day):
        day = str(day)
        io = IOLoader()
        rankings = io.get_ranking(board=self.board)
        part1_ranks = []
        part2_ranks = []
        for id in rankings['members']:
            member = rankings['members'][id]
            if day in member['completion_day_level']:
                if '1' in member['completion_day_level'][day]:
                    part1_ranks.append((member['name'], member['completion_day_level'][day]['1']['get_star_ts']))
                if '2' in member['completion_day_level'][day]:
                    part2_ranks.append((member['name'], member['completion_day_level'][day]['2']['get_star_ts']))

        return part1_ranks, part2_ranks

    def get_ranking_for_day(self, day):
        part1_ranks, part2_ranks = self._load_rankings(day)
        my_part_1 = self._rank_for_part(part1_ranks, "1")
        my_part_2 = self._rank_for_part(part2_ranks, "2")

        if my_part_1 is None or my_part_2 is None:
            exit("Could not find any completion entries for day: " + day)

        self._print_time_taken_between_parts(my_part_1, my_part_2)

    def _rank_for_part(self, ranks, part):
        ranks.sort(key=lambda x: x[1])
        count = 1
        for pair in ranks:
            if pair[0] == USER:
                print("part " + part + " you came in " + str(count) + " place on leaderboard: " + self.board)
                return pair
            count += 1

    def _print_time_taken_between_parts(self, part1, part2):
        if part1 is None or part2 is None:
            return
        time1, time2 = part1[1], part2[1]
        minutes = (time2 - time1) // 60
        seconds = (time2 - time1) % 60
        print("time taken between parts: " + str(minutes) + "m " + str(seconds) + "s")


if __name__ == '__main__':
    Ranking().get_ranking_for_day("8")
