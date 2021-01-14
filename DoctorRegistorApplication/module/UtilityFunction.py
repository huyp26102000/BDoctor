import time
from datetime import datetime, date
import random

def getRandomText():
    now = datetime.now()
    today = date.today()
    current_time = now.strftime("%Ho%Mo%S")
    current_date = today.strftime("%mo%do%y")
    randomNumber = int(random.random()*100000000)
    randomText = str(current_date)+'o'+str(current_time)+'o'+str(randomNumber)
    return randomText