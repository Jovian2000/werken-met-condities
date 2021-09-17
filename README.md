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
## F1.3.01.O1
print("------------------------------------------------------------")
print("     Vacature: Circusdirecteur voor Circus HotelDeBotel")
print("------------------------------------------------------------")
print("Er word u een aantal relevante vragen gesteld...")
print("Als blijkt dat u aan de criteria voldoet dan komt u in")
print("aanmerking voor een serieus sollicitatiegesprek!")
print("Ontspan maar blijf wakker, hier komen de vragen")
print("------------------------------------------------------------")
    # (line 1 - 8) hier ziet de gebruiker gewoon het begin
print("Wat is uw naam?")
naam = input("")
    # (line 10 - 11 ) hier word er door de naam van de gebruiker gevraagd 
print("U geslacht? M/V")
geslacht = input("")
    # (line 13 - 14) hier word gevraagd aan de gebruiker wat het geslacht is  
print("Wat is uw lengte in hele cm?")
lengte = int(input(""))
    # (line 16 - 17) hier word de lengte van de gebruiker gevraagd 
print("Wat is u lichaamsgewicht in kg?")
gewicht = int(input(""))
    # (line 19 - 20) hier word het gewicht gevraagd 
if lengte >= 150 and gewicht >=90:
    # (line 22) hier word berekend of de lengte groter is of gelijk aan 150 en het gewicht is groter of gelijk aan 90, zo ja dan mag de gebruiker verder en zo niet dan word die al afgewezen  
    print("Heeft u een diploma? J/N")
    diploma = input("")
    # hier word er gevraagd of de gebruiker een diploma heeft (line 24 - 25)      
    if diploma == "j" or diploma == "J" or diploma == "ja" or diploma == "Ja":
        # (line 27) als de gebruiker j of ja heeft ingetypt mag de gebruiker verder
        print("Wat voor diploma heeft u? MBO/HBO/Universiteit/...")
        diploma2 = input("")
        # (line 29 - 30) hier word gevraagd wat voor diploma
        if diploma2 == "MBO" or diploma2 == "mbo" or diploma2 == "Mbo":
            # (line 32) als de gebruiker mbo heeft gekozen mag de gebruiker door naar de volgende vraag op line 34
            print("Op welk niveau heeft u het afgerond?")
            diplomaMBO = int(input("Niveau "))
            # (line 34 - 35) hier word gevraagd op welk niveau de gebruiker het heeft afgerond
            if diplomaMBO == 4:
                # (line 37) als de gebruiker niveau 4 heeft geantwoord dan gaat de gebruiker verder naar de volgende vraag
                print("Is uw opleiding gerelateerd op ondernemen? J/N")
                diplomaMBO4 = input("")
                # (line 39 - 40) hier word weer een vraag gesteld
                if diplomaMBO4 == "J" or diplomaMBO4 == "j" or diplomaMBO4 == "Ja" or diplomaMBO4 == "ja":
                    # (line 43) als de gebruiker j of ja antwoord, word er weer drie vragen gesteld
                    print("Hoeveel jaar praktijkervaring heeft u met dieren-dressuur?")
                    vraag1 = int(input(""))
                    print("Hoeveel jaar praktijkervaring heeft u met jongleren?")
                    vraag2 = int(input(""))
                    print("Hoeveel jaar praktijkervaring heeft u met acrobatiek?")
                    vraag3 = int(input(""))
                    # (line 44 - 49) hier worden drie vragen gesteld waarop de gebruiker weer op moet antwoorden
                    if vraag1 >= 4 or vraag2 >= 5 or vraag3 >= 3:
                        # (line 51) als de gebruiker 1 van de 3 beantwoord, hoger dan de aangegeven getal, dan gaat de gebruiker verder naar de volgende vraag
                        print("Bezit u een geldige vracht rijbewijs? J/N")
                        vraag5 = input("")
                        # (line 53 - 54 er word weer een vraag gesteld)
                        if vraag5 == "j" or vraag5 == "J" or vraag5 == "ja" or vraag5 == "Ja":
                            print("Bezit u een hoge hoed? J/N")
                            vraag6 = input("")
                            if (vraag6 == "j" or vraag6 == "J" or vraag6 == "Ja" or vraag6 == "ja") and (geslacht == "M" or geslacht == "m" or geslacht == "Man" or geslacht == "man"):
                                # (line 59) als de gebruiker j of ja heeft geantwoord en bij geslacht m of man heeft gezet op line 14 dan gaat hij verder naar de vraag op line 61
                                print("Heeft u gezichtsbeharing? J/N")
                                vraag7m = input("")
                                if vraag7m == "J" or vraag7m == "j" or vraag7m == "ja" or vraag7m == "Ja":
                                    print("Wat voor soort gezichtsbeharing heeft u? Snor/baard/beide/geen")
                                    vraag8m = input("")
                                    if vraag8m == "snor" or vraag8m == "Snor":
                                        print("Hoe breed is uw snor in hele cm?")
                                        vraag10m = int(input(""))
                                        if vraag10m >= 10:
                                            print("Heeft u een certificaat 'Overleven met gevaarlijk personeel'? J/N")
                                            vraag9m = input("")
                                            if vraag9m == "J" or vraag9m == "j" or vraag9m == "Ja" or vraag9m == "ja":
                                                print("Proficiat " + naam + "! U komt in aanmerking voor een sollicitatiegesprek, stuur snel uw CV")
                                                # (line 73) hier print de programma het eind resultaat als de gebruiker een man is die aan de juiste eisen heeft voldaan en MBO niveau 4 heeft gekozen
                                            else:
                                                print("U voldoet niet aan de juiste eisen.")
                                            #(else: print("U voldoet niet aan de juiste eisen."))
                                            # elke keer wanneer de gebruiker niet goed heeft beantwoord dan laat het programma de text uit printen "U voldoet niet aan de juiste eisen." 
                                        else:
                                            print("U voldoet niet aan de juiste eisen.")
                                    else:
                                        print("U voldoet niet aan de juiste eisen.")
                                else:
                                    print("Zorg ervoor dat u een snor heeft.")
                            elif (vraag6 == "j" or vraag6 == "J" or vraag6 == "Ja" or vraag6 == "ja") and (geslacht == "V" or geslacht == "v" or geslacht == "Vrouw" or geslacht == "vrouw"):
                                # (line 83) als de gebruiker j of ja heeft geantwoord en bij geslacht v of vrouw heeft gezet op line 14 dan gaat zij verder naar de vraag op line 85 
                                print("Welke kleur haar heeft u?")
                                vraag7v = input("")
                                if vraag7v == "rood" or vraag7v == "Rood":
                                    print("Wat voor soort haar heeft u? Krullen, stijl, etc.?")
                                    vraag8v = input("")
                                    if vraag8v == "krullen" or vraag8v == "Krullen":
                                        print("Hoelang is uw haar in hele cm?")
                                        vraag10v = int(input(""))
                                        if vraag10v >= 20:
                                            print("Heeft u een certificaat 'Overleven met gevaarlijk personeel? J/N")
                                            vraag9v = input("")
                                            if vraag9v == "J" or vraag9v == "j" or vraag9v == "Ja" or vraag9v == "ja":
                                                print("Proficiat " + naam + "! U komt in aanmerking voor een sollicitatiegesprek, stuur snel uw CV")
                                            else:
                                                print("U voldoet niet aan de juiste eisen.")
                                        else:
                                            print("U voldoet niet aan de juiste eisen.")
                                    else: 
                                        print("U voldoet niet aan de juiste eisen.")
                                else:
                                    print("U voldoet niet aan de juiste eisen.")
                            else:
                                print("U voldoet niet aan de juiste eisen.")
                        else:
                            print("U voldoet niet aan de juiste eisen.")
                    else:
                        print("U voldoet niet aan de juiste eisen.")
                else:
                    print("U voldoet niet aan de juiste eisen.")
            else:
                print("U voldoet niet aan de juiste eisen.")                        
        elif diploma2 == "HBO" or diploma2 == "Universiteit" or diploma2 == "Hbo" or diploma2 == "hbo" or diploma2 == "universiteit":
            #(line 116) als de gebruiker hbo of universiteit heeft beantwoord op line 30 dan gaat de gebruiker door naar de vraag op line 118
            print("Is uw opleiding gerelateerd op ondernemen? J/N")
            diplomaHU = input("")
            if diplomaHU == "J" or diplomaHU == "j" or diplomaHU == "Ja" or diplomaHU == "ja":
                print("Hoeveel jaar praktijkervaring heeft u met dieren-dressuur?")
                vraag1 = int(input(""))
                print("Hoeveel jaar praktijkervaring heeft u met jongleren?")
                vraag2 = int(input(""))
                print("Hoeveel jaar praktijkervaring heeft u met acrobatiek?")
                vraag3 = int(input(""))
                if vraag1 >= 4 or vraag2 >= 5 or vraag3 >= 3:
                    print("Bezit u een geldige vracht rijbewijs? J/N")
                    vraag5 = input("")
                    if vraag5 == "j" or vraag5 == "J" or vraag5 == "ja" or vraag5 == "Ja":
                        print("Bezit u een hoge hoed? J/N")
                        vraag6 = input("")
                        if (vraag6 == "j" or vraag6 == "J" or vraag6 == "ja" or vraag6 == "Ja") and (geslacht == "M" or geslacht == "m" or geslacht == "Man" or geslacht == "man"):
                            print("Heeft u gezichtsbeharing? J/N")
                            vraag7m = input("")
                            if vraag7m == "J" or vraag7m == "j" or vraag7m == "ja" or vraag7m == "Ja":
                                print("Wat voor soort gezichtsbeharing heeft u? Snor/baard/beide/geen")
                                vraag8m = input("")
                                if vraag8m == "snor" or vraag8m == "Snor":
                                    print("Hoe breed is uw snor in hele cm?")
                                    vraag10m = int(input(""))
                                    if vraag10m >= 10:
                                        print("Heeft u een certificaat 'Overleven met gevaarlijk personeel'? J/N")
                                        vraag9m = input("")
                                        if vraag9m == "J" or vraag9m == "j" or vraag9m == "Ja" or vraag9m == "ja":
                                            print("Proficiat " + naam + "! U komt in aanmerking voor een sollicitatiegesprek, stuur snel uw CV")
                                        else:
                                            print("U voldoet niet aan de juiste eisen.")
                                    else:
                                        print("U voldoet niet aan de juiste eisen.")
                                else:
                                    print("U voldoet niet aan de juiste eisen.")
                            else:
                                print("Zorg ervoor dat u een snor heeft.")
                        elif (vraag6 == "j" or vraag6 == "J" or vraag6 == "ja" or vraag6 == "Ja") and (geslacht == "V" or geslacht == "v" or geslacht == "Vrouw" or geslacht == "vrouw"):
                            print("Welke kleur haar heeft u?")
                            vraag7v = input("")
                            if vraag7v == "rood" or vraag7v == "Rood":
                                print("Wat voor soort haar heeft u? Krullen, stijl, etc.?")
                                vraag8v = input("")
                                if vraag8v == "krullen" or vraag8v == "Krullen":
                                    print("Hoelang is uw haar in hele cm?")
                                    vraag10v = int(input(""))
                                    if vraag10v >= 20:
                                        print("Heeft u een certificaat 'Overleven met gevaarlijk personeel? J/N")
                                        vraag9v = input("")
                                        if vraag9v == "J" or vraag9v == "j" or vraag9v == "Ja" or vraag9v == "ja":
                                            print("Proficiat " + naam + "! U komt in aanmerking voor een sollicitatiegesprek, stuur snel uw CV")
                                        else:
                                            print("U voldoet niet aan de juiste eisen.")
                                    else:
                                        print("U voldoet niet aan de juiste eisen.")
                                else:
                                    print("U voldoet niet aan de juiste eisen.")
                            else:
                                print("U voldoet niet aan de juiste eisen.")
                        else:
                            print("U voldoet niet aan de juiste eisen.")
                    else:
                        print("U voldoet niet aan de juiste eisen.")
                else:
                    print("U voldoet niet aan de juiste eisen.")
            else:
                print("U voldoet niet aan de juiste eisen.")
        else:
            print("U voldoet niet aan de juiste eisen.")
    else:
        print("U voldoet niet aan de juiste eisen.")
else:
    print("U voldoet niet aan de juiste eisen.")
