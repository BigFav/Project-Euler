#include <stdio.h>
#include <stdlib.h>
#include <primesieve.h>

/* How many numbers below 50 million can be expressed as
   the sum of a prime square, prime cube, and prime fourth power? */

unsigned int SQ (int x) { return x*x; }
unsigned int CUBE (int x) { return x*x*x; }
unsigned int FOURTH (int x) { return x*x*x*x; }

int main() {
    unsigned int sum;
    char *sums = malloc(50000000*sizeof(char));

    size_t size;
    short *primes = (short *)primesieve_generate_primes(2, 7772, &size, SHORT_PRIMES);

    unsigned int sq = 0;
    do {
        unsigned int cube = 0;
        do {
            unsigned int fourth = 0;
            sum = SQ(primes[sq]) + CUBE(primes[cube]) + FOURTH(primes[fourth]);
            while (sum < 50000000) {
                sums[sum] = 1;
                sum = SQ(primes[sq]) + CUBE(primes[cube]) + FOURTH(primes[++fourth]);
            }
        } while (SQ(primes[sq]) + CUBE(primes[++cube]) + 16 < 50000000);
    } while (SQ(primes[++sq]) + 24 < 50000000);
    primesieve_free(primes);

    unsigned int numbers = 0;
    for (sum = 1; sum < 50000000; ++sum) {
        numbers += sums[sum];
    }
    free(sums);
    printf("%u\n", numbers);
}
