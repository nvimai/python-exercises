
from functions.math import sum2Nums, sub2Nums

print(sum2Nums(2, 3))
print(sub2Nums(4, 5))

from functions.shapes.rectangle import Rectangle
# from functions.shapes.square import Square

rec = Rectangle(4, 5)
print(rec)

# sq = Square(7)
# print(sq)

import time
print('1')
_time = (time.strptime("30 Nov 00", "%d %b %y") )
print(_time.tm_mon)
print('2')

# 