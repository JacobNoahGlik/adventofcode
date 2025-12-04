import sys
import os

class Lock:
    def __init__(self, starting_value, max=99):
        self.max = max
        self.counter = 0
        self.value = starting_value
        self.zero_times = int(self.value == 0)
        # is zero?
        # True  -> int(True)  -> 1
        # False -> int(False) -> 0

    def rotate(self, right: bool, distance: int) -> None:
        if not right:
            distance *= -1
        self.value += distance
        if self.value < 0:
            self.value += self.max + 1
        elif self.value > self.max:
            self.value -= self.max + 1
        self.counter += 1

    def update(self, inp: str) -> None:
        if len(inp) < 2 or inp[0].lower() not in 'lr':
            return
        direction = inp[0].lower()
        self.rotate(direction == 'r', int(''.join([char for char in inp[1:].split('\n', 1)[0] if char in '1234567890'])))
        self.zero_times += int(self.value == 0)

    def consume(self, filename: str) -> None:
        if not os.path.exists(filename):
            print(f'Could not find "{filename}"')
            exit()
        with open(filename, 'r') as f:
            for line in f.read().split('\n'):
                old_val = self.value
                self.update(line)
                print(f' > "{line}": {old_val} -> {self.value}   ({self.counter})')

    def display_result(self) -> None:
        print(f'Lock value is {self.value}')
        print(f'It was 0 exactly {self.zero_times} times')


if len(sys.argv) != 3:
    print('USAGE: python3 <fname>.py <START_VALUE> <INPUT_FILE>')
    exit()

try:
    starting_value = int(sys.argv[1])
except:
    print(f"Could not convert {sys.argv[1]} to int")
    exit()

lock = Lock(starting_value)
lock.consume(sys.argv[2])

lock.display_result()
