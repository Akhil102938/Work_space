
class Player:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def update_score(self, score):
        self.score += score

    def display(self):
        print("Name:", self.name)
        print("Score:", self.score)


p1 = Player("Aki", 69)
p2 = Player("Mani", 50)

p1.update_score(30)
p1.display()

p2.update_score(29)
p2.display()
