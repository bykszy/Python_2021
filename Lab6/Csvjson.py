import sys
import csv


class DataClass:
    def __init__(self, file):
        self.file = file

    def show(self):
        with open(self.file) as file:
            csv_reader = csv.reader(file)
            header = next(csv_reader)
            for idx, line in enumerate(csv_reader):
                print(f"Row {idx + 1}")
                for idx, header_row in enumerate(header):
                    print(f"{header_row} - {line[idx]}")
                print()

    def new(self):
        with open(self.file) as csv_in_file:
            csv_reader = csv.reader(csv_in_file)
            header = next(csv_reader)

        new_row = [input(f"Type new rew of data {header_row}: ") for header_row in header]
        with open(self.file, 'a+', newline='') as output:
            new_data = csv.writer(output)
            new_data.writerow(new_row)

    def remove(self):
        remove = int(input("Enter data that you want to delete: "))
        if remove == 0:
            print("Input out of range")
            return
        with open(self.file, 'r') as csv_in_file:
            reader = csv.reader(csv_in_file)
            lines = [row for row in reader]
            for i, line in enumerate(lines):
                if remove == i:
                    lines.remove(line)
                    break
            else:
                print("Did not find entered number of record")
                return
        with open(self.file, 'w', newline='') as output:
            writer = csv.writer(output)
            writer.writerows(lines)

    def menu(self):
        option = """
        Show stored data - show
        Add new data - add
        Remove data - remove
        quit
        """
        action_handler = {
            'show': self.show,
            'add': self.new,
            'remove': self.remove,
            'quit': sys.exit
        }
        while True:
            user_input = input(option)
            action_handler[user_input]()


if __name__ == '__main__':
    startup = DataClass("../files/todo.csv")
    startup.menu()
