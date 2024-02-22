import random

class Reel:
  def __init__(self, symbols):
    self.symbols = symbols
    self.length = len(self.symbols)

    #Simulate a spin, by selecting a random index
      #Whenever a Reel object is instantiated, it gets 'spun' to a random index.
      #This index represents the topmost visible symbol on the reel
    randomIndex = random.randint(0, self.length - 1)

    # Set symbolOne, symbolTwo, and symbolThree based on the selected index, ensure wrapping
    self.symbolOne = self.symbols[randomIndex]#Top symbol
    self.symbolTwo = self.symbols[(randomIndex + 1) % self.length]#Middle symbol
    self.symbolThree = self.symbols[(randomIndex + 2) % self.length]#Bottom symbol

    # FOR TESTING
    self.indexOne = randomIndex
    self.indexTwo = (randomIndex + 1) % self.length
    self.indexThree = (randomIndex + 2) % self.length

class LeftReel(Reel):
  def __init__(self):
    symbols = [
      'Blue_ray', 'Pear', 'Melon', 'Orange_ray', 'Pear', 'Melon', 'Plum', 'Melon', 'Pear', 'Melon',
      'Orange_ray', 'Blue_ray', 'Plum', 'Melon', 'Orange_ray', 'Plum', 'Pear', 'Cherry', 'Orange',
      'Orange_ray', 'Plum', 'Blue_ray', 'Grape', 'Blue_ray'
    ]
    super().__init__(symbols)

class MidReel(Reel):
  def __init__(self):
    symbols = [
      'Orange_ray', 'Melon', 'Cherry', 'Grape', 'Pear', 'Cherry', 'Plum', 'Melon', 'Plum', 'Blue_ray',
      'Grape', 'Melon', 'Melon', 'Pear', 'Grape', 'Orange', 'Orange_ray', 'Plum', 'Melon', 'Plum',
      'Cherry', 'Grape', 'Blue_ray', 'Orange'
    ]
    super().__init__(symbols)

class RightReel(Reel):
  def __init__(self):
    symbols = [
      'Plum', 'Melon', 'Melon', 'Orange_ray', 'Plum', 'Star', 'Blue_ray', 'Strawberry', 'Star',
      'Orange_ray', 'Orange', 'Pear', 'Grape', 'Melon', 'Star', 'Orange_ray', 'Grape', 'Cherry',
      'Star', 'Pear', 'Grape', 'Orange_ray', 'Star', 'Blue_ray'
    ]
    super().__init__(symbols)

class MultiplierReel(Reel):#TODO: This class should spin independently of the other reels
  def __init__(self):
    symbols = [
      'Tails', 'Heads', 'Heads', 'Neither', 'Heads', 'Tails', 'Tails', 'Heads', 'Tails', 'Tails',
      'Heads', 'Heads', 'Heads', 'Tails', 'Tails', 'Heads', 'Tails', 'Heads', 'Half', 'Heads',
      'Tails', 'Heads', 'Tails', 'Tails'
    ]
    super().__init__(symbols)


#FOR TESTING
#left_reel = LeftReel()
#print(f"Symbol One: {left_reel.symbolOne}, Index: {left_reel.indexOne}")
#print(f"Symbol Two: {left_reel.symbolTwo}, Index: {left_reel.indexTwo}")
#print(f"Symbol Three: {left_reel.symbolThree}, Index: {left_reel.indexThree}")
