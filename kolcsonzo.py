from datetime import datetime
from berles import Berles

class Autokolcsonzo:
    def __init__(self, nev: str):
        self.nev = nev
        self.autok = []
        self.berlesek = []

    def hozzaad_auto(self, auto):
        self.autok.append(auto)

    def berel_auto(self, rendszam: str, datum: str):
        if not self._valid_datum(datum):
            return "Hibás dátum formátum! (elvárt: YYYY-MM-DD)"

        auto = self._keres_auto(rendszam)
        if auto is None:
            return f"Nincs ilyen rendszámú autó: {rendszam}"

        if self._foglalt_e(rendszam, datum):
            return "Az autó már foglalt erre a napra!"

        self.berlesek.append(Berles(auto, datum))
        return f"Sikeres bérlés! Ár: {auto.berleti_dij} Ft"

    def lemond_berlest(self, rendszam: str, datum: str):
        for b in self.berlesek:
            if b.auto.rendszam == rendszam and b.datum == datum:
                self.berlesek.remove(b)
                return "A bérlés sikeresen törölve."
        return "Nincs ilyen bérlés!"

    def listaz_berlesek(self):
        if not self.berlesek:
            return "Nincsenek aktív bérlések."
        return "\n".join(str(b) for b in self.berlesek)

    def _keres_auto(self, rendszam: str):
        for auto in self.autok:
            if auto.rendszam == rendszam:
                return auto
        return None

    def _foglalt_e(self, rendszam: str, datum: str):
        return any(b.auto.rendszam == rendszam and b.datum == datum for b in self.berlesek)

    def _valid_datum(self, datum: str):
        try:
            datetime.strptime(datum, "%Y-%m-%d")
            return True
        except ValueError:
            return False
