from grid import SlotGrid
#Control variables
MAX_SPINS = 10000
STARTING_CAPITAL = 10.0
COST_PER_SPIN = 1.0

playerMoney = STARTING_CAPITAL

def clearTerminal():
  for i in range(0, 5):
    print("")

for num in range(0, MAX_SPINS):
  grid = SlotGrid()
  #On each spin, pay to spin slot machine
  playerMoney -= COST_PER_SPIN
  print(f"Player has {playerMoney} money left")
  #Check for win and add that to players money
  totalWinnings = grid.checkLines(playerMoney)
  playerMoney += totalWinnings
  grid.printGrid()
  print(f"Player's money after spin {num + 1}: {playerMoney}")
  clearTerminal()
