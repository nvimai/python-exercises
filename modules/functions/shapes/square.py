from rectangle import Rectangle

class Square(Rectangle):
  def __init__(self, edge):
    super().__init__(edge, edge)

  def edge(self, edge = None):
    if(edge != None): 
      self._height = self._width = edge
    return self._height

  def __str__(self):
    return f'Square with: Edge({self._height})'