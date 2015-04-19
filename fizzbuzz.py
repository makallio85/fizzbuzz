# See about Fizz buzz game in here, http://en.wikipedia.org/wiki/Fizz_buzz

import time

# Whether to print each row result in iteration on not
printRounds = False

# Starting rounds amount for game
amount = 10

# Get time in milliseconds
def curr_mill_time():
    return round(time.time() * 1000)

# Run game
def do_run(amount, printRounds):
    start = curr_mill_time()
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
    end = curr_mill_time()
    print(get_result_string(start, end, amount))

# Get result string to print after rounds are iterated
def get_result_string(start, end, amount):
    duration = end - start
    return "It took {} milliseconds to run {} rounds in Fizz buzz game.".format(duration, amount)

# Run game with different round amounts
while (amount <= 10000000):
    do_run(amount, printRounds)
    amount = amount * 10
