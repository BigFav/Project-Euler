#include <stdio.h>
#include <math.h>
#include <stdint.h>
#include <inttypes.h>
#define abs(x) ((x) < 0 ? (-(x)) : (x))


int isPerfectSquare(int n) {
    int h = n & 0xF;  // h is the last hex "digit"
    if (h > 9)
        return 0;

    if (h != 2 && h != 3 && h != 5 && h != 6 && h != 7 && h != 8) {
        int t = (int) floor(sqrt((double) n) + 0.5);
        return t*t == n;
    }
    return 0;
}

intmax_t chakravala(int N) {
    intmax_t a = round(sqrt(N));
    intmax_t b = 1;
    intmax_t k = a*a - N;
    while (a*a - N*b*b != 1) {    
        intmax_t abs_k = abs(k);
        intmax_t og_m = 1;
        if (N == 181)
            printf("YOLO %lld ", b);
        for (; (a + b*og_m) % abs_k; ++og_m);
        if (N == 181)
            puts("Swag");
        
        int t = 2;
        intmax_t m = og_m;
        intmax_t next_m = abs_k + og_m;
        while ((uintmax_t)abs((m*m - N)) > (uintmax_t)abs((next_m*next_m - N))) {
            m = next_m;
            next_m = abs_k*t + og_m;
            ++t;
        }
        
        intmax_t tmp_a = a;
        a = (a*m + N*b) / abs_k;
        b = (tmp_a + b*m) / abs_k;
        k = (m*m - N) / k;
    }
    return a;
}

int main() {
    int max_D = 0;
    intmax_t max_a = 0;
    for (int i = 61; i <= 1000; ++i) {
        if (!isPerfectSquare(i)) {
            intmax_t a = chakravala(i);
            if (a > max_a) {
                max_a = a;
                max_D = i;
            }
        }
    }
    printf("%d: %lld\n", max_D, max_a);
}
