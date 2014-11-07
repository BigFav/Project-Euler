#include <math.h>
#include <stdio.h>
#include <stdbool.h>

/* Find the least number for which the proportion of bouncy numbers is exactly 99%. */

bool allSame(int num) {
    int digit = num % 10;
    num /= 10;
    while (num) {
        if (digit != num % 10) {
            return false;
        }
        num /= 10;
    }
    return true;
}

int reverseNumber(int num) {
    int reverse = 0;
    while (num) {
        reverse *= 10;
        reverse += num % 10;
        num /= 10;
    }
    return reverse;
}

int is_bouncy(int num, int trunc_amt) {
    int a = num % 10;
    num /= 10;
    while (num && num % 10 == a) {
        num /= 10;
    }

    if (num) {
        int isDecreasing = num % 10 > a;
        a = num % 10;
        num /= 10;
        if (isDecreasing) {
            for (; num; num /= 10) {
                if (num % 10 < a) {
                    return (int)pow(10, (int)log10(num) + trunc_amt);
                }
                a = num % 10;
            }
            if (trunc_amt) {
                return (int)pow(10, trunc_amt-1);
            }
        } else {
            for (; num; num /= 10) {
                if (num % 10 > a) {
                    return (int)pow(10, (int)log10(num) + trunc_amt);
                }
                a = num % 10;
            }
        }
    }
    return 0;
}

int main() {
    int bouncy_incr;
    int num_bouncy = 19822;
    int overall_nums = 22000;
    for (; (double)num_bouncy / overall_nums != 0.99; overall_nums += (bouncy_incr == 0) ? 1 : bouncy_incr) {
        if (allSame(overall_nums / 10)) {
            bouncy_incr = 10;
            continue;
        }

        int reverse = reverseNumber(overall_nums);
        bouncy_incr = is_bouncy(reverse, (int)log10(overall_nums) - (int)log10(reverse));
        if (bouncy_incr) {
            num_bouncy += bouncy_incr;
        }
    }
    printf("%d / %d\n", num_bouncy, overall_nums);
}
