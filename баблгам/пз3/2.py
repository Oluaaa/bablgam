class DevelopmentTeam:
    def __init__(self, lst=[]):
        self.lst = lst

    def add_junior(self=None, *arg):
        if len(arg) == 1:
            self.lst.append((arg[0], 'junior'))
        else:
            for i in arg:
                self.lst.append((i, 'junior'))

    def add_senior(self=None, *arg):
        if len(arg) == 1:
            self.lst.append((arg[0], 'senior'))
        else:
            for i in arg:
                self.lst.append((i, 'senior'))

    @property
    def get(self):
        return self.lst

    def __iter__(self):
        return iter(self.lst)


beegeek = DevelopmentTeam()

beegeek.add_junior('Timur')
beegeek.add_junior('Arthur', 'Valery')
print(*beegeek, sep='\n')
