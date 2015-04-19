# See about Fizz buzz game in here, http://en.wikipedia.org/wiki/Fizz_buzz

import time

#Whether to print each row result in iteration on not
printRounds = False

#Get time in milliseconds
def currMillTime():
    return round(time.time() * 1000)

#Run rounds
def doRun(amount, printRounds):
    start = currMillTime()
    for x in range(1, amount + 1):
        string = ""
        if x % 3 == 0:
            string = "Fizz"
        if x % 5 == 0:
            string = string + "Buzz"
        if string == "":
            string = x
        if printRounds:
            print(string)
    end = currMillTime()
    print(getResultString(start, end, amount))

#Get result string to print after rounds are iterated
def getResultString(start, end, amount):
    duration = end - start
    return "It took " + str(duration) + " milliseconds to run " + str(amount) + " rounds in Fizz buzz game."

#Run game with different amounts of rounds
amount = 10
while (amount <= 10000000):
    doRun(amount, printRounds)
    amount = amount * 10
