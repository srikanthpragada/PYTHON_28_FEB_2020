class Player:
    def __init__(self, name):
        self.name = name

    def set_name(self, name):
        self.name = name


class Cricketer(Player):
    def __init__(self, name, runs):
        # super().__init__(name)
        Player.__init__(self, name)
        self.runs = runs

    def __str__(self):
        return f"{self.name} - {self.runs}"


class Footballer(Player):
    def __init__(self, name, goals):
        super().__init__(name)
        self.goals = goals

    def __str__(self):
        return f"{self.name} - {self.goals}"


f = Footballer("Gullet", 20)
f.set_name("Rud Gullet")
print(str(f))  # f.__str__()

print(isinstance(f, Footballer))
print(isinstance(f, Player))
print(issubclass(Footballer, Player))
print(issubclass(Footballer, object))
print(issubclass(list, object))
