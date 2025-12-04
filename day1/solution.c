#include <stdio.h>

int main() {
    int position = 50, zero_count = 0, value;
    char direction;
    while (scanf(" %c%d", &direction, &value) != EOF) {
        position = (direction == 'L' ? (position - value + 100) : (position + value)) % 100;
        if (position == 0) zero_count++;
    }
    printf("%d\n", zero_count);
    return 0;
}
