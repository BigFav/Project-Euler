#include <numeric>
#include <vector>
#include <string>
#include <fstream>
#include <sstream>
#include <iostream>
#include <algorithm>
#include <unordered_set>

using namespace std;


/* Find the sum of special subset sums. */

int subset_len;
int *subsetSums;

void subsetSum(int numbers[], int length) {
    int i, j;
	int sum = 0;
	for (i = 0; i < length; ++i) {
		sum += numbers[i];
	}
	subset_len = sum + 1;
	
    int starts[subset_len];
	fill_n(starts, subset_len, length + 1);

	starts[0] = 0;
	for (i = 1; i <= subset_len; ++i) {
		for (j = 1; j <= length; ++j) {
			int k = i - numbers[j - 1];
			if (k >= 0 && starts[k] < j) {
				starts[i] = j;
				break;
			}
		}
	}

    subsetSums = new int[subset_len];
    copy(starts, starts + subset_len, subsetSums);
}


int main(void) {
    int sum_of_sums = 0;
    ifstream infile("p105_sets.txt");
    while (infile) {
        /* Read file */
        string s;
        if (!getline(infile, s)) {
            break;
        }
        istringstream ss(s);
        vector<int> numbers;
        numbers.reserve(15);
        while (ss) {
            string r;
            if (!getline(ss, r, ',')) {
                break;
            }
            numbers.push_back(stoi(r));
        }
        
        int i, j;
        int N = numbers.size();
        bool special_sub = true;
        int permMask = (1 << (N - 1));
        for (i = 1; i < permMask; ++i) {
            int B_sum = 0;
            unordered_set<int> B = unordered_set<int>();
            unordered_set<int> C = unordered_set<int>(begin(numbers), end(numbers));
            for (j = 0; j < N; ++j) {
                if ((i & (1 << j)) > 0) {
                   B_sum += numbers[j];
                   B.insert(numbers[j]);
                   C.erase(numbers[j]);
                }
            }

            int *set_c = new int[C.size()];
            copy(C.begin(), C.end(), set_c);
            subsetSum(set_c, C.size());
            if ((B_sum < subset_len) && (subsetSums[B_sum] != C.size() + 1)) {
                special_sub = false;
                break;
            }
            
            free(set_c);
            free(subsetSums);
        }

        if (special_sub) {
            sort(begin(numbers), end(numbers));
            for (i = 1; i <= (N >> 1); ++i) {
                int sum1 = 0, sum2 = 0;
                for (j = 0; j <= i; ++j) {
                    sum1 += numbers[j];
                }
                for (j = N-1; j >= N-i; --j) {
                    sum2 += numbers[j];
                }
                if (sum1 <= sum2) {
                    special_sub = false;
                    break;
                }
            }
        }

        if (special_sub) {
            sum_of_sums = accumulate(numbers.begin(), numbers.end(), sum_of_sums);
        }
    }
    cout << sum_of_sums << endl;
}
