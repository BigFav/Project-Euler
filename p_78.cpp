#include <iostream>
#include <vector>

using namespace std;

/* Find the 1st number whose integer partition is divisible by 1,000,000. */

int p(int n, vector<int> &memo) {
    if (n < 0) {
        return 0;
    }
    if (n < memo.size()) {
        return memo[n];
    }

    int num_partitions = 0;
    for (int k = 1; k < n; ++k) {
        int right_param = n - (k*(3*k + 1) >> 1);
        int right_side = p(right_param, memo);
        int left_side = p(right_param + k, memo);

        if (k % 2 == 0) {
            num_partitions -= left_side + right_side;
        } else {
            num_partitions += left_side + right_side;
        }

        if (right_param <= 0) {
            break;
        }
    }

    num_partitions %= 1000000;
    memo.push_back(num_partitions);
    return num_partitions;
}

int main() {
    int base_cases[4] = {1, 1, 2, 3};
    vector<int> memo(base_cases, base_cases + 4);
    memo.reserve(500);

    int i;
    for (i = 4; p(i, memo) != 0; ++i);
    cout << i << ": " << memo[i] << endl;
}
