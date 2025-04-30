import random


class RandomLooper:
    def __init__(self, *arg):
        self.arg = arg
        self.items = []
        for iterable in arg:
            self.items.extend(list(iterable))

        random.shuffle(self.items)
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.items):
            raise StopIteration

        item = self.items[self.index]
        self.index += 1
        return item


randomlooper = RandomLooper(['red', 'blue', 'green', 'purple'])

print(list(randomlooper))
print(list(randomlooper))

colors = ['red', 'blue', 'green', 'purple']
shapes = ['square', 'circle', 'triangle', 'octagon']
randomlooper = RandomLooper(colors, shapes)

print(list(randomlooper))
































print(chr(int("5350", 16)))
print(chr(int("5350", 16)))
print(chr(int("5350", 16)))
print(chr(int("5350", 16)))