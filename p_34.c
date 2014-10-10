#include <stdio.h>

/* Find sum of factorians. */

int digit_fac_check(unsigned int n, int factorial[]) {
    unsigned int sum = 0;
    unsigned int n_copy = n;
    for (; n >= 10; n /= 10)
        sum += factorial[n % 10];
    return sum + factorial[n] == n_copy;
}

int main() {
    int sum = 0;
    int factorial[10] = {1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880};
    for (unsigned int i = 10; i < 100000000; ++i) {
        if (digit_fac_check(i, factorial))
            sum += i;
    }
    printf("%u\n", sum);
}
