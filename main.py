from auto import Szemelyauto, Teherauto
from kolcsonzo import Autokolcsonzo

def main():
    kolcsonzo = Autokolcsonzo("Adam's Autókölcsönző")
    kolcsonzo.hozzaad_auto(Szemelyauto("AB-AA-123", "Ford Focus", 12000, 4))
    kolcsonzo.hozzaad_auto(Szemelyauto("AB-AB-456", "Suzuki Vitara", 10000, 4))
    kolcsonzo.hozzaad_auto(Teherauto("TC-AB-123", "Ford Transit", 18000, 1500))

    kolcsonzo.berel_auto("AB-AA-123", "2025-05-16")
    kolcsonzo.berel_auto("TC-AB-123", "2025-05-17")
    kolcsonzo.berel_auto("AB-AB-456", "2025-05-18")
    kolcsonzo.berel_auto("TC-AB-123", "2025-05-19")

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
