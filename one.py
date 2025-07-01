# Dieses Skript fragt den Benutzer nach einer Liste von Zahlen,
# berechnet dann den Durchschnitt und gibt ihn aus.

def berechne_durchschnitt(zahlen_liste):
    """Berechnet den Durchschnitt einer Liste von Zahlen"""
    summe = 0
    for zahl in zahlen_liste:
        summe += zahl
    durchschnitt = summe / len(zahlen_liste)
    return durchschnitt

def main():
    print("Gib mehrere Zahlen ein, getrennt durch Kommas (z.B. 3,5,7,9):")
    eingabe = input("Zahlen: ")
    
    # Umwandlung der Eingabe in eine Liste von Ganzzahlen
    zahlen = eingabe.split(",")
    zahlen = [int(z.strip()) for z in zahlen]  # BUG 1: int statt float – bei Dezimalzahlen Fehler

    # Durchschnitt berechnen
    durchschnitt = berechne_durchschnitt(zahlen)

    # Ergebnis ausgeben
    print("Der Durchschnitt der Zahlen ist: " + durchschnitt)  # BUG 2: Typfehler – String + Float

if __name__ == "__main__":
    main()
