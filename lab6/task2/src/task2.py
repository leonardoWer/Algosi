from lab6 import utils
import os

CURRENT_SCRIPT_DIR_PATH = os.path.dirname(os.path.abspath(__file__))


class PhoneBook:
    """Телефонная книга"""

    def __init__(self):
        self.contacts_book = {}

    def __str__(self):
        all_contacts = ""
        for number in self.contacts_book:
            all_contacts += f"{number} {self.contacts_book[number]}"
        return all_contacts

    def add_contact(self, number:str, name: str):
        self.contacts_book[number] = name

    def del_contact(self, number: str):
        self.contacts_book.pop(number, None)

    def find_number(self, number: str):
        if number in self.contacts_book.keys():
            return self.contacts_book[number]
        return "not found"

    def commands_to_actions(self, commands:list[str]):
        result = []
        for command in commands:
            command = command.split()
            operation = command[0]
            match operation:
                case "add":
                    number, name = command[1], command[2]
                    self.add_contact(number, name)
                case "del":
                    number = command[1]
                    self.del_contact(number)
                case "find":
                    number = command[1]
                    result.append(self.find_number(number))
                case _:
                    return f"Команды {operation} нет!"

        return result


def input_data():
    data = utils.read_file(CURRENT_SCRIPT_DIR_PATH)
    n, commands = data[0], data[1:]
    return n, commands


def main():
    n, commands = input_data()
    my_phone_book = PhoneBook()
    result = my_phone_book.commands_to_actions(commands)

    return result


if __name__ == "__main__":
    result = main()
    utils.write_file(CURRENT_SCRIPT_DIR_PATH, result)
