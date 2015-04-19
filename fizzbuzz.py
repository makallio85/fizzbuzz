# See about Fizz buzz in here, http://en.wikipedia.org/wiki/Fizz_buzz

def doRun():
    for x in range(1, 101):
        string = ""
        if x % 3 == 0:
            string = "Fizz"
        if x % 5 == 0:
            string = string + "Buzz"
        if string == "":
            string = x
        print(string)
doRun()
