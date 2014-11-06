#include <stdio.h>

/* Find the first four consecutive integers to have four distinct prime factors. */

int four_prime_factors(int n) {
    int num_primes = 0;
    for (int d = 2; d*d <= n; ++d) {
        int is_fac = ((n % d) == 0) ? 1 : 0;
        for (int is_fac = 0; (n % d) == 0; n /= d);
        if (is_fac) {
            num_primes += 1;
        }
    }
    if (n > 1) {
        num_primes += 1;
    }
    return num_primes > 3;
}

int main() {
    int first = 644;
    while (1) {
        while (!four_prime_factors(first)) {
            first += 1;
        }

        if (!four_prime_factors(first+1)) {
            first += 2;
            continue;
        }
        if (!four_prime_factors(first+2)) {
            first += 3;
            continue;
        }
        if (!four_prime_factors(first+3)) {
            first += 4;
            continue;
        }
        break;
    }
    printf("%d\n", first);
}
