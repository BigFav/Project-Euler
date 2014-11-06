#include <algorithm>
#include <iostream>
#include <vector>

using namespace std;


int digit_sq_sum(int n, char squares[]) {
    int sum = 0;
    for (; n >= 10; n /= 10) {
        sum += squares[n % 10];
    }
    return sum + squares[n];
}

int main() {
    char squares[10] = {0, 1, 4, 9, 16, 25, 36, 49, 64, 81};
    char *end_stop = new char[10000000];

    /* Fill in all "permutations" of 1s. */
    for (int i = 1; i < 10000000; i *= 10) {
        end_stop[i] = 1;
    }

    /* Fill in all permutations of 89s. */
    char start_int[7] = {0, 0, 0, 0, 0, 8, 9};
    do {
        int result = (((((((start_int[0])*10+start_int[1])*10+
                            start_int[2])*10+start_int[3])*10+
                            start_int[4])*10+start_int[5])*10+start_int[6]);
        end_stop[result] = 89;
    } while (next_permutation(start_int, start_int+7));

    int eightyNines = 0;
    for (int i = 2; i < 10000000; ++i) {
        if (end_stop[i] == 0) {
            int digits = i;
            vector<int> sq_digits_cycle;
            while (end_stop[digits] == 0) {
                sq_digits_cycle.push_back(digits);
                digits = digit_sq_sum(digits, squares);
            }

            /* Fill in all perms of all nums in current chain. */
            for (int &num : sq_digits_cycle) {
                for (int i = 6; i >= 0; --i) {
                    start_int[i] = num % 10;
                    num /= 10;
                }
                do {
                    int result = (((((((start_int[0])*10+start_int[1])*10+
                                        start_int[2])*10+start_int[3])*10+
                                        start_int[4])*10+start_int[5])*10+
                                        start_int[6]);
                    end_stop[result] = end_stop[digits];
                } while (next_permutation(start_int, start_int+7));
            }
        }
        if (end_stop[i] == 89) {
            ++eightyNines;
        }
    }

    delete[] end_stop;
    cout << eightyNines << endl;
}
