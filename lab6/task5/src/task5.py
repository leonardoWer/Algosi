from lab6 import utils
import os

CURRENT_SCRIPT_DIR_PATH = os.path.dirname(os.path.abspath(__file__))


def calculate_election_results(votes_list):
    votes = {}

    for entry in votes_list:
        candidate, count = entry.split()
        count = int(count)
        if candidate in votes:
            votes[candidate] += count
        else:
            votes[candidate] = count

    sorted_candidates = sorted(votes.items())

    result = [f"{candidate} {total_votes}" for candidate, total_votes in sorted_candidates]
    return result


def input_data():
    data = utils.read_file(CURRENT_SCRIPT_DIR_PATH)
    return data


def main():
    candidates_list = input_data()
    result = calculate_election_results(candidates_list)
    return result


if __name__ == "__main__":
    result = main()
    utils.write_file(CURRENT_SCRIPT_DIR_PATH, result)
