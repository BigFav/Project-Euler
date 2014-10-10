#include <stdio.h>

/* Find number that is triangular, pentagonal, and hexagonal. */

unsigned long pentagonal(unsigned int n) {
    return n*((3*n - 1) >> 1);
}

unsigned long hexagonal(unsigned int n) {
    return n*((n << 1) - 1);
}

int main() {
    /* Can ignore triangular since all hexagonals are triangular. */
    unsigned long p_n = 166;
    unsigned long h_n = 144;

    unsigned long p = pentagonal(p_n);
    unsigned long h = hexagonal(h_n);
    while (p != h) {
        while (h > p) {
            p = pentagonal(++p_n);
        }

        if (h != p) {
            h = hexagonal(++h_n);
        }
    }
    printf("%lu\n", p);
}
