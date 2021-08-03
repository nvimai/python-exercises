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


