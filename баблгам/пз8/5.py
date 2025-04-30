class SuperInt(int):
    def repeat(self, n=2):
        if str(self)[0] == '-':
            count = '-'
            for i in range(n):
                count += str(self)[1:]
            return count
        else:
            count = ''
            for i in range(n):
                count += str(self)
            return count

    def to_bin(self):
        if str(self)[0] == '-':
            return '-' + bin(self)[3:]
        return bin(self)[2:]

    def next(self):
        return self + 1

    def prev(self):
        return self - 1

    def __iter__(self):
        for i in str(self):
            if i == '-':
                continue
            yield i



superint1 = SuperInt(17)
superint2 = SuperInt(-17)

print(superint1.repeat())
print(superint2.repeat(3))

superint1 = SuperInt(17)
superint2 = SuperInt(-17)

print(superint1.to_bin())
print(superint2.to_bin())

superint = SuperInt(17)

print(superint.prev())
print(superint.next())

superint1 = SuperInt(1337)
superint2 = SuperInt(-2077)

print(*superint1)
print(*superint2)
