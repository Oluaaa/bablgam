class Logger:
    def __setattr__(self, attr, value):
        print(f"Изменение значения атрибута {attr} на {value}")
        object.__setattr__(self, attr, value)

    def __delattr__(self, attr):
        print(f"Удаление атрибута {attr}")
        object.__delattr__(self, attr)


obj = Logger()

obj.name = 'pygen'
obj.rating = '5*'
obj.ceo = 'Timur'
del obj.rating
obj.rating = '6*'
