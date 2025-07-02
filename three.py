def lade_zahlen():
    return [5, 8, 12, "zwölf", 3, -1, 0, 17] 

def berechne_durchschnitt(zahlen):
    return sum(zahlen) / len(zahlen)

            
def finde_gerade(zahlen):
    gerade = []
    for zahl in zahlen:
        if zahl % 2 == 0: # hier stand % 1 == 0, das ist natürlich immer 0
            gerade.append(zahl)
    return gerade


# Überprüft ob alle Werte numerisch sind und gibt bei falschen Werten 
# die Möglichkeit diese zu korrigieren oder zu entfernen.
def check_zahlen(zahlen):
    for zahl in zahlen:
        if isinstance(zahl, (int,float,complex)):
            continue
        else:
            print(str(zahl) + " ist keine Zahl")
            ersetzen = input("Wert ersetzen? (y/n)")

            if ersetzen == "y":
                neu = input("Wert für " + zahl + " eingeben: ")
                zahlen.insert(zahlen.index(zahl), float(neu))
                zahlen.remove(zahl)
            else:
                print(zahl + " wird entfernt.")
                zahlen.remove(zahl)
    return zahlen
                           

def main():
    zahlen = lade_zahlen()
    print("Geladene Zahlen:", zahlen)

    zahlen_gecheckt = check_zahlen(zahlen)

    durchschnitt = berechne_durchschnitt(zahlen_gecheckt)
    print("Durchschnitt:", durchschnitt)

    gerade_zahlen = finde_gerade(zahlen_gecheckt)
    print("Gefundene gerade Zahlen:", gerade_zahlen)

if __name__ == "__main__":
    main()
