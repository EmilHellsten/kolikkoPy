from symbols import (Symbol, Blue_ray, Orange_ray, Star, Melon, Plum, Grape, Pear, Orange, Cherry, Strawberry, Heads, Tails, Neither, Half)#

class LeftReel:
  def __init__(self):
    self.symbols = [
      Blue_ray(), Pear(), Melon(), Orange_ray(), Pear(), Melon(), Plum(), Melon(), Pear(), Melon(), Orange_ray(), Blue_ray(), Plum(), Melon(), Orange_ray(), Plum(), Pear(), Cherry(), Orange(), Orange_ray(), Plum(), Blue_ray(), Grape(), Blue_ray()
    ]

    self.length = len(self.symbols) -1

class MidReel:
   def __init__(self):
    self.symbols = [
      Orange_ray(), Melon(), Cherry(), Grape(), Pear(), Cherry(), Plum(), Melon(), Plum(), Blue_ray(), Grape(), Melon(), Melon(), Pear(), Grape(), Orange(), Orange_ray(), Plum(), Melon(), Plum(), Cherry(), Grape(), Blue_ray(), Orange()
    ]
    self.length = len(self.symbols) -1

class RightReel:
  def __init__(self):
    self.symbols = [
      Plum(), Melon(), Melon(), Orange_ray(), Plum(), Star(), Blue_ray(), Strawberry(), Star(), Orange_ray(), Orange(), Pear(), Grape(), Melon(), Star(), Orange_ray(), Grape(), Cherry(), Star(), Pear(), Grape(), Orange_ray(), Star(), Blue_ray()
    ]
    self.length = len(self.symbols) -1

class MultiplierReel:
  def __init__(self):
    self.symbols = [
      Tails(), Heads(), Heads(), Neither(), Heads(), Tails(), Tails(), Heads(), Tails(), Tails(), Heads(), Heads(), Heads(), Tails(), Tails(), Heads(), Tails(), Heads(), Half(), Heads(), Tails(), Heads(), Tails(), Tails()
    ]
    self.length = len(self.symbols) -1
