#include <iostream>
#include <vector>
#include <math.h>

using namespace std;


/* Find the sum of numbers that cannot be made of 2 abundant sums.  */

int proper_divisors_sum(unsigned int n) {
    int proper_divisors_sum = -n;
    for (int i = 1; i <= int(sqrt(n)); ++i) {
        if (n % i == 0) {
            proper_divisors_sum += i;
            if (i != n / i)
                proper_divisors_sum += (n / i);
        }
    }
    return proper_divisors_sum;
}

int abundant_sum_check(int num, vector<int> abundant_nums) {
    int head = 0;
    int tail = abundant_nums.size() - 1;
    while (head <= tail) {
        int result = abundant_nums[head] + abundant_nums[tail];
        if (result > num)
            --tail;
        else if (result < num)
            ++head;
        else
            return 0;
    }
    return num;
}

int main() {
    int non_abundant_sum = 1;
    vector<int> abundant_nums;
    abundant_nums.reserve(5000);
    for (unsigned int i = 2; i <= 20161; ++i) {
        non_abundant_sum += abundant_sum_check(i, abundant_nums);
        if (proper_divisors_sum(i) > i)
            abundant_nums.push_back(i);
    }
    cout << non_abundant_sum << endl;
}
