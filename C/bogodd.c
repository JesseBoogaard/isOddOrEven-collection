#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int isOdd(unsigned char num) {
    while (1) {
        unsigned char t = (rand() % (1 << sizeof(char) * 8 - 1)) * 2;
        if (num == t) return 0;
        if (num == t + 1) return 1;
    }
}

int main() {
    srand(time(0));

    for (unsigned char i = 0; i < 100; i++) {
        printf("%d %d\n", i, isOdd(i));
    }

    return 0;
}
