#include <stdio.h>
#include <assert.h>

int isOdd(long num) {
    char s[2];

    num = num << sizeof(long) * 8 - 1;
    snprintf(s, 2, "%lf", (double)(*((double *)(&num))));
    return s[0] == '-';
}

int main () {
    for (int i = 0; i < 100; i++) {
        printf("%d %d\n", i, isOdd(i));
    }
}

