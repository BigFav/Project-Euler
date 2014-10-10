#include <stdio.h>
#define abs(x) ((x) < 0 ? (-x) : (x))

/* Find area of grid whose number of embedded rectangles is closest to 2,000,000. */

int main() {
    int area;
    int sum = 0;
    int closest_diff = 5000000;
    for (int n = 1, k = 2000; n <= k; (sum < 2000000) ? ++n : --k) {
        sum = (n*(n+1) * k*(k+1)) >> 2;
        int diff = abs((sum - 2000000));
        if (diff < closest_diff) {
            closest_diff = diff;
            area = k*n;
        }
    }
    printf("%d %d\n", area, closest_diff);
}
