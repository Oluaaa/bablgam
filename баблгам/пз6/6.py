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
            self.value -= 1
        else:
            if (self.value - num) < 0:
                self.value = 0
            else:
                self.value -= num


class NonDecCounter(Counter):
    def dec(self, num=10):
        Counter.__init__(self, start=self.value)
        pass


class LimitedCounter(Counter):
    def __init__(self, start=0, limit=10):
        self.start = start
        self.limit = limit
        self.value = self.start
        Counter.__init__(self, start=self.value)

    def inc(self, num=True):
        if isinstance(num, bool):
            if (self.value + 1) > self.limit:
                self.value += 0
            else:
                self.value += 1
        else:
            if (self.value + num) > self.limit:
                self.value = self.limit
            else:
                self.value += num


counter = LimitedCounter()

print(counter.value)
counter.inc()
counter.inc(4)
print(counter.value)
counter.dec()
counter.dec(2)
print(counter.value)
counter.inc(20)
print(counter.value)
