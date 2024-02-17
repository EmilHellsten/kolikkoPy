from grid import SlotGrid
import time

def playGame(rolls):
    #instantiate grid
    slotGrid = SlotGrid()
    i = 0

    #TESTING
    while i < rolls:
      slotGrid.displayGrid()
      #CLEAR TERMINAL AFTERWARDS
      print("")
      print("")
      print("")
      print("")
      print("")
      print("")
      print("")

      time.sleep(2)
      i +=1
    
playGame(15)
