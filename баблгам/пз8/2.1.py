class LowerString(str):
    def __new__(cls, obj=''):
        if not isinstance(obj, str):
            obj = str(obj)

        value = obj.lower()
        return super().__new__(cls, value)


s1 = LowerString('BEEGEEK')
s2 = LowerString('BeeGeek')

print(s1)
print(s2)
print(s1 == s2)
print(issubclass(LowerString, str))


print(LowerString(['Bee', 'Geek']))
print(LowerString({'A': 1, 'B': 2, 'C': 3}))
s = LowerString('BeeGeek')


s = LowerString('BeeGeek')

print(s[0])