#DiceRoll.py
#Name:
#Date:
#Assignment:
import random

def main():
  #Create an empty list with possible roll values
  rolls = [0,0,0,0,0,0,0,0,0,0,0,0]
  #Create two dice values ranging from 1 - 6 each
  for r in range(60000):
    dice1 = random.randint(1,6)
    rolls[dice1 - 1] = rolls[dice1 - 1] + 1
    dice2 = random.randint(1,6)
    rolls[dice2 + 5] = rolls[dice2 + 5] + 1
  #find the sum total of the two dice
  diceSum = dice1 + dice2
  #print statictics for dice rolls
  totalNumber = sum(rolls)
  diceSum = 1
  for count in rolls:
    percent = ((count)/(totalNumber))*100
    percent = round(percent, 1)
    print(diceSum, ":", count, ":", percent, "%")
    diceSum = diceSum + 1
  

if __name__ == '__main__':
  main()
