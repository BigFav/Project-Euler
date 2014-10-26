#include <math.h>
#include <stdio.h>

/* Find the minimised difference of 2 pentagonal numbers whose sum and difference are also pentagonal. */

unsigned long pentagonal(unsigned int n) {
    return n * (3*n - 1) / 2;
}

int isPentagonal(unsigned long n) {
    long double isPentCheck = (1 + sqrt(24*n + 1)) / 6;
    return isPentCheck == (int)isPentCheck;
}

int main() {
    for (unsigned int x = 1; 1; ++x) {
        unsigned long pentX = pentagonal(x);
        for (unsigned int y = x+1; y < 10000; ++y) {
            unsigned long pentY = pentagonal(y);
            unsigned long difference = pentY - pentX;
            if (isPentagonal(difference) && isPentagonal(pentY + pentX)) {
                printf("%lu\n", difference);
                return 0;
            }
        }
    }
}
