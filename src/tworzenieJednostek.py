import xlrd
from src import classes

class arkuszOkregu:
    nrOkregu = 0
    kodGminy = 1
    gmina = 2
    nrObwodu = 4
    adres = 6
    uprawnieni = 7
    wydane = 8
    karty = 9
    glosyWazne = 11
    glosyNiewazne = 10
    pierwszyKandydat = 12


class arkuszWojewodztwa:
   symbolPoczatkuWojewodztwa = 0
   nrOkregu = 0
   siedziba = 1
   nazwaWojewodztwa = 1

def nrDoSciezki(nr):
    if nr < 10:
        return "0" + str(int(nr))
    else:
        return str(int(nr))




def stworz_obwod(sheet, wiersz, rodzic):
    obwod = classes.Wezel("obwód", int(sheet.cell(wiersz, arkuszOkregu.nrObwodu).value), rodzic)
    obwod.Adres = sheet.cell(wiersz, arkuszOkregu.adres).value
    obwod.glosyNiewazne = sheet.cell(wiersz, arkuszOkregu.glosyNiewazne).value
    obwod.glosyWazne = sheet.cell(wiersz, arkuszOkregu.glosyWazne).value
    obwod.kartyWydane = sheet.cell(wiersz, arkuszOkregu.karty).value
    obwod.uprawnieni = sheet.cell(wiersz, arkuszOkregu.uprawnieni).value
    for i in range(0, classes.iloscKandydatow):
        obwod.wynikiKandydatow[i] = int(sheet.cell(wiersz, i+arkuszOkregu.pierwszyKandydat).value)
    obwod.zsumujWynikiWezla()
    return obwod



def stworz_gmine(sheet, rodzic, od, do):
    gmina = classes.Wezel("gmina", sheet.cell(od, arkuszOkregu.gmina).value, rodzic)
    gmina.kod = sheet.cell(od, arkuszOkregu.kodGminy).value
    for i in range(od, do+1):
        gmina.dzieci.append(stworz_obwod(sheet, i, gmina))

    return gmina


def stworz_okrag(nrOkregu, rodzic):
    book = xlrd.open_workbook("data/daneOkregowGmin/obw" + nrDoSciezki(nrOkregu) +".xls")
    sheet = book.sheet_by_index(0)

    okrag = classes.Wezel("okrąg", int(nrOkregu), rodzic)
    iloscWierszyArkusza = sheet.nrows
    poczatekGminy = 1
    koniecGminy = -1
    kodGminy = sheet.cell(poczatekGminy, arkuszOkregu.kodGminy).value

    for i in range(2, iloscWierszyArkusza+1):
        if i == iloscWierszyArkusza:
            koniecGminy = iloscWierszyArkusza-1
            okrag.dzieci.append(stworz_gmine(sheet, okrag, poczatekGminy, koniecGminy))

        elif(kodGminy != sheet.cell(i, arkuszOkregu.kodGminy).value):
            koniecGminy = i-1
            okrag.dzieci.append(stworz_gmine(sheet, okrag, poczatekGminy, koniecGminy))
            kodGminy = sheet.cell(i, arkuszOkregu.kodGminy).value
            poczatekGminy = i

    return okrag

def stworz_wojewodztwo(sheet, rodzic, od, do):
    wojewodztwo = classes.Wezel("województwo", sheet.cell(od-1, arkuszWojewodztwa.nazwaWojewodztwa).value, rodzic)
    for i in range(od, do+1):
        wojewodztwo.dzieci.append(stworz_okrag(sheet.cell(i, arkuszWojewodztwa.nrOkregu).value, wojewodztwo))

    return wojewodztwo


def stworz_kraj():
    kraj = classes.Wezel("cały_kraj", "Polska", None)
    kraj.wezelRodzic = kraj

    book = xlrd.open_workbook("data/daneWojewodztw/zal2.xls")
    sheet = book.sheet_by_index(0)
    iloscWierszyArkusza = sheet.nrows
    symbolPoczatkuNowegoWojewodztwa = "województwo"
    poczatekWojewodztwa = 8

    for i in range(10, iloscWierszyArkusza+1):
        if i == iloscWierszyArkusza:
            koniecWojewodztwa = iloscWierszyArkusza-1
            kraj.dzieci.append(stworz_wojewodztwo(sheet, kraj, poczatekWojewodztwa, koniecWojewodztwa))

        elif(symbolPoczatkuNowegoWojewodztwa == sheet.cell(i, arkuszWojewodztwa.symbolPoczatkuWojewodztwa).value):
            koniecWojewodztwa = i-1
            kraj.dzieci.append(stworz_wojewodztwo(sheet, kraj, poczatekWojewodztwa, koniecWojewodztwa))
            poczatekWojewodztwa = i+1

    return kraj



