class Counter:
    def __init__(self, start=0):
        self.start = start
        self.value = self.start

    def inc(self, num=True):
        if isinstance(num, bool):
            self.value += 1
        else:
            self.value += num

    def dec(self, num=True):
        if isinstance(num, bool):
            if (self.value - num) < 0:
                self.value = 0
            else:
                self.value -= 1
        else:
            if (self.value - num) < 0:
                self.value = 0
            else:
                self.value -= num


class DoubledCounter(Counter):
    def __init__(self, start=0):
        Counter.__init__(self, start=0)
        self.start = start
        self.value = self.start

    def inc(self, num=True):
        if isinstance(num, bool):
            self.value += 2
        else:
            self.value += num * 2

    def dec(self, num=True):
        if isinstance(num, bool):
            if (self.value - 2) < 0:
                self.value = 0
            else:
                self.value -= 2
        else:
            if (self.value - num * 2) < 0:
                self.value = 0
            else:
                self.value -= num * 2


print(issubclass(DoubledCounter, Counter))

counter = Counter(10)

print(counter.value)
counter.inc()
counter.inc(5)
print(counter.value)
counter.dec()
counter.dec(10)
print(counter.value)
counter.dec(10)
print(counter.value)
print()
counter = DoubledCounter(20)

print(counter.value)
counter.inc()
counter.inc(5)
print(counter.value)
counter.dec()
counter.dec(10)
print(counter.value)
counter.dec(10)
print(counter.value)
