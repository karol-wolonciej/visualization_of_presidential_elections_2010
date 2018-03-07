import os
from jinja2 import Environment, PackageLoader
from src import classes


def stworzFolder(sciezka):
    if not os.path.exists(sciezka):
        os.makedirs(sciezka)

def stworzSciezkeDoFolderu(wezel, dotychczasowaSciezka):
    typJednostki = wezel.typJednostki
    nazwaNumer = wezel.nazwaNumer
    if isinstance(typJednostki, float):
        typJednostki = int(typJednostki)
    if isinstance(nazwaNumer, float):
        nazwaNumer = int(nazwaNumer)
    return dotychczasowaSciezka + "/" + str(typJednostki) + "_" + str(nazwaNumer)

def stworzSciezkeZKoncowaStrona(wezel, sciezkaDoDocelowegoFolderu):
    typJednostki = wezel.typJednostki
    nazwaNumer = wezel.nazwaNumer
    if isinstance(typJednostki, float):
        typJednostki = int(typJednostki)
    if isinstance(nazwaNumer, float):
        nazwaNumer = int(nazwaNumer)
    return sciezkaDoDocelowegoFolderu + "/" + str(typJednostki) + "_" + str(nazwaNumer)


def stworzStrone(wezel, sciezkaZKoncowaStrona, sciezkaDoPoprzednika, sciezkaDoStylow):
    env = Environment(
        loader=PackageLoader('yourapplication','templates'),
        #autoescape=select_autoescape(['html', 'xml'])
    )
    template = env.get_template('wezelTemplate.html')
    output_from_parsed_template = template.render(dane = wezel,
                                                  sciezkaZKoncowaStrona = sciezkaZKoncowaStrona,
                                                  sciezkaDoPoprzednika = sciezkaDoPoprzednika,
                                                  sciezkaDoStylow = sciezkaDoStylow,
                                                  imionaKandydatow = classes.Kandydaci.imiona
                                                  )
    with open(sciezkaZKoncowaStrona+".html", "w") as fh:
        fh.write(output_from_parsed_template)


def stworzStroneGlowna(wezel, sciezkaZKoncowaStrona, sciezkaDoStylow):
    env = Environment(
        loader=PackageLoader('yourapplication', 'templates'),
        # autoescape=select_autoescape(['html', 'xml'])
    )
    template = env.get_template('korzenPolskaTemplate.html')
    output_from_parsed_template = template.render(dane=wezel,
                                                  sciezkaZKoncowaStrona=sciezkaZKoncowaStrona,
                                                  sciezkaDoPoprzednika=sciezkaZKoncowaStrona,
                                                  sciezkaDoStylow=sciezkaDoStylow,
                                                  imionaKandydatow=classes.Kandydaci.imiona
                                                  )
    with open(sciezkaZKoncowaStrona + "/" + str(wezel.typJednostki) + "_" + str(wezel.nazwaNumer) + ".html", "w") as fh:
        fh.write(output_from_parsed_template)


def stworzDrzewoFolderow(korzen, dotychczasowaSciezka):
    if korzen.dzieci:
        for v in korzen.dzieci:
            sciezkaDoFolderuDziecka = stworzSciezkeDoFolderu(v, dotychczasowaSciezka)
            stworzFolder(sciezkaDoFolderuDziecka)
            stworzDrzewoFolderow(v, sciezkaDoFolderuDziecka)



def stworzWszystkieStronyDlaDrzewa(korzen, dotychczasowaSciezka, dotychczasowaSciezkaDoStylow, zaglebienie):
    if zaglebienie <= 0:
        return
    if korzen.dzieci:
        for v in korzen.dzieci:
            sciezkaDoFolderuDziecka = stworzSciezkeDoFolderu(v, dotychczasowaSciezka)
            stworzStrone(v ,stworzSciezkeZKoncowaStrona(v, sciezkaDoFolderuDziecka), dotychczasowaSciezka+".html", "../"+dotychczasowaSciezkaDoStylow)
            stworzWszystkieStronyDlaDrzewa(v, sciezkaDoFolderuDziecka, "../"+dotychczasowaSciezkaDoStylow, zaglebienie -1)

