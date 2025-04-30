class FuzzyString(str):
    def __new__(cls, obj=''):
        if not isinstance(obj, str):
            obj = str(obj)

        value = obj.lower()
        return super().__new__(cls, value)

    def __eq__(self, other):
        if isinstance(self, str):
            if (self.lower()) == (other.lower()):
                return True
            else:
                return False
        else:
            return False

    def __lt__(self, other):
        if (self.lower()) < (other.lower()):
            return True
        else:
            return False

    def __le__(self, other):
        if (self.lower()) <= (other.lower()):
            return True
        else:
            return False
    def __contains__(self, other):
        if (self.lower()) in (other.lower()):
            return True
        else:
            return False



s = FuzzyString('patrick')

words = ['patrick', 'Patrick', 'pAtrick', 'PAtrick', 'paTrick', 'PaTrick', 'pATrick', 'PATrick', 'patRick', 'PatRick',
         'pAtRick', 'PAtRick', 'paTRick', 'PaTRick', 'pATRick', 'PATRick', 'patrIck', 'PatrIck', 'pAtrIck', 'PAtrIck',
         'paTrIck', 'PaTrIck', 'pATrIck', 'PATrIck', 'patRIck', 'PatRIck', 'pAtRIck', 'PAtRIck', 'paTRIck', 'PaTRIck',
         'pATRIck', 'PATRIck', 'patriCk', 'PatriCk', 'pAtriCk', 'PAtriCk', 'paTriCk', 'PaTriCk', 'pATriCk', 'PATriCk',
         'patRiCk', 'PatRiCk', 'pAtRiCk', 'PAtRiCk', 'paTRiCk', 'PaTRiCk', 'pATRiCk', 'PATRiCk', 'patrICk', 'PatrICk',
         'pAtrICk', 'PAtrICk', 'paTrICk', 'PaTrICk', 'pATrICk', 'PATrICk', 'patRICk', 'PatRICk', 'pAtRICk', 'PAtRICk',
         'paTRICk', 'PaTRICk', 'pATRICk', 'PATRICk', 'patricK', 'PatricK', 'pAtricK', 'PAtricK', 'paTricK', 'PaTricK',
         'pATricK', 'PATricK', 'patRicK', 'PatRicK', 'pAtRicK', 'PAtRicK', 'paTRicK', 'PaTRicK', 'pATRicK', 'PATRicK',
         'patrIcK', 'PatrIcK', 'pAtrIcK', 'PAtrIcK', 'paTrIcK', 'PaTrIcK', 'pATrIcK', 'PATrIcK', 'patRIcK', 'PatRIcK',
         'pAtRIcK', 'PAtRIcK', 'paTRIcK', 'PaTRIcK', 'pATRIcK', 'PATRIcK', 'patriCK', 'PatriCK', 'pAtriCK', 'PAtriCK',
         'paTriCK', 'PaTriCK', 'pATriCK', 'PATriCK', 'patRiCK', 'PatRiCK', 'pAtRiCK', 'PAtRiCK', 'paTRiCK', 'PaTRiCK',
         'pATRiCK', 'PATRiCK', 'patrICK', 'PatrICK', 'pAtrICK', 'PAtrICK', 'paTrICK', 'PaTrICK', 'pATrICK', 'PATrICK',
         'patRICK', 'PatRICK', 'pAtRICK', 'PAtRICK', 'paTRICK', 'PaTRICK', 'pATRICK', 'PATRICK']

print(all(s == item for item in words))