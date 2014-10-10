#include <stdio.h>
#define abs(x) ((x) < 0 ? (-(x)) : (x))

int main() {
    // Hopefully I don't have to go through the other Heegner num derivatives
    int p = 41;
    int high_prod = 0;
    for (int i = p - 1; high_prod == 0; --i) {   // (n-i)^2 + (n-i) + p
        int a = -2*i - 1;
        int b = i*i + i + p;

        if ((abs(a) < 1000) && (abs(b) < 1000)) {
            high_prod = a * b;
        }
    }
    printf("%d\n", high_prod);
}
