print("Welke kaas is het?")
print("Antwoord alleen met 'ja' of 'nee'")
Antwoord = input("Is de kaas geel? ")
if Antwoord == "ja":
    Antwoordj = input("Zitten er gaten in? ")
    if Antwoordj == "ja":
        Antwoordjj = input("Is de kaas belachelijk duur? ")
        if Antwoordjj == "ja":
            print("Emmenthaler")
        elif Antwoordjj == "nee":
            print("Leerdammer")
    elif Antwoordj == "nee":
        Antwoordjn = input("Is de kaas hard als steen? ")
        if Antwoordjn == "ja":
            print("Parmigiano")
        elif Antwoordjn == "nee":
            print("Goudse kaas")
elif Antwoord == "nee":
    Antwoordn = input("Heeft de kaas blauwe schimmel? ")
    if Antwoordn == "ja":
        Antwoordnj = input("Heeft de kaas een korst? ")
        if Antwoordnj == "ja":
            print("Bleu de Rochbaron")
        elif Antwoordnj == "nee":
            print("Foume d'Ambert")
    elif Antwoordn == "nee":
        Antwoordnn = input("Heeft de kaas een korst? ")
        if Antwoordnn == "ja":
            print("Camembert")
        elif Antwoordnn == "nee":
            print("Mozarella")     


