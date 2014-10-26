#include <stdio.h>
#include <math.h>

/* How many continued fractions for N ≤ 10000 have an odd period? */

int isNotPerfectSquare(int n) {
    int h = n & 0xF;
    if (h > 9) {
        return 1;
    }
    if (h != 2 && h != 3 && h != 5 && h != 6 && h != 7 && h != 8) {
        int t = sqrt(n);
        return t*t != n;
    }
    return 1;
}

int contFracExp(int sq) {
    int period_length = 0;
    int a_0 = sqrt(sq);
    int m = 0, d = 1, a = a_0;
    while (a < 2*a_0) {
        m = d*a - m;
        d = (sq - m*m) / d;
        a = (a_0 + m) / d;
        ++period_length;
    }
    return period_length % 2;
}

int main() {
    int num_odd_periods = 4;
    for (int i = 14; i <= 10000; ++i) {
        if (isNotPerfectSquare(i)) {
            num_odd_periods += contFracExp(i);
        }
    }
    printf("%d\n", num_odd_periods);
}
