print("Welke kaas is het?")
print("Antwoord alleen met 'ja' of 'nee'")
print("Is de kaas geel? ")
Antwoord = input("")
if Antwoord == "ja":
    print("Zitten er gaten in?")
    Antwoordj = input("")
    if Antwoordj == "ja":
        print("Is de kaas belachelijk duur?")
        Antwoordjj = input("")
        if Antwoordjj == "ja":
            print("Emmenthaler")
        elif Antwoordjj == "nee":
            print("Leerdammer")
    elif Antwoordj == "nee":
        print("Is de kaas hard als steen?")
        Antwoordjn = input("")
        if Antwoordjn == "ja":
            print("Parmigiano")
        elif Antwoordjn == "nee":
            print("Goudse kaas")
elif Antwoord == "nee":
    print("Heeft de kaas blauwe schimmel?")
    Antwoordn = input("")
    if Antwoordn == "ja":
        print("Heeft de kaas een korst?")
        Antwoordnj = input("")
        if Antwoordnj == "ja":
            print("Bleu de Rochbaron")
        elif Antwoordnj == "nee":
            print("Foume d'Ambert")
    elif Antwoordn == "nee":
        print("Heeft de kaas een korst?")
        Antwoordnn = input("")
        if Antwoordnn == "ja":
            print("Camembert")
        elif Antwoordnn == "nee":
            print("Mozarella")     
