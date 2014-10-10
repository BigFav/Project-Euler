#include <stdio.h>
#define abs(x) ((x) < 0 ? (-(x)) : (x))

/* Find area of grid whose number of embedded rectangles is closest to 2,000,000. */

int main() {
    int area;
    int sum = 0;
    int closest_diff = 5000000;

    int n = 1, k = 2000;
    unsigned int n_sq = 2;
    unsigned int k_sq = 2000*2001;
    while (n <= k) {
        sum = (n_sq * k_sq) >> 2;
        int diff = abs(sum - 2000000);
        if (diff < closest_diff) {
            closest_diff = diff;
            area = k*n;
        }
        if (sum < 2000000) {
            n_sq = (++n)*(n+1);
        } else {
            k_sq = (--k)*(k+1);
        }
    }
    printf("Area: %d, Closest Diff: %d\n", area, closest_diff);
}
