class Animal:
    def __init__(self, legs: int, have_tail: bool):
        print('Animal')
        self.legs = legs
        self.have_tail = have_tail

    def do_aniaml(self):
        print('doing animal')



class Human(Animal):
    def __init__(self, legs, have_tail, sex):
        print('Human')
        super().__init__(legs, have_tail)
        self.sex = sex

    def say_hi(self):
        print('Hi')

    
    def __repr__(self):
        return f'Legs: {self.legs}, Tail: {self.have_tail}, sex: {self.sex} '
    

class Mother(Human):
    voice = 'Nice voice'
    def __init__(self, legs, have_tail, sex, eye):
        print('Mother')
        super().__init__(legs, have_tail, sex)
        self.eye = eye


class Father(Human):
    power = 'father'
    def __init__(self, legs, have_tail, sex, eye):
        print('Mother')
        super().__init__(legs, have_tail, sex)
        self.eye = eye


class Child(Mother, Father):
    is_chil = True
    def __init__(self):
        print('child')



if __name__ == '__main__':
    bartek = Human(2, False, 'M')
    bartek.do_aniaml()
    print(bartek)
    mama = Mother(2, False, 'W', 'blue')
    tata = Father(2, False, 'W', 'red')

    dziecko = Child()
    dziecko.do_aniaml()
    print(dziecko.is_chil)
    print(dziecko.power)

