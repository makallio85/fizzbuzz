<?php

//See about Fizz buzz game in here, http://en.wikipedia.org/wiki/Fizz_buzz

//Whether to print each row result in iteration on not
$printRounds = false;

//Starting rounds amount for game
$amount = 10;

//Get time in milliseconds
function currMillTime()
{
    return round(microtime(true) * 1000);
}

//Run game
function doRun($amount, $printRounds)
{
    $start = currMillTime();
    for ($x = 1; $x < $amount + 1; $x++) {
        $string = "";
        if ($x % 3 == 0) {
            $string = "Fizz";
        }
        if ($x % 5 == 0) {
            $string .= "Buzz";
        }
        if ($string == "") {
            $string = $x;
        }
        if ($printRounds) {
            echo $string."\n";
        }
    }
    $end = currMillTime();
    echo getResultString($start, $end, $amount)."\n";
}
#Get result string to print after rounds are iterated
function getResultString($start, $end, $amount)
{
    $duration = $end - $start;

    return "It took $duration milliseconds to run $amount rounds in Fizz buzz game.";
}

#Run game with different round amounts
while ($amount <= 10000000) {
    doRun($amount, $printRounds);
    $amount *= 10;
}
