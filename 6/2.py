class Czas:
    def __init__(self, godzina=0, minuty=0, sekundy=0):
        self.godzina = godzina
        self.minuty = minuty
        self.sekundy = sekundy

    def __str__(self):
        return "g="+str(self.godzina)+" m="+str(self.minuty)+" s="+str(self.sekundy)

    def set_time(self, g=None, m=None, s=None, **kwargs):
        if g:
            self.godzina = g
        if m:
            self.minuty = m
        if s:
            self.sekundy = s

    def add_time(self, h=0, m=0, s=0):
        if s > 59:
            self.minuty += int(s/60)
        self.sekundy += s % 60
        if m > 59:
            self.godzina += int(m/60)
        self.minuty += m % 60
        self.godzina += h

    def seconds(self):
        return self.sekundy + self.minuty * 60 + self.godzina * 60 ** 2

    def minutes(self):
        return self.sekundy * 60 ** (-1) + self.minuty + self.godzina * 60

    def hours(self):
        return self.sekundy * 60 ** (-2) + self.minuty * 60 ** (-1) + self.godzina


class Zegar(Czas):
    def __init__(self, *args, par, **kwargs):
        super().__init__(**kwargs)
        self.par = par


class DokladnyZegar(Zegar):
    def __init__(self, msekundy=0, **kwargs):
        super().__init__(**kwargs)
        self.msekundy = msekundy

    def __str__(self):
        return "g=" + str(self.godzina) + " m=" + str(self.minuty) + " s=" + str(self.sekundy)+" ms="+str(self.msekundy)

    def set_time(self, ms=None, **kwargs):
        super().set_time(**kwargs)
        if ms:
            self.msekundy = ms


def mojprint(strs, count, sufix=False):
    if sufix:
        print(strs * count)
    else:
        for i in range(count):
            print(strs+"\n")


czas = DokladnyZegar(msekundy=23, par="24H", godzina=12, minuty=0, sekundy=0)
czas.set_time(ms=7, g=6, m=7, s=9)
print(czas.__str__())
