# werken-met-condities
## F1.3.01.L1
### input en if-statement
a = int(input("a = "))
b = int(input("b = "))
if a > b: 
    Max = a
    Min = b
    print("a is het grootste getal: " + str(Max))
### elif-statement
a = int(input("a = "))
b = int(input("b = "))
if a > b: 
    Max = a
    Min = b
    print("a is het grootste getal: " + str(Max))
elif a < b:
    Max = b
    Min = a
    print("a is het kleinste getal: " + str(Min))
### else-statement
a = int(input("a = "))
b = int(input("b = "))
if a > b: 
    Max = a
    Min = b
    print("a is het grootste getal: " + str(Max))
elif a < b:
    Max = b
    Min = a
    print("a is het kleinste getal: " + str(Min))
else:
    print("a en b zijn even groot")
### Min en Max
a = int(input("a = "))
b = int(input("b = "))
if a > b: 
    Max = a
    Min = b
    print("a is het grootste getal: " + str(Max))
    print("Het maximum is: " + str(Max))
    print("Het minimum is: " + str(Min))

elif a < b:
    Max = b
    Min = a
    print("a is het kleinste getal: " + str(Min))
    print("Het maximum is: " + str(Max))
    print("Het minimum is: " + str(Min))
else:
    Max = a
    Max = b
    print("a en b zijn even groot")
    print("Het maximum is: " + str(Max))
    print("Het minimum is: " + str(Min))
## F1.3.01.L2 
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