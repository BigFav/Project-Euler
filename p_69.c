#include <stdio.h>

/* Find the value of n ≤ 1,000,000 for which n/φ(n) is a maximum. */

int main() {
    int top_n = 1;
    double top_div = 1.0;
    int phi[1000000] = {0 , 1};
    for (int i = 2; i < 1000000; ++i) {
        if (phi[i] == 0) {
            phi[i] = i - 1;
            for (int j = 2; j * i < 1000000; ++j) {
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
        double div = (double) i / phi[i];
        if (div > top_div) {
            top_div = div;
            top_n = i;
        }
    }
    printf("%d\n", top_n);
}
