from symbols import (Symbol, Blue_ray, Orange_ray, Star, Melon, Plum, Grape, Pear, Orange, Cherry, Strawberry, Heads, Tails, Neither, Half)#

class LeftReel:
  #Should contain following symbols:
  #[blue_ray, pear, melon, orange_ray, pear, melon, plum, melon, pear, melon, orange_ray, blue_ray, plum, melon, orange_ray, plum, pear, cherry, orange, orange_ray, plum, blue_ray, grapes, blue_ray]
  def __init__(self):
    self.symbols = [
      Blue_ray(), Pear(), Melon(), Orange_ray(), Pear(), Melon(), Plum(), Melon(), Pear(), Melon(), Orange_ray(), Blue_ray(), Plum(), Melon(), Orange_ray(), Plum(), Pear(), Cherry(), Orange(), Orange_ray(), Plum(), Blue_ray(), Grape(), Blue_ray()
    ]

class MidReel:
   #Should contain following symbols:
   #[Orange_ray(), Melon(), Cherry(), Grapes(), Pear(), Cherry(), Plum(), Melon(), Plum(), Blue_ray(), Grape(), Melon(), Melon(), Pear(), Grape(), Orange(), Orange_ray(), Plum(), Melon(), Plum(), Cherry(), Grape(), Blue_ray(), Orange()]
  def __init__(self):
    self.symbols = [
      Orange_ray(), Melon(), Cherry(), Grape(), Pear(), Cherry(), Plum(), Melon(), Plum(), Blue_ray(), Grape(), Melon(), Melon(), Pear(), Grape(), Orange(), Orange_ray(), Plum(), Melon(), Plum(), Cherry(), Grape(), Blue_ray(), Orange()
    ]


class RighttReel:
   #Should contain following symbols:
   #[Plum(), Melon(), Melon(), Orange_ray(), Plum(), Star(), Blue_ray(), Strawberry(), Star(), Orange_ray(), Orange(), Pear(), Grape(), Melon(), Star(), Orange_ray(), Grape(), Cherry, Star(), Pear(), Grape(), Orange_ray(), Star(), Blue_ray()]
  def __init__(self):
    self.symbols = [
      Plum(), Melon(), Melon(), Orange_ray(), Plum(), Star(), Blue_ray(), Strawberry(), Star(), Orange_ray(), Orange(), Pear(), Grape(), Melon(), Star(), Orange_ray(), Grape(), Cherry(), Star(), Pear(), Grape(), Orange_ray(), Star(), Blue_ray()
    ]

class MultiplierReel:
   #Should contain following symbols:
   #self.symbols = [
   # Tails(), Heads(), Heads(), Neither(), Heads(), Tails(), Tails(), Heads(), Tails(), Tails(), Heads(), Heads(), Heads(), Tails(), Tails(), Heads(), Tails(), Heads(), Half(), Heads(), Tails(), Heads(), Tails(), Tails()
   # ]
  def __init__(self):
    self.symbols = [
      Tails(), Heads(), Heads(), Neither(), Heads(), Tails(), Tails(), Heads(), Tails(), Tails(), Heads(), Heads(), Heads(), Tails(), Tails(), Heads(), Tails(), Heads(), Half(), Heads(), Tails(), Heads(), Tails(), Tails()
    ]
