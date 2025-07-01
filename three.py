def lade_zahlen():
    return [5, 8, 12, "zwölf", 3, -1, 0, 17]

def berechne_durchschnitt(zahlen):
    return sum(zahlen) / len(zahlen)

def finde_gerade(zahlen):
    gerade = []
    for zahl in zahlen:
        if zahl % 1 == 0:
            gerade.append(zahl)
    return gerade

def main():
    zahlen = lade_zahlen()
    print("Geladene Zahlen:", zahlen)

    durchschnitt = berechne_durchschnitt(zahlen)
    print("Durchschnitt:", durchschnitt)

    gerade_zahlen = finde_gerade(zahlen)
    print("Gefundene gerade Zahlen:", gerade_zahlen)

if __name__ == "__main__":
    main()
