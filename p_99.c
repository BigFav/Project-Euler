#include <math.h>
#include <stdio.h>
#include <string.h>

/* Determine the line number which has the greatest exponent/base value. */

int main() {
    char line[20];
    int max_line;
    double max_value;
    FILE *fr = fopen("p099_base_exp.txt", "rt");
    for (int i = 1; fgets(line, 20, fr) != NULL; ++i) {
        int base, exponent;
        sscanf(strtok(line, ","), "%d", &base);
        sscanf(strtok(NULL, ","), "%d", &exponent);

        double value = exponent * log2(base);
        if (value > max_value) {
            max_value = value;
            max_line = i;
        }
    }
    fclose(fr);
    printf("%d\n", max_line);
}
