#include <iostream>
#include <vector>

using namespace std;

/* Find the sum of numbers that cannot be made of 2 abundant sums. */

int abundant_sum_check(int num, vector<int> abundant_nums) {
    vector<int>::iterator head = abundant_nums.begin();
    vector<int>::reverse_iterator tail = abundant_nums.rbegin();

    /* abundant_nums will always be sorted, thus a linear search. */
    while (head <= (tail + 1).base()) {
        int result = *head + *tail;
        if (result > num) {
            ++tail;
        } else if (result < num) {
            ++head;
        } else {
            return 0;
        }
    }
    return num;
}

int main() {
    unsigned int non_abundant_sum = 20239;
    vector<int> abundant_nums;
    abundant_nums.reserve(5000);
    abundant_nums.push_back(12);

    int proper_divisors_sums[20161];
    for (int i = 1; i <= 10081; ++i) {
        for (int j = 2*i; j <= 20161; j += i) {
            proper_divisors_sums[j] += i;
        }
    }

    for (int i = 13; i < 20161; ++i) {
        non_abundant_sum += abundant_sum_check(i, abundant_nums);
        if (proper_divisors_sums[i] > i) {
            abundant_nums.push_back(i);
        }
    }
    cout << non_abundant_sum << endl;
}
