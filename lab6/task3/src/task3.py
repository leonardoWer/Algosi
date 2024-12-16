from lab6 import utils
import os

CURRENT_SCRIPT_DIR_PATH = os.path.dirname(os.path.abspath(__file__))


def hash_function(s, p=1000000007, x=263):
    hash_value = 0
    for i, char in enumerate(s):
        hash_value = (hash_value + ord(char) * (x ** i)) % p
    return hash_value


def commands_to_actions(m: int, n: int, requests: list[str]) -> list:
    hash_table = [[] for i in range(m)]
    result = []
    for query in requests:
        query = query.split()
        command = query[0]
        match command:
            case "add":
                string = query[1]
                hash_val = hash_function(string) % m
                if string not in hash_table[hash_val]:
                    hash_table[hash_val].insert(0, string)

            case "del":
                string = query[1]
                hash_val = hash_function(string) % m
                if string in hash_table[hash_val]:
                    hash_table[hash_val].remove(string)

            case "find":
                string = query[1]
                hash_val = hash_function(string) % m
                if string in hash_table[hash_val]:
                    result.append("yes")
                else:
                    result.append("no")

            case "check":
                i = int(query[1])
                if hash_table[i]:
                    result.append(" ".join(hash_table[i]))
                else:
                    result.append("")

            case _:
                return f"Команды {command} не существует!"

    return result


def input_data():
    data = utils.read_file(CURRENT_SCRIPT_DIR_PATH)
    m, n, requests = int(data[0]), int(data[1]), data[2:]
    return m, n, requests


def main():
    m, n, requests = input_data()
    result = commands_to_actions(m, n, requests)
    return result


if __name__ == "__main__":
    result = main()
    utils.write_file(CURRENT_SCRIPT_DIR_PATH, result, True)
