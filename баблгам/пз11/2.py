class MinStat:
    def __init__(self, iterable=[]):
        self.iterable = iterable

    def add(self, num):
        self.iterable.append(num)

    def result(self):
        if not (len(self.iterable) == 0):
            return min(self.iterable)
        return None

    def clear(self):
        self.iterable.clear()


class MaxStat:
    def __init__(self, iterable=[]):
        self.iterable = iterable

    def add(self, num):
        self.iterable.append(num)

    def result(self):
        if not (len(self.iterable) == 0):
            return max(self.iterable)
        return None

    def clear(self):
        self.iterable.clear()


class AverageStat:
    def __init__(self, iterable=[]):
        self.iterable = iterable

    def add(self, num):
        self.iterable.append(num)

    def result(self):
        if not (len(self.iterable) == 0):
            return sum(self.iterable) / len(self.iterable)
        return None

    def clear(self):
        self.iterable.clear()



minstat = MinStat()
maxstat = MaxStat()
averagestat = AverageStat()

print(minstat.result())
print(maxstat.result())
print(averagestat.result())

minstat = MinStat()
maxstat = MaxStat()
averagestat = AverageStat()

for i in range(1, 6):
    minstat.add(i)
    maxstat.add(i)
    averagestat.add(i)

print(minstat.result())
print(maxstat.result())
print(averagestat.result())


minstat = MinStat([1, 2, 4])
maxstat = MaxStat([1, 2, 4])
averagestat = AverageStat([1, 2, 4])

minstat.add(5)
maxstat.add(5)
averagestat.add(5)

print(minstat.result())
print(maxstat.result())
print(averagestat.result())
