#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

/* Find n, 1 < n < 10^7, with the minimal n/φ(n) ratio, for which φ(n) is a permutation of n. */

bool same_digits(int phi_num, int index_num) {
    char digits[10] = {0};
    while (phi_num) {
        ++digits[phi_num % 10];
        phi_num /= 10;
    }

    while (index_num) {
        if (digits[index_num % 10] == 0) {
            return false;
        }
        --digits[index_num % 10];
        index_num /= 10;
    }
    return true;
}

int main() {
    int num = 2;
    double min_ratio = 2.0;
    int *phi = calloc(10000000, sizeof(int));

    phi[1] = 1;
    for (int i = 2; i < 10000000; ++i) {
        if (phi[i] == 0) {
            phi[i] = i - 1;     // Can't be a permutation

            for (int j = 2; j * i < 10000000; ++j) {
                if (phi[j] != 0) {
                    int q = j;
                    int f = i - 1;
                    while (q % i == 0) {
                        f *= i;
                        q /= i;
                    }
                    int index = i * j;
                    phi[index] = f * phi[q];

                    double ratio = (double)index / phi[index];
                    if (ratio < min_ratio && same_digits(index, phi[index])) {
                        num = index;
                        min_ratio = ratio;
                    }
                }
            }
        }
    }
    free(phi);
    printf("%d\n", num);
}
