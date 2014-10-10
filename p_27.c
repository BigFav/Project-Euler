#include <stdio.h>
#define abs(x) ((x) < 0 ? (-(x)) : (x))

int main() {
    // Hopefully I don't have to go through the other Heegner num derivatives
    int a = 1000, b = 1000;
    for (int i = 40; (abs(a) >= 1000) || (abs(b) >= 1000); --i) {
        a = -2*i - 1;
        b = i*i + i + 41;
    }
    printf("%d\n", a*b);
}
