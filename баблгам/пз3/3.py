class AttrsIterator:
    def __init__(self, obj):
        self.obj = obj
        self.attr_names = list(self.obj.__dict__.values())
    
    @property
    def zz(self):
        return ('name', self.attr_names[0]), ('surname', self.attr_names[1]), ('age', self.attr_names[2])

    def __iter__(self=None):
        return iter(self.zz)


class User:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age


user = User('Debbie', 'Harry', 77)
attrsiterator = AttrsIterator(user)

print(*attrsiterator)