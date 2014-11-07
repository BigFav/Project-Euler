#include <stdio.h>
#include <stdbool.h>
#define SQ(x) ((x)*(x))

/* Find the integer whose square has the form 1_2_3_4_5_6_7_8_9_0, where each "_" is any number. */

bool isntProperFormat(long long num) {
    for (int i = 9; i >= 1; --i, num /= 100) {
        if (i != num % 10) {
            return true;
        }
    }
    return false;
}

int main() {
    long long num = 1389026620;  // int(sqrt(1929394959697989990)) rounded to lower 10
    for (; isntProperFormat(SQ(num) / 100); num -= 10);
    printf("%lld\n", num);
}
