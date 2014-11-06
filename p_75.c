#include <stdio.h>
#include <math.h>
#define P 1500000

/* How many perimiter values ≤ 1,500,000 can exactly one integer sided right angle triangle be formed? */

long ggt(long a, long b) {
    if (b==0) return a;
    if (a==0) return b;
    return ggt(b, a % b);
}

int main() {
    int s = 0;
    int erg[P/2] = {0};
    for (int u = 2; u <= sqrt(P/2) + 1; ++u) {
        for (int v = 1; v < u; ++v) {
            if ((u+v) % 2 == 1 && ggt(u,v) == 1){
                s = u * (u+v);
                for (int i=1; s*i <= P/2; ++i) {
                    ++erg[s*i];
                }
            }
        }
    }

    s = 0;
    for (int i = 0; i < P/2; i++) {
        if(erg[i] == 1){
            ++s;
        }
    }
    printf("%d\n", s);
}
