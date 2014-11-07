#include <stdbool.h>
#include <stdio.h>

/* Find number Lychrel numbers are there below 10,000. */

unsigned long reverseNumber(unsigned long num) {
    unsigned long reverse = 0;
    while (num != 0) {
        reverse *= 10;
        reverse += num % 10;
        num /= 10;
    }
    return reverse;
}

bool isPalindrome(unsigned long x) {
    if (x < 0)
        return false;

    unsigned long div = 1;
    while (x / div >= 10) {
        div *= 10;
    }
    while (x != 0) {
        unsigned long l = x / div;
        unsigned long r = x % 10;
        if (l != r)
            return false;
        x = (x % div) / 10;
        div /= 100;
    }
    return true;
}

int main() {
    int lychrel_num = 10000;
    for (int i = 0; i < 10000; ++i) {
        unsigned long num = i;
        for (int j = 0; j < 50; ++j) {
            unsigned long reverse = reverseNumber(num);
            unsigned long sum = num + reverse;
            if (isPalindrome(sum)) {
                --lychrel_num;
                break;
            } else {
                num = sum;
            }
        }
    }
    printf("%d\n", lychrel_num);
}
