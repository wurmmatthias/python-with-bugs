# Dieses Skript zählt, wie viele Vokale in einem eingegebenen Satz vorkommen.

def zaehle_vokale(text):
    """Zählt die Anzahl der Vokale im gegebenen Text"""
    vokale = ['a', 'e', 'i', 'o', 'u'] # hier ist nur die kleine Schreibweise vorhanden
    zaehler = 0

    t = text.lower() # Entweder alles auf lower setzten oder das Array erweitern

    for buchstabe in t:
        if buchstabe in vokale:
            zaehler += 1
    return zaehler

def main():
    print("Bitte gib einen Satz ein:")
    eingabe = input(">> ")

    # Anzahl der Vokale ermitteln
    anzahl = zaehle_vokale(eingabe)

    print("Anzahl der Vokale im Text: " + str(anzahl))

if __name__ == "__main__":
    main()

