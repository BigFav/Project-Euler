#include <algorithm>
#include <iostream>
#include <vector>
#define MAX 1000000

using namespace std;

/* Find the smallest member of the longest amicable chain with no element exceeding one million. */

int main() {
    int min_value;
    int longest_len = 1;
    bool prev_seen[MAX+1] = {false};

    int proper_divisors_sums[MAX+1];
    for (int i = 1; i <= MAX/2 + 1; ++i) {
        for (int j = 2*i; j <= MAX; j += i) {
            proper_divisors_sums[j] += i;
        }
        if (proper_divisors_sums[i] <= 1) {
            prev_seen[i] = true;
        }
    }

    for (int i = 6; i <= MAX; ++i) {
        if (!prev_seen[i]) {
            int div_sum = i;
            vector<int> ami_cycle;
            do {
                prev_seen[div_sum] = true;
                ami_cycle.push_back(div_sum);
                div_sum = proper_divisors_sums[div_sum];
            } while (div_sum > 1 && div_sum <= MAX && !prev_seen[div_sum]);

            if (div_sum <= 1 || div_sum > MAX) {
                continue;
            }

            vector<int>::iterator in_cycle;
            in_cycle = find(ami_cycle.begin(), ami_cycle.end(), div_sum);
            if (in_cycle != ami_cycle.end()) {
                prev_seen[div_sum] = true;
                if (div_sum == i && ami_cycle.size() > longest_len) {
                    min_value = i;
                    longest_len = ami_cycle.size();
                } else {
                    int cycle_min_value = *min_element(in_cycle, ami_cycle.end());
                    int curr_cycle_len = ami_cycle.size() -
                                            distance(ami_cycle.begin(), in_cycle);
                    if (curr_cycle_len > longest_len) {
                        min_value = cycle_min_value;
                        longest_len = curr_cycle_len;
                    }
                }
            }
        }
    }
    cout << min_value << endl;
}
