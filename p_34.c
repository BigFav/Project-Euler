#include <stdio.h>

/* Find sum of factorians. */

int digit_fac_check(unsigned int n, unsigned int factorial[]) {
    unsigned long long sum = 0;
    unsigned long long n_copy = n;
    for (; n >= 10; n /= 10)
        sum += factorial[n % 10];
    return sum + factorial[n] == n_copy;
}

int main() {
    unsigned int sum = 0;
    unsigned int factorial[10] = {1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880};
    for (unsigned int i = 10; i < 100000000; ++i) {
        if (digit_fac_check(i, factorial))
            sum += i;
    }
    printf("%u\n", sum);
}
