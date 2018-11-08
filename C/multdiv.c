bool isEven(int input) {
    int res = input / 2; // int division drops decimals
    res = res * 2; // if the number is even, res should be eq to input
    return res == input; // if it's odd it should be off by one
}

bool isOdd(int input) {
    return !isEven(input);
}