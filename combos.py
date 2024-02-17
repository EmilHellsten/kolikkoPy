from symbols import (Symbol, Blue_ray, Orange_ray, Star, Melon, Plum, Grape, Pear, Orange, Cherry, Strawberry)

validCombos = [
  [Orange_ray(), Orange_ray(), Orange_ray()],
  [Blue_ray(), Blue_ray(), Blue_ray()],
  [Blue_ray(), Blue_ray(), Star()],
  [Melon(), Melon(), Melon()],
  [Melon(), Melon(), Star()],
  [Plum(), Plum(), Plum()],
  [Plum(), Plum(), Star()],
  [Grape(), Grape(), Grape()],
  [Grape(), Grape(), Star()],
  [Pear(), Pear(), Pear()],
  [Pear(), Pear(), Star()],
  [Orange(), Orange(), Orange()],
  [Orange(), Orange(), Star()],
  [Cherry(), Cherry(), Cherry()],
  [Cherry(), Cherry(), Strawberry()],
  [Cherry(), Cherry(), Symbol()],  #
  [Symbol(), Symbol(), Strawberry()],  # 
  [Cherry(), Symbol(), Symbol()],  # 
]

# You can add more combinations or modify existing ones as needed
