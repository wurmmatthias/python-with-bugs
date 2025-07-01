# Dieses Skript zählt, wie viele Vokale in einem eingegebenen Satz vorkommen.

def zaehle_vokale(text):
    """Zählt die Anzahl der Vokale im gegebenen Text"""
    vokale = ['a', 'e', 'i', 'o', 'u']
    zaehler = 0
    for buchstabe in text:
        if buchstabe in vokale:
            zaehler += 1
    return zaehler

def main():
    print("Bitte gib einen Satz ein:")
    eingabe = input(">> ")

    # Anzahl der Vokale ermitteln
    anzahl = zaehle_vokale(eingabe)

    print("Anzahl der Vokale im Text: " + str(anzahl))  # BUG 1: Typfehler – String + int

    # BUG 2 (optional): Großbuchstaben werden nicht als Vokale erkannt

if __name__ == "__main__":
    main()

