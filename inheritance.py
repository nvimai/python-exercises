
# class Mammel:
#     def __init__(self, limb, type):
#         self._type = type
#         self._limb = limb
#         self._born = "Child"
#         self._feed = "Milk"

#     def limb(self, limb = None):
#         if(limb != None): self._limb = limb
#         return self._limb

#     def born(self):
#         return self._born

#     def feed(self):
#         return self._feed

#     def __str__(self):
#         return f"This is {self._type}, has {self._limb} limbs, borns {self._born}, feeds {self._feed}"

# class Human(Mammel):
#     def __init__(self, hand, foot):
#         self._type = "Human"
#         self._hand = hand
#         self._foot = foot
#         super().__init__(hand + foot, self._type)

#     def hand(self, hand = None):
#         if(hand != None):
#             self._hand = hand
#             super().limb(self._foot + hand)
#         return self._hand

#     def foot(self, foot = None):
#         if(foot != None):
#             self._foot = foot
#             super().limb(self._hand + foot)
#         return self._foot

#     def __str__(self):
#         return f"This is {self._type}, has {self._hand} hands and {self._foot} feet, borns {self._born}, feeds {self._feed}"

# class Dog(Mammel):
#     def __init__(self, limb, type):
#         super().__init__(limb, type)
#         self._bark = "Gâu gâu"
#     def type(self, type = None):
#         if(type != None): self._type = type
#         return self._type

#     def born(self, born = None):
#         if(born != None): self._born = born
#         return self._born
#     def feed(self, feed = None):
#         if(feed != None): self._feed = feed
#         return self._feed
#     def bark(self):
#         return self._bark
#     def __str__(self):
#         return f"This is {self._type}, bark {self._bark} ,has {self._limb} limb, borns {self._born}, feeds {self._feed} "


# class VietnameseDog(Dog):
#     def __init__(self, limb, type, eat):
#         super().__init__(limb, type)
#         self._eat = eat
#     def type(self, type = None):
#         if(type != None): self._type = type
#         return self._type
#     def eat(self, eat = None):
#         if(eat != None): self._eat = eat
#         return self._eat    
#     def born(self, born = None):
#         if(born != None): self._born = born
#         return self._born
#     def feed(self, feed = None):
#         if(feed != None): self._feed = feed
#         return self._feed
#     def bark(self):
#         return self._bark
#     def __str__(self):
#         return f"This is {self._type}, bark {self._bark} ,has {self._limb} limb, borns {self._born}, feeds {self._feed}, eat {self._eat} "


# mammel = Mammel(4, "Mammel")
# print(mammel.limb())
# print(mammel.born())
# print(mammel.feed())
# print(mammel)
# human = Human(2, 2)
# print(human.limb())
# print(human.hand())
# print(human.foot())
# print(human.born())
# print(human.feed())
# print(human)
# dog =Dog(4, "Dog")
# print(dog.limb())
# print(dog.born())
# print(dog.feed())
# print(dog)
# muc = VietnameseDog(4, "Vietnamese Dog", "Leftover rice")
# print(muc.limb())
# print(muc.born())
# print(muc.feed())
# print(muc)


# Product, Computer | Tablet, Speaker
# Product (name, type, brand, price, brief description)
# Computer | Speaker
# Tablet   | Google Home
class Product:
    def __init__(self, name, type, brand, price,):
        self._name = name
        self._type = type
        self._brand = brand
        self._price = price
        self._description = "This is a product of a website"

    def name(self, name = None):
        if(name != None): self._name = name
        return self._name

    def brand(self, brand = None):
        if(brand != None): self._brand = brand
        return self._brand

    def price(self, price = None):
        if(price != None): self._price = price
        return self._price

    def description(self):
        return self._description

    def __str__(self):
        return f"This is: {self._type}, name: {self._name}, brand: {self._brand}, price: {self._price}, and description: {self._description}."
class Computer(Product):
    def __init__(self, name, brand, price, cpu, ram, storage):
        self._type = "Computer"
        self._cpu = cpu
        self._ram = ram
        self._storage = storage
        super().__init__(name, self._type, brand, price)
    def cpu(self, cpu = None):
        if(cpu != None): self._cpu = cpu
        return self._cpu
    def ram(self, ram = None):
        if(ram != None): self._ram = ram
        return self._ram
    def storage(self, storage = None):
        if(storage != None): self._storage = storage
        return self._storage
    def __str__(self):
        return f"This is: {self._type}, name: {self._name}, brand: {self._brand}, price: {self._price}, and description: {self._description}, CPU: {self._cpu}, RAM: {self._ram}, STORAGE: {self._storage}."

class Tablet(Computer):
    def __init__(self, name, brand, price, cpu, ram, storage):
        self._mobile = "these are more portable than computers"
        self._screen = "has touch screen"
        super().__init__(name, brand, price, cpu, ram, storage)
    
    def __str__(self):
        return f"This is: {self._type} but {self._mobile} and {self._screen}, name: {self._name}, brand: {self._brand}, price: {self._price}, CPU: {self._cpu}, RAM: {self._ram}, STORAGE: {self._storage}, and description: {self._description},"
class Speaker(Product):
    def __init__(self, name, brand, price, wattage):
        self._wattage = wattage
        self._type = "Speaker"
        self._concept = "Can connect to devices to play music"
        super().__init__(name, self._type, brand, price)
    def wattage(self, wattage = None):
        if(wattage != None): self._wattage = wattage
        return self._wattage
    def __str__(self):
        return f"This is: {self._type}, {self._concept}, name: {self._name}, brand: {self._brand}, price: {self._price}, and description: {self._description}."

class GoogleHome(Speaker):
    def __init__(self, name, brand, price, wattage):
        self._assistant = "say Ok Google to talk with goole assistant"
        self._controlHome = "can control devices in your home"
        super().__init__(name, brand, price, wattage)
    def __str__(self):
        return f"This is: {self._type}, has function likes: {self._assistant}, {self._controlHome}, name: {self._name}, brand: {self._brand}, price: {self._price}, and description: {self._description}."

thanh = Product("Item", "product", "unknow", "unknow")
print(thanh.name())
print(thanh.brand())
print(thanh.price())
print(thanh)
thanh1 = Computer("PREDATOR", "ACER", "5000$", "I7 11700K", "16GB", "1TB HDD")
print(thanh1.name())
print(thanh1.brand())
print(thanh1.price())
print(thanh1.cpu())
print(thanh1.ram())
print(thanh1.storage())
print(thanh1)
thanh2 = Tablet("Ipad pro 11inch", "APPLE", "1500$", "M1", "8GB", "512GB")
print(thanh2.name())
print(thanh2.brand())
print(thanh2.price())
print(thanh2)
thanh3 = Speaker("Woburn 2", "Marshall", "500$", "130W")
print(thanh3.name())
print(thanh3.brand())
print(thanh3.price())
print(thanh3.description())
print(thanh3._concept)
print(thanh3)
thanh4 = GoogleHome("Google Home Mini", "Google", "25$", "9W")
print(thanh4.name())
print(thanh4.brand())
print(thanh4.price())
print(thanh4)

