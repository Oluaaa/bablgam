class RoundedInt(int):
    def __new__(cls, num, even=True):
        if even:
            if num % 2 == 0:
                num = num
            if num % 2 == 1:
                num = num + 1
        else:
            if num % 2 == 1:
                num = num
            if num % 2 == 0:
                num = num + 1

        return super().__new__(cls, num)


print(RoundedInt(7))
print(RoundedInt(8))
print(RoundedInt(7, False))
print(RoundedInt(8, False))

roundedint1 = RoundedInt(7)
roundedint2 = RoundedInt(7, False)

print(roundedint1 + roundedint2)
print(roundedint1 + 1)
print(roundedint2 + 1)

print(type(roundedint1))
print(type(roundedint2))
