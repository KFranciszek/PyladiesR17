class Czlowiek:
    def __init__(self, imie, wzrost, waga):
        self.imie = imie
        self.wzrost = wzrost
        self.waga = waga

    def speak(self):
        print("Mowie prawde")

    def count_bmi(self):
        return self.waga / ((self.wzrost / 100) ** 2)

    def diff_to_norm(self):
        if self.count_bmi() >= 25:
            return (self.count_bmi()-25)*((self.wzrost/100) ** 2)
        elif self. count_bmi() <= 18.5:
            return (18.5-self.count_bmi())*((self.wzrost/100) ** 2)
        else:
            return 0

    def save_data(self):
        file = open(self.imie+".json", 'w')
        file.writelines('{\"imie\": \"' + self.imie + "\", \"wzrost\" : " + str(self.wzrost) + ", \"waga\" : " + str(self.waga) + ", \"bmi\" : " + str(self.count_bmi()) + '}')
        file.close()

    def to_burn(self, activity):
        kcal = self.diff_to_norm()*6000
        if activity == "run":
            return kcal/500
        elif activity == "bike":
            return  kcal/600
        elif activity == "hobby":
            return kcal/250
        elif activity == "chess":
            return  kcal/150
        else:
            return "That's REALLY REALLY odd activity"

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

adam = Czlowiek("Adam", 250, 70)
print(adam.diff_to_norm())
print(adam.to_burn(""))
