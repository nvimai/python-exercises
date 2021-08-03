class Rectangle:
  def __init__(self, height, width):
    self._height = height
    self._width = width

  def height(self, height = None):
    if(height != None): self._height = height
    return self._height

  def width(self, width = None):
    if(width != None): self._width = width
    return self._width

  def __str__(self):
    return f'Rectangle with: Height({self._height}) and Width({self._width})'