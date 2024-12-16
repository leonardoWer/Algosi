from lab6 import utils
import os

CURRENT_SCRIPT_DIR_PATH = os.path.dirname(os.path.abspath(__file__))


def hash_table_operations(n, x, a, b, ac, bc, ad, bd) -> list:
    hash_table = set()

    for i in range(n):
        if x in hash_table:
            a = (a + ac) % 10 ** 3
            b = (b + bc) % 10 ** 15
        else:
            hash_table.add(x)
            a = (a + ad) % 10 ** 3
            b = (b + bd) % 10 ** 15

        x = (x * a + b) % 10**15

    return [x, a, b]


def input_data():
    data = utils.read_file(CURRENT_SCRIPT_DIR_PATH)
    line1 = utils.str_to_list(data[0])
    line2 = utils.str_to_list(data[1])
    line1 = [int(i) for i in line1]
    line2 = [int(i) for i in line2]
    n, x, a, b = line1[0], line1[1], line1[2], line1[3]
    ac, bc, ad, bd = line2[0], line2[1], line2[2], line2[3]

    return n, x, a, b, ac, bc, ad, bd


def main():
    n, x, a, b, ac, bc, ad, bd = input_data()
    result = hash_table_operations(n, x, a, b, ac, bc, ad, bd)
    return result


if __name__ == "__main__":
    result = main()
    utils.write_file(CURRENT_SCRIPT_DIR_PATH, [result])
