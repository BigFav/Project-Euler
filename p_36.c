#include <stdio.h>

/* Find sum of numbers that are palindrones in base 10 and base 2. */

int getBit(unsigned int num, int index) {
    return ((1 << index) & num) != 0;
}

int isBinPalindrome(unsigned int num) {
    int first_one;
    for (int i = 19; 1; --i) {
        if (getBit(num, i)) {
            first_one = i;
            break;
        }
    }
    for (int i = first_one, j = 0; i > j; --i, ++j) {
        if (getBit(num, i) ^ getBit(num, j)) {
            return 0;
        }
    }
    return 1;
}

int isTenPalindrome(unsigned int x) {
    if (x < 0)
        return 0;
    
    unsigned int div = 1;
    while (x / div >= 10) {
        div *= 10;
    }
    while (x) {
        unsigned int l = x / div;
        unsigned int r = x % 10;
        if (l != r)
            return 0;
        x = (x % div) / 10;
        div /= 100;
    }
    return 1;
}

int main() {
    unsigned int sum = 1;
    for (unsigned int i = 2; i < 1000000; ++i) {
        if (isBinPalindrome(i) && isTenPalindrome(i)) {
            sum += i;
        }
    }
    printf("%u\n", sum);
}
