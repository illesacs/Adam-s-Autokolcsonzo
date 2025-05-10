class Berles:
    def __init__(self, auto, datum: str):
        self.auto = auto
        self.datum = datum

    def __str__(self):
        return f"{self.auto.rendszam} ({self.auto.tipus}) - {self.datum} - {self.auto.berleti_dij} Ft"
