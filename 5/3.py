class Czlowiek:
    def __init__(self, imie, wzrost, waga):
        self.imie = imie
        self.wzrost = wzrost
        self.waga = waga

    def speak(self):
        print("Mowie prawde")

    def count_bmi(self):
        return self.waga/((self.wzrost/100)**2)

    def diff_to_norm(self):
        pass

    def save_data(self):
        pass

    def to_burn(self):
        pass

    def to_eat(self):
        pass

    def what_to_do(self):
        pass

class Polityk(Czlowiek):
    def speak(self):
        if self.recive_bribe()==True:
            super().speak()
        else:
            print("Klamie, bo moge")

    def recive_bribe(self):
        return True