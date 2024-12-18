from lab7 import utils
import os


CURRENT_SCRIPT_DIR_PATH = os.path.dirname(os.path.abspath(__file__))


def min_coins(money, coins):
    dp = [float('inf')] * (money + 1)  # Создаем массив для хранения минимального количества монет для каждой суммы
    dp[0] = 0  # Нулевая сумма требует ноль монет

    # Заполняем массив dp
    for coin in coins:
        for x in range(coin, money + 1):
            dp[x] = min(dp[x], dp[x - coin] + 1)

    return dp[money] if dp[money] != float('inf') else -1  # Если сумма не достижима


def input_data() -> (int, int, list):
    data = utils.read_file(CURRENT_SCRIPT_DIR_PATH)
    line1 = data[0]
    line2 = data[1]
    money, k = map(int, line1.split())
    coins_list = utils.str_to_list(line2)
    return money, k, coins_list


def main():
    money, k, coins_list = input_data()
    result = min_coins(money, coins_list)
    return result


if __name__ == "__main__":
    result = main()
    utils.write_file(CURRENT_SCRIPT_DIR_PATH, [result])
