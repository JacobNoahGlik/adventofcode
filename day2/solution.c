#include <stdio.h>

int main() {
    int position = 50, zeroCount = 0, value; char direction;
    while (scanf(" %c%d", &direction, &value) != EOF) {
        for (int i = 0; i < value; i++) position = (direction == 'L' ? (position - 1 + 100) : (position + 1)) % 100, zeroCount += (position == 0);
    }
    printf("%d\n", zeroCount);
    return 0;
}
