#from src import tworzenieJednostek
#from src import debug
#from src import tworzeniePlikowINazw
from src import tworzeniePlikowINazw, tworzenieJednostek

#from jinja2 import Environment, PackageLoader

wszystkieStrony = 6

kraj = tworzenieJednostek.stworz_kraj()
kraj.zsumujPoddrzewo()
tworzeniePlikowINazw.stworzDrzewoFolderow(kraj, "wynikiGeneratora/kraj")
tworzeniePlikowINazw.stworzWszystkieStronyDlaDrzewa(kraj, "wynikiGeneratora/kraj", "../../style", wszystkieStrony)
tworzeniePlikowINazw.stworzStroneGlowna(kraj, "wynikiGeneratora/kraj", "../../style")

#debug.chodzeniePoDrzewie(kraj)
#debug.wypiszDzieciNazwy(kraj)