#include <stdio.h>

/* Find the 1st number whose number of integer partition is divisible by 1,000,000. */

static int memo[100000] = {[0 ... 1] = 1, [2] = 2, [3] = 3, [4 ... 99999] = -1};

int p(int n) { 
    if (n < 0) {
        return 0;
    }
    if (memo[n] != -1) {
        return memo[n];
    }
    
    int right_param, num_partitions = 0, k = 1;
    do {
        right_param = n - (k*(3*k + 1) >> 1);
        int right_side = p(right_param);
        int left_side = p(right_param + k);
        
        if (k++ % 2 == 0) {
            num_partitions -= left_side + right_side;
        } else {
            num_partitions += left_side + right_side;
        }
    } while (right_param > 0);
    
    /*for (int k = 1, right_param = 1; right_param > 0; ++k) {
        right_param = n - (k*(3*k + 1) >> 1);
        int right_side = p(right_param);
        int left_side = p(right_param + k);
        
        if (k % 2 == 0) {
            num_partitions -= left_side + right_side;
        } else {
            num_partitions += left_side + right_side;
        }
    }*/
    
    num_partitions %= 1000000;
    memo[n] = num_partitions;
    return num_partitions;
}

int main() {
    int i;
    for (i = 4; p(i) != 0; ++i);
    printf("%d\n", i);
}
