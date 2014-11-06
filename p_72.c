#include <stdio.h>

/* Find the cardinality of the set of reduced proper fractions for d ≤ 1,000,000. */

int main() {
    unsigned long s = 0;
    int phi[1000001] = {0 , 1};
    for (int i = 2; i <= 1000000; ++i) {
        if (phi[i] == 0) {
            phi[i] = i - 1;
            for (int j = 2; j * i <= 1000000; ++j) {
                if (phi[j] != 0) {
                    int q = j;
                    int f = i - 1;
                    while (q % i == 0) {
                        f *= i;
                        q /= i;
                    }
                    phi[i*j] = f * phi[q];
                }
            }
        }
        s += phi[i];
    }
    printf("%lu\n", s);
}
