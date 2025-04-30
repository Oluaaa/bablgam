class LowerString(str):
    def __init__(self, obj=''):
        self.obj = obj
        if self.obj == '':
            self.obj = ''
        else:
            if isinstance(self.obj, str):
                self.obj = self.obj.lower()
                self.obj = str(self.obj)
            elif isinstance(self.obj, list):
                self.obj = [i.lower() for i in self.obj]
                self.obj = str(self.obj)
            elif isinstance(self.obj, dict):
                self.obj = {i.lower(): j for i, j in self.obj.items()}
                self.obj = str(self.obj)

    def __str__(self):
        return self.obj

    def __eq__(self, other):
        if isinstance(self.obj, str):
            return self.obj.lower() == other.obj.lower()
        elif isinstance(self.obj, list):
            return [i.lower for i in self.obj] == [i.lower for i in other.obj]
        elif isinstance(self.obj, dict):
            return {i.lower: j for i, j in self.obj.items()} == {i.lower: j for i, j in self.obj.items()}


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

print(s)
