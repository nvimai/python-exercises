# Write a Python mathematic class of 2 numbers
# Has methods: Sum (add), Subtract (sub), Multiply (mul), dividen (div)
# has Attributes: num1, num2
# Has setter, getter method
class Mathematic:
    def __init__(self, num1, num2):
        self._num1 = num1
        self._num2 = num2
    def num1(self, num1 = None):
        if (num1 != None): self._num1 = num1
        return self._num1
    def num2(self, num2 = None):
        if (num2 != None): self._num2 = num2
        return self._num2
    def sum(self):
       add = self._num1 + self._num2
       return add
    def subtract(self):
        sub = self._num1 - self._num2
        return sub
    def multiply(self):
        mul = self._num1 * self._num2
        return mul
    def dividen(self):
        try:
            div = self._num1 / self._num2
            return div
        except Exception as e:
            print(e)
        
# thanh = Mathematic(12, 21)
# nhat = Mathematic(13, 31)
# print(nhat.num1())
# print(thanh.sum())
# print(thanh.subtract())
# print(thanh.multiply())
# print(thanh.dividen())
# print(thanh.num1(2))
# print(thanh.num2(1))
# print(thanh.sum())
# print(thanh.subtract())
# print(thanh.multiply())
# print(thanh.dividen())



# Write a Python object of a rectangle shape
# Has attributes:
# Has Methods: size, setters, getters, print out value of 2 edges
class RectangleShape:
    def __init__(self, length, width):
        self._length = length
        self._width = width
    def size(self):
        size = self._length * self._width
        return size
    def length(self, length = None):
        if (length != None): self._length = length
        return self._length
    def width(self, width = None):
        if (width != None): self._width = width
        return self._width

    def __str__(self):
        return f'length: {self._length}, width: {self._width}'


# thanh = RectangleShape(4, 12)
# thanh.length(2)
# thanh.width(5)
# print(thanh.size())
# print(thanh)
# Write a Python object of a square shape
# Has attributes:
# Has Methods: size, setters, getters, print out value of an edge

# class SquareShape:
#     def __init__(self, edge):
#         self._edge = edge
#     def size(self):
#         size = self._edge**2
#         return size
#     def edge(self, edge = None):
#         if (edge != None): self._edge = edge
#         return self._edge
#     def __str__(self):
#         return f'edge: {self._edge}'

# thanh = SquareShape(5)
# print(thanh.edge(12))
# print(thanh.size())
# print(thanh)

class SquareShape(RectangleShape):
    # constructor
    def __init__(self, edge):
        super().__init__(edge, edge)

    # edge getter/setter
    def edge(self, edge = None):
        if(edge != None): 
            self._length = self._width = edge
        return self._length

    def __str__(self):
        return f'edge: {self._length}'

# thanhRect = RectangleShape(2, 3)
# thanhSquare = SquareShape(3)

# print(thanhRect)
# print(thanhRect.size())
# print(thanhSquare)
# print(thanhSquare.size())
# thanhSquare.edge(4)
# print(thanhSquare)
# print(thanhSquare.size())