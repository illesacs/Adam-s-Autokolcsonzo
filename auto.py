from abc import ABC, abstractmethod

class Auto(ABC):
    def __init__(self, rendszam: str, tipus: str, berleti_dij: int):
        self.rendszam = rendszam
        self.tipus = tipus
        self.berleti_dij = berleti_dij

    @abstractmethod
    def __str__(self):
        pass

class Szemelyauto(Auto):
    def __init__(self, rendszam: str, tipus: str, berleti_dij: int, utas_szam: int):
        super().__init__(rendszam, tipus, berleti_dij)
        self.utas_szam = utas_szam

    def __str__(self):
        return f"Személyautó: {self.rendszam} - {self.tipus} - {self.berleti_dij} Ft/nap - {self.utas_szam} utas"

class Teherauto(Auto):
    def __init__(self, rendszam: str, tipus: str, berleti_dij: int, teherbiras: int):
        super().__init__(rendszam, tipus, berleti_dij)
        self.teherbiras = teherbiras

    def __str__(self):
        return f"Teherautó: {self.rendszam} - {self.tipus} - {self.berleti_dij} Ft/nap - {self.teherbiras} kg"
