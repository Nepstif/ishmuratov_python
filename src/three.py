class Counter:
    def __init__(self):
        self.numders_list = [5, 9, 3, 50, 5]

    def get_number(self):
        new_list = [three for three in self.numders_list if three % 3 == 0]
        return print(new_list)


if __name__ == "__main__":
    Counter().get_number()
