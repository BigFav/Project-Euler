#include <stdio.h>
#define MAX_PERI 1000000000

/* Find the sum of the perimeters of all almost equilateral triangles
   with integral side lengths and area and whose perimeters do not
   exceed one billion (1,000,000,000). */

int main() {
    unsigned long peri_sums = 984;      // Sum of the first 4 perimeters
    unsigned long perimeter = 2704;     // Third in n+1 chain
    unsigned long side_length = 901;
    unsigned int old_old = 5, old = 65;
    while (perimeter <= MAX_PERI) {
        peri_sums += perimeter;
        old_old = old;
        old = side_length;

        side_length = 14*old - old_old - 4;
        perimeter = 3*side_length + 1;
    }

    perimeter = 10082;                  // Third in n-1 chain
    side_length = 3361;
    old_old = 17, old = 241;
    while (perimeter <= MAX_PERI) {
        peri_sums += perimeter;
        old_old = old;
        old = side_length;

        side_length = 14*old - old_old + 4;
        perimeter = 3*side_length - 1;
    }

    printf("%lu\n", peri_sums);
}
