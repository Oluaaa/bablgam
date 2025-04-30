class UpperPrintString(str):
    def __init__(self, st):
        self.st = st

    def __str__(self):
        return self.st.upper()


s1 = UpperPrintString('beegeek')
s2 = UpperPrintString('BeeGeek')

print(s1)
print(s2)
s = UpperPrintString('beegeek')
print(list(s))
