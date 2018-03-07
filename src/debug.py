def wypiszElement(wezel):
    print("\n\n KOJENA JEDNOSTKA")
    print("typ jednostki: "+str(wezel.typJednostki))
    print("nazwaNumer: "+str(wezel.nazwaNumer))
    print("Adres "+str(wezel.Adres))
    print("uprawnienia "+str(wezel.uprawnieni))
    print("kartyWydane "+str(wezel.kartyWydane))
    print("glosyWazne "+str(wezel.glosyWazne))
    print("glosyNiewazne "+str(wezel.glosyNiewazne))
    print("ilosc dzieci: "+str(len(wezel.dzieci)))

def wypiszDzieciNazwy(wezel):
    for v in wezel.dzieci:
        print("| "+ v.typJednostki + " " + v.nazwaNumer + " |")


def chodzeniePoDrzewie(korzen):
    obecny = korzen
    while True:
        wypiszElement(obecny)
        nrDziecka = input('podaj nr dziecka do ktorego przejsc')
        obecny = obecny.dzieci[int(nrDziecka)]
