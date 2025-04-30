class Validator:
    def __init__(self, obj):
        self.obj = obj

    def is_valid(self):
        return None

class NumberValidator(Validator):
    def is_valid(self):
        if isinstance(self.obj, int) or isinstance(self.obj, float):
            return True
        return False



print(issubclass(NumberValidator, Validator))

validator1 = NumberValidator('beegeek')
validator2 = NumberValidator(1)
validator3 = NumberValidator(1.1)

print(validator1.is_valid())
print(validator2.is_valid())
print(validator3.is_valid())

