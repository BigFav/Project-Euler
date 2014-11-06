#include <algorithm>
#include <iostream>
#include <vector>
#define MAX 60

using namespace std;

/* How many chains, that start below a million, contain exactly sixty non-repeating terms? */

unsigned int digit_fac_sum(unsigned int n, int factorial[]) {
    unsigned int sum = 0;
    for (; n >= 10; n /= 10)
        sum += factorial[n % 10];
    return sum + factorial[n];
}

int main() {
    int sixty_cycle = 0;
    char steps_left[1000000];
    int factorial[10] = {1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880};
    for (unsigned int i = 1; i < 1000000; ++i) {
        vector<unsigned int> fac_cycle;
        fac_cycle.reserve(MAX);

        unsigned int digits = i;
        vector<unsigned int>::iterator in_cycle;
        do {
            fac_cycle.push_back(digits);
            digits = digit_fac_sum(digits, factorial);
            if (digits < i) {
                break;
            }
            in_cycle = find(fac_cycle.begin(), fac_cycle.end(), digits);
        } while (fac_cycle.size() < MAX && in_cycle == fac_cycle.end());

        if (digits < i) {
            steps_left[i] = steps_left[digits] + fac_cycle.size();
            if (steps_left[i] == MAX) {
                ++sixty_cycle;
            }
        } else {
            steps_left[i] = fac_cycle.size();
            if (in_cycle != fac_cycle.end() && fac_cycle.size() == MAX) {
                ++sixty_cycle;
            }
        }
    }
    cout << sixty_cycle << endl;
}
