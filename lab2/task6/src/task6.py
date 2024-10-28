"""
Поиск максимальной прибыли
"""

from lab2 import utils

file_in = open("../txtfiles/gzp.txt").read().split("\n")

lst = []
price_lst = []
for s in file_in:
    date, price = s.split(";")
    date = str(date)
    price = price.replace(",", ".")
    price = float(price)
    lst.append([date, price])
    price_lst.append(price)


def max_podposl(name: str, lst: list, price_list: list) -> str:
    """
    - Принимает на вход список со списками, в которых дата и цена соответственно, и список только с ценами в том же порядке, для удобного выбора п\п
    - Ищет максимальную подпоследовательность
    - Разница между первым и последним элементом максимальна
    - Возвращает: дату покупки, выручку, дату продажи
    """
    res = (
        f"Компания, акции которой анализируются: {name}\nАкции анализируются в период с {lst[-1][0]} по {lst[0][0]}\n"
        f"Чтобы получить прибыль от акций, лучше всего купить их ")

    low, high, max_sum = find_max_subarray(price_list)
    res += f"{lst[high][0]} за {lst[high][1]} и продать {lst[low][0]} за {lst[low][1]}\nТогда можно получить выручку равную {max_sum} за акцию."

    return res


def find_max_subarray(lst: list, low: int = 0, high: int = len(lst) - 1):
    """
    - Алгоритм поиска максимального подмассива, в случаях, если он находится слева или справа от середины
    - Вызывает другую функцию поиска максимальной п\п в случае, если п\п пересекает середину
    """
    if low == high:
        return low, high, abs(lst[low] - lst[high])
    else:
        mid = (low + high) // 2
        left_low, left_high, left_sum = find_max_subarray(lst, low, mid)
        right_low, right_high, right_sum = find_max_subarray(lst, mid + 1, high)
        cross_low, cross_high, cross_sum = find_max_cross_subarray(lst, low, mid, high)

        if left_sum >= right_sum and left_sum >= cross_sum:
            return left_low, left_high, left_sum
        elif right_sum >= left_sum and right_sum >= cross_sum:
            return right_low, right_high, right_sum
        else:
            return cross_low, cross_high, cross_sum


def find_max_cross_subarray(lst: list, low: int, mid: int, high: int):
    """
    - Алгоритм поиска п\п в случае, если п\п пересекает середину
    """
    max_left, max_right = 0, 0
    left_sum = -10 ** 6
    sum = 0
    for i in range(mid, low + 1, -1):
        sum += lst[i]
        if sum > left_sum:
            left_sum = sum
            max_left = i

    right_sum = -10 ** 6
    sum = 0
    for j in range(mid + 1, high + 1):
        sum += lst[j]
        if sum > right_sum:
            right_sum = sum
            max_right = j

    return max_left, max_right, abs(lst[max_left] - lst[max_right])


# utils.write_file([max_podposl("Газпром", lst, price_lst)])
print(max_podposl("Газпром", lst, price_lst))
