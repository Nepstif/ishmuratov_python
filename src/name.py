class People:
    def __init__(self):
        self.greetings = "Вячеслав"

    def phrasebook(self):
        name = input("Please enter is name: ")
        if name == self.greetings:
            return print("Привет, " + self.greetings)
        return print("Нет такого имени")


if __name__ == "__main__":
    People().phrasebook()
