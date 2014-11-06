#include <stdio.h>
#include <math.h>

/* Find the lowest M, max for any dimension of the cuboid, such that the minimal
   route from one corner to the other, along the surface, is an int. */

int main() {
    int num_min_dist_int = 0;
    int length, height, width, w_plus_h;
    for (length = 1; num_min_dist_int <= 1000000; ++length) {
        unsigned int length_sq = length*length;
        for (width = 1; width <= length; ++width) {
            for (height = 1; height <= width; ++height) {
                unsigned int w_plus_h = width + height;
                double shortest_dist = sqrt(length_sq + w_plus_h*w_plus_h);
                if (((int)shortest_dist) == shortest_dist) {
                    ++num_min_dist_int;
                }
            }
        }
    }
    printf("%d\n", length-1);
}
