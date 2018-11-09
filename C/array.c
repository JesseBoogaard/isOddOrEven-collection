bool isEven(int input) {
    bool results[10];

    results[0] = true;
    results[1] = false;
    results[2] = true;
    results[3] = false;
    results[4] = true;
    results[5] = false;
    results[6] = true;
    results[7] = false;
    results[8] = true;
    results[9] = false;

    int dec = input / 10;
    dec = dec * 10;
    int index = input - dec;

    return results[index];
}

bool isOdd(int input) {
    return !isEven(input);
}