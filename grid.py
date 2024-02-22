from reels import LeftReel, MidReel, RightReel, MultiplierReel
from combos import validCombos

class SlotGrid:
  def __init__(self):
    #Whenever a new SlotGrid object is instantiated, spawn it in with three reels and one multiplier reel
    self.leftReel = LeftReel()
    self.midReel = MidReel()
    self.rightReel = RightReel()
    self.multReel = MultiplierReel()

    #Build grid out of reels
    self.grid = [
      [self.leftReel.symbolOne,   self.midReel.symbolOne,   self.rightReel.symbolOne,   self.multReel.symbolOne],
      [self.leftReel.symbolTwo,   self.midReel.symbolTwo,   self.rightReel.symbolTwo,   self.multReel.symbolTwo],
      [self.leftReel.symbolThree, self.midReel.symbolThree, self.rightReel.symbolThree, self.multReel.symbolThree]
    ]
  
    #Lines
    self.lineOne   = [self.grid[0][0], self.grid[1][1], self.grid[2][2]]#Diagonally downward
    self.lineTwo   = [self.grid[0][0], self.grid[0][1], self.grid[0][2]]#Straight across top
    self.lineThree = [self.grid[1][0], self.grid[1][1], self.grid[1][2]]#Straight across mid
    self.lineFour  = [self.grid[2][0], self.grid[2][1], self.grid[2][2]]#Straight across bot
    self.lineFive  = [self.grid[2][0], self.grid[1][1], self.grid[0][2]]#Diagonally upwards

    #Multiplier Value
    #TODO: Implement multiplier reel after a winning spin
    self.multiplier = self.multReel.symbolTwo


  def checkLines(self, playerMoney):#TODO refactor into helper methods
    winningLines = []
    #Iterate over each of the lines
    for line in [self.lineOne, self.lineTwo, self.lineThree, self.lineFour, self.lineFive]:
        for combo, value in validCombos:#For each line, check ALL combos
            matchCount = 0
            #How many symbols in given line match up with symbols in combination
            for symbol, comboSymbol in zip(line, combo):
                if comboSymbol == 'Symbol' or symbol == comboSymbol:
                    matchCount += 1# ^ Special case for 'Symbol'

                if matchCount == 3:#If three matches are found it means that it was a winning line
                    winningLines.append([line, value])
                    break #

            if matchCount == 3:
                break  #If combo found, move on to next iteration

    if winningLines:#Check that winning lines contains something, if yes -> happy, if no -> unhappy path
        print(f"Winning lines: {winningLines}")
    else:
        print("No winning lines detected.")

    return sum(value for _, value in winningLines)#TODO: Shouldnt be the sum of winning lines, should be max(_, value)*size(winningLines)

  def printGrid(self):
    for row in self.grid:
      print(row)