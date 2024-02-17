#from operator import le
import random
from reels import LeftReel, MidReel, RightReel, MultiplierReel

class SlotGrid:
  def __init__(self):
    self.grid = [
      [None, None, None, None],
      [None, None, None, None],
      [None, None, None, None]
    ]

    self.lineCoords = [
      [(0, 0), (1, 1), (2, 2)],
      [(0, 0), (0, 1), (0, 2)],
      [(1, 0), (1, 1), (1, 2)],
      [(2, 0), (2, 1), (2, 2)],
      [(2, 0), (1, 1), (0, 2)]
    ]

    self.multiplierCoords = [
      [(0, 3), (1, 3), (2, 3)]
    ]#Tässä kiinnostaa ainoastaan keskimmäinen arvo?

    #reels
    self.leftReel = LeftReel()
    self.midReel = MidReel()
    self.rightReel = RightReel()
    self.multiplierReel = MultiplierReel()

    #randomly assign starting positions for each 'head'
    self.leftHead = random.randint(0, self.leftReel.length)    
    self.midHead = random.randint(0, self.midReel.length)    
    self.rightHead = random.randint(0, self.rightReel.length)    
    self.multHead = random.randint(0, self.multiplierReel.length)    #
    
    #body
    self.leftBody = (self.leftHead + 1) if ( (self.leftHead + 1) < self.leftReel.length) else (self.leftHead + 1 - self.leftReel.length)
    self.midBody = (self.midHead + 1) if ( (self.midHead + 1) < self.midReel.length) else (self.midHead + 1 - self.midReel.length)
    self.rightBody = (self.rightHead + 1) if ( (self.rightHead + 1) < (self.rightReel.length) ) else (self.rightHead + 1 - self.rightReel.length)
    self.multBody = (self.multHead + 1) if ( (self.multHead + 1) < (self.multiplierReel.length) ) else (self.multHead + 1 - self.multiplierReel.length)
  
    #tail
    self.leftTail = (self.leftHead + 2) if ( (self.leftHead + 2) < self.leftReel.length) else (self.leftHead + 2 - self.leftReel.length)
    self.midTail = (self.midHead + 2) if ( (self.midHead + 2) < self.midReel.length) else (self.midHead + 2 - self.midReel.length)
    self.rightTail = (self.rightHead + 2) if ( (self.rightHead + 2) < (self.rightReel.length) ) else (self.rightHead + 2 - self.rightReel.length)
    self.multTail = (self.multHead + 2) if ( (self.multHead + 2) < (self.multiplierReel.length) ) else (self.multHead + 2 - self.multiplierReel.length)
  
    #update the grid with the starting positions
    self.updateGrid()

  def updateGrid(self):
    # Clear the current grid
    self.grid = [[None, None, None, None] for _ in range(3)]

    # Update the grid with symbols from the regular reels
    self.grid[0][0] = self.leftReel.symbols[self.leftHead]
    self.grid[1][0] = self.leftReel.symbols[self.leftBody]
    self.grid[2][0] = self.leftReel.symbols[self.leftTail]

    self.grid[0][1] = self.midReel.symbols[self.midHead]
    self.grid[1][1] = self.midReel.symbols[self.midBody]
    self.grid[2][1] = self.midReel.symbols[self.midTail]

    self.grid[0][2] = self.rightReel.symbols[self.rightHead]
    self.grid[1][2] = self.rightReel.symbols[self.rightBody]
    self.grid[2][2] = self.rightReel.symbols[self.rightTail]

    # Display the updated grid
    self.displayGrid()
    self.updateMultiplierReel()

  def updateMultiplierReel(self):
    #update the multiplier reel in the fourth column
    self.grid[0][3] = self.multiplierReel.symbols[self.multHead]
    self.grid[1][3] = self.multiplierReel.symbols[self.multBody]
    self.grid[2][3] = self.multiplierReel.symbols[self.multTail]

  def displayGrid(self):
    for row in self.grid:
      symbols = []
      for symbol in row:
        symbols.append(symbol.__class__.__name__)
      
      print(symbols)
