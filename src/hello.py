class Greeting:
    def __init__(self):
        self.nums = 7

    def number_checking(self):
        my_nums = float(input("Please enter nums: "))
        if my_nums > self.nums:
            return print("Привет")


if __name__ == "__main__":
    Greeting().number_checking()