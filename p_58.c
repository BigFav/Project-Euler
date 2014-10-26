#include <math.h>
#include <stdio.h>

/* What is the side length of the Ulam spiral for which the ratio of primes along both diagonals falls below 10%? */

int isPrime(long long n) {
    if (n % 2 == 0 || n % 3 == 0)
        return 0;
    for (int i = 5; i < (long)sqrt(n) + 1; i += 6) {
        if (n % i == 0 || n % (i + 2) == 0)
            return 0;
    }
    return 1;
}

int main() {
    long long num_diags = 5;
    long long curr_diag = 3;
    long long num_primes = 3;
    unsigned int side_length = 3;
    while ((float)num_primes / num_diags > 0.1) {
        long long first_diag = curr_diag + 3*(side_length-1) + side_length + 1;
        side_length += 2;

        unsigned int diag_gap = side_length - 1;
        num_primes += isPrime(first_diag);
        num_primes += isPrime(first_diag + diag_gap);
        num_primes += isPrime(first_diag + 2*diag_gap);
        num_primes += isPrime(first_diag + 3*diag_gap);

        num_diags += 4;
        curr_diag = first_diag;
    }
    printf("%u\n", side_length);
}
