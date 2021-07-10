
class Mammel:
    def __init__(self, limb, type):
        self._type = type
        self._limb = limb
        self._born = "Child"
        self._feed = "Milk"

    def limb(self, limb = None):
        if(limb != None): self._limb = limb
        return self._limb

    def born(self):
        return self._born

    def feed(self):
        return self._feed

    def __str__(self):
        return f"This is {self._type}, has {self._limb} limbs, borns {self._born}, feeds {self._feed}"

class Human(Mammel):
    def __init__(self, hand, foot):
        self._type = "Human"
        self._hand = hand
        self._foot = foot
        super().__init__(hand + foot, self._type)

    def hand(self, hand = None):
        if(hand != None):
            self._hand = hand
            super().limb(self._foot + hand)
        return self._hand

    def foot(self, foot = None):
        if(foot != None):
            self._foot = foot
            super().limb(self._hand + foot)
        return self._foot

    def __str__(self):
        return f"This is {self._type}, has {self._hand} hands and {self._foot} feet, borns {self._born}, feeds {self._feed}"

class Dog(Mammel):
    pass

class VietnameseDog(Dog):
    pass

mammel = Mammel(4, "Mammel")
print(mammel.limb())
print(mammel.born())
print(mammel.feed())
print(mammel)
human = Human(2, 2)
print(human.limb())
print(human.hand())
print(human.foot())
print(human.born())
print(human.feed())
print(human)
dog = Dog(4, "Dog")
print(dog.limb())
muc = VietnameseDog(4, "Vietnamese Dog")
print(muc.limb())
print(muc.born())
print(muc.feed())

# Product, Computer | Tablet, Speaker
# Product (name, type, brand, price, brief description)
# Computer | Speaker
# Tablet   | Google Home