# author: Milosz Cygan

class Currency:
    countries = None
    name = None
    shortcut = None

    def __init__(self, countries: list, name: str, shortcut: str):
        self.countries = countries
        self.name = name
        self.shortcut = shortcut

    def __eq__(self, other: object) -> bool:
        return self.shortcut == other.shortcut




class Banknote:
    currency = None
    value = None

    def __init__(self, currency: Currency, value: int):
        self.currency = currency
        self.value = value

    
    def __add__(self, other: object):
        if self.currency == other.currency:
            return self.value + other.value
        else:
            print('Cannot add, diffrent currency')
            return None
        
    def __sub__(self, other: object):
        if self.currency == other.currency:
            return self.value - other.value
        else:
            print('Cannot sub, diffrent currency')
            return None

    # * / no sense 

    def __eq__(self, other: object):
        if self.currency == other.currency:
            return self.value == other.value
        else:
            print('Cannot eq, diffrent currency')
            return None
        
    def __gt__(self, other: object):
        if self.currency == other.currency:
            return self.value > other.value
        else:
            print('Cannot eq, diffrent currency')
            return None




if __name__ == '__main__':
    euro = Currency(['Germany, France'], 'Euro', 'EUR')
    dolar = Currency(['USA', 'Ecuador'], 'United States Dollar', 'USD')


    euro_10 = Banknote(euro, 10)
    euro_20 = Banknote(euro, 20)

    dolar_100 = Banknote(dolar, 100)
    dolar_200 = Banknote(dolar, 200)


    print(f'adding eur10 and eur20 - Value: {euro_10 + euro_20} ')
    print(f'adding eur10 and dolar100 - Value: {euro_10 + dolar_100} ')
    print(dolar_100 > dolar_200)