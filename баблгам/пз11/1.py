class USADate:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def format(self):
        return f'{self.month:02}-{self.day:02}-{self.year}'

    def iso_format(self):
        return f'{self.year}-{self.month:02}-{self.day:02}'


class ItalianDate:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def format(self):
        return f'{self.day:02}/{self.month:02}/{self.year}'

    def iso_format(self):
        return f'{self.year}-{self.month:02}-{self.day:02}'


usadate = USADate(2023, 4, 6)

print(usadate.format())
print(usadate.iso_format())


italiandate = ItalianDate(2023, 4, 6)

print(italiandate.format())
print(italiandate.iso_format())
