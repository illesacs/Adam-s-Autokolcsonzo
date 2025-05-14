from auto import Szemelyauto, Teherauto
from kolcsonzo import Autokolcsonzo

def main():
    kolcsonzo = Autokolcsonzo("Adam's Autókölcsönző")
    kolcsonzo.hozzaad_auto(Szemelyauto("AA-AA-001", "Opel Astra", 9000, 5))
    kolcsonzo.hozzaad_auto(Szemelyauto("AB-AA-123", "Ford Focus", 12000, 4))
    kolcsonzo.hozzaad_auto(Szemelyauto("AB-AB-456", "Suzuki Vitara", 10000, 4))
    kolcsonzo.hozzaad_auto(Szemelyauto("AB-BB-789", "Suzuki Swift", 8000, 4))
    kolcsonzo.hozzaad_auto(Teherauto("TC-AA-123", "Mercedes Sprinter", 20000, 1500))
    kolcsonzo.hozzaad_auto(Teherauto("TC-AB-456", "Ford Transit", 18000, 1500))
    kolcsonzo.hozzaad_auto(Teherauto("TC-BB-789", "Iveco Daily", 16000, 1500))

    kolcsonzo.berel_auto("AAA-111", "2025-05-10")
    kolcsonzo.berel_auto("BBB-222", "2025-05-11")
    kolcsonzo.berel_auto("CCC-333", "2025-05-12")
    kolcsonzo.berel_auto("AAA-111", "2025-05-13")

    while True:
        print("\n--- Adam's Autókölcsönző ---")
        print("1. Autó bérlése")
        print("2. Bérlés lemondása")
        print("3. Bérlések listázása")
        print("0. Kilépés")
        valasz = input("Választott menüpont: ")

        if valasz == "1":
            print("\nElérhető autók:")
            for auto in kolcsonzo.autok:
                print(f" - {auto}")
            rendszam = input("Add meg a rendszámot: ")
            datum = input("Add meg a bérlés dátumát (YYYY-MM-DD): ")
            print(kolcsonzo.berel_auto(rendszam, datum))
        elif valasz == "2":
            rendszam = input("Add meg a rendszámot: ")
            datum = input("Add meg a lemondandó bérlés dátumát (YYYY-MM-DD): ")
            print(kolcsonzo.lemond_berlest(rendszam, datum))
        elif valasz == "3":
            print("\nAktív bérlések:")
            print(kolcsonzo.listaz_berlesek())
        elif valasz == "0":
            print("Kilépés...")
            break
        else:
            print("Érvénytelen választás!")

if __name__ == "__main__":
    main()
