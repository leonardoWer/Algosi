from lab7 import utils
import os


CURRENT_SCRIPT_DIR_PATH = os.path.dirname(os.path.abspath(__file__))


def longest_common_subsequence(n1:int, lst1:list, n2:int, lst2:list) -> int:
    dp = [[0] * (n2 + 1) for i in range(n1 + 1)] # Таблица

    # Заполняем таблицу
    for i in range(1, n1 + 1):
        for j in range(1, n2 + 1):
            if lst1[i - 1] == lst2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[n1][n2]


def input_data() -> (int, list, int, list):
    data = utils.read_file(CURRENT_SCRIPT_DIR_PATH)
    n1, lst1, n2, lst2 = int(data[0]), utils.str_to_list(data[1]), int(data[2]), utils.str_to_list(data[3])
    return n1, lst1, n2, lst2


def main():
    n1, lst1, n2, lst2 = input_data()
    result = longest_common_subsequence(n1, lst1, n2, lst2)
    return result


if __name__ == "__main__":
    result = main()
    utils.write_file(CURRENT_SCRIPT_DIR_PATH, [result])
