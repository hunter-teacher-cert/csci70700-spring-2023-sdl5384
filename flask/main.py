import random
from flask import Flask
from flask import render_template

app = Flask(__name__)

def roll(givenNumberOfSides):
  dice = []
  for i in range(0,random.randint(1,10)):
    dice.append(random.randint(1,givenNumberOfSides))

  return dice

def generateDiceMessageString(diceArray):
  msg = 'The numbers rolled after rolling ' + str(len(diceArray)) + ' are: '
  for j in range(0,len(diceArray)):
    msg = msg + str(diceArray[j]) + ', '
  return msg

def average(diceArray):
  sum = 0
  for k in range(0,len(diceArray)):
    sum = sum + diceArray[k]

  return sum/len(diceArray)

def standardDeviation():
  return None

@app.route('/')
def index():
    return 'Hello from Flask!'

@app.route('/gameAnalysis/')
def analysisPage():
  dice = []
  dice = roll(20)
  msg = generateDiceMessageString(dice)
  return msg

app.run(host='0.0.0.0', port=81)

@app.route('/monopolyDice/')
def monopolyDiceStats():
  render_template('dice_statistics.html')
  return None
