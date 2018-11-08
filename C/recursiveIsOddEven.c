bool isEven(int input) {
    switch(input) {
        case 0:
            return true;
        case 1:
            return false;
        default:
            return isEven(input - 2);
    }
}

bool isOdd(int input) {
    return !isEven(input);
}