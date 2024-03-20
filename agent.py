class Agent():
  def __init__(self, x: int, y: int):
    self.dd = 0
    self.du = -sqrt(2)/2
    self.ud = sqrt(2)/2
    self.uu = 0

    self.coordinates = (x, y)

  def PX(self, bit: int):
    pass

  def PY(self, bit: int):
    pass

  def PZ(self, bit: int):
    pass

  def CNOT(self, bit: int):
    pass

  def HADAUMARD(self, bit: int):
    pass

  def render(self):
    pass