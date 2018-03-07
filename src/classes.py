iloscKandydatow = 12



class Wezel:
    def __init__(self, typJednostki, nazwaNumer, wezelRodzic):
        self.typJednostki = typJednostki
        self.nazwaNumer = nazwaNumer
        self.Adres = ""
        self.uprawnieni = 0
        self.kartyWydane = 0
        self.glosyWazne = 0
        self.glosyNiewazne = 0
        self.wynikiKandydatow = [0] * iloscKandydatow
        self.sumaWszystkichGlosow = 0
        self.wezelRodzic = wezelRodzic
        self.kod = -1
        self.dzieci = []


    def zsumujPoddrzewo(self):
        #napraw nazwe
        self.typJednostki = str(self.typJednostki)
        self.nazwaNumer = str(self.nazwaNumer)
        self.typJednostki = (self.typJednostki).replace(" ", "_")
        self.nazwaNumer = (self.nazwaNumer).replace(" ", "_")


        for dziecko in self.dzieci:
            dziecko.zsumujPoddrzewo()
            self.uprawnieni += dziecko.uprawnieni
            self.kartyWydane += dziecko.kartyWydane
            self.glosyWazne += dziecko.glosyWazne
            self.glosyNiewazne += dziecko.glosyNiewazne
            self.sumaWszystkichGlosow += dziecko.sumaWszystkichGlosow
            for i in range(0, iloscKandydatow):
                self.wynikiKandydatow[i] += dziecko.wynikiKandydatow[i]

    def zsumujWynikiWezla(self):
        suma = 0
        for i in range(0, len(self.wynikiKandydatow)):
            suma += self.wynikiKandydatow[i]
        if suma == 0:
            suma += 1
        self.sumaWszystkichGlosow = suma




class Kandydaci:
    imiona = ["Grabowski Dariusz Maciej", "Ikonowicz Piotr", "Kalinowski Jarosław",
                 "Korwin-Mikke Janusz", "Krzaklewski Marian", "Kwaśniewski Aleksander",
                 "Lepper Andrzej", "Łopuszański Jan", "Olechowski Andrzej Marian",
                 "Pawłowski Bogdan" , "Wałęsa Lech" , "Wilecki Tadeusz Adam"]

"""
TypJednostki
nazwaNumer
Adres

uprawnieni
kartyWydane
glosyWazne
glosyNiewazne

wynikiKandydatow = [0] * iloscKandydatow
l = [None] * 10

"""