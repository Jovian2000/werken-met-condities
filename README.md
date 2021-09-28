# werken-met-condities
## F1.3.01.L1
### input en if-statement
```python
a = int(input("a = "))
b = int(input("b = "))
if a > b: 
    Max = a
    Min = b
    print("a is het grootste getal: " + str(Max))
```
### elif-statement
```python
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
```
### else-statement
```python
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
```
### Min en Max
```python
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
```
## F1.3.01.L2 
```python
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
```
## F1.3.01.O2
```python
print("---------------------------------------------")
print("         Welcome                             ")
print("You will enter a cave to steal               ")
print("a precious gem, but be carefull!             ")
print("This cave is extremely dangerous,            ")
print("one wrong way and you die!                   ")
print("---------------------------------------------")
print("Rules:")
print("Type correctly or you wil automatically")
print("choose the wrong path")
print("")
print("Enter your name")
name = input("Name: ")
print("")
print("Stage 1")
print("You find your self in the entrance of the dangerous cave. You enter the cave and you see 2 paths.")
print("They both have signs.")
print("The left one says this way for the gem an the right one says no entry.")
print("")
print("Which way are you choosing? Left/Right")
stage1 = input(name + ": ")
if stage1 == "Right" or stage1 == "right":
    print("")
    print(name + " choose the right path")
    print("")
    print("Stage 2")
    print("")
    print("Good job, obviously it would be a trap if you chose the obvious path.")
    print(name + " enters the right path and sees a room and at the end of the room a closed door.")
    print("There is a bucket with unlimited stones, an empty vase in the middle of the room")
    print("and on the wall you see a sign that says:")
    print("'Put the right ammount in the vase and the door will open.'")    
    print(name + " also sees: 'hint: 5 x 3 - 2 x 5 + 3'")
    print(name + " picks up some stones and put it in the vase.")
    print("")
    print("How many stones do you put in the vase?")
    stage2 = int(input(name + ": "))
    if stage2 == 8:
        print("")
        print(name + " put " + str(stage2) + " stones in the vase")
        print("")
        print("Stage 3")
        print("After " + name + " puts stones in the vase, the closed door slowly turns open.")
        print(name + " walks through the door and sees another room with an iron shield, a sword")
        print("and a bow and arrow. " + name + " picks up the weapons and walks further. Suddenly a giant")
        print("dragon appears. " + name + " took out his weapons and decided to take on the giant dragon.")
        print("")
        print("What is your first move? A/B" )
        print("A: Use your shield to charge forward and use the sword to strike the dragon")
        print("B: Use your bow and arrow to hit the dragon")
        stage3 = input(name + ": ")
        if stage3 == "A" or stage3 == "a":
            print("")
            print(name + " use the shield and sword")
            print("")
            print("Stage 4")
            print("After a succesfull hit, the dragon screamed and was ready to attack")
            print("from above. " + name + " use his shield to block some attacks and ")
            print("tries to dodge the heavy attacks. Now its time to use his bow.")
            print("")
            print("How many arrows will you shoot?")
            stage4 = int(input(name + ": "))
            if stage4 <= 4:
                print("")
                print(name + " use " + str(stage4) + " arrows")
                print("")
                print("Stage 5")
                print("After shooting the arrows, the dragon goes for another attack.")
                print(name + " managed to dodge because he didn't try to shoot too much.")
                print("The dragon landed back on the ground. It looks like he needs to rest")
                print("after the shots. Now is your chance to strike.")
                print("")
                print("How many strikes will you use with your sword?")
                stage5 = int(input(name + ": "))
                if stage5 >= 5:
                    print("")
                    print(name + " use " + str(stage5) + " strikes")
                    print("")
                    print("Stage 6")
                    print("Thats enough strikes, the dragon dies and " + name + " walks further.")
                    print("There is another room with 3 questions, it looks like you have to answer")
                    print("them correctly or else something bad will happen.")
                    print("")
                    print("First question: What is 3x3?")
                    stage6a = int(input(name + ": "))
                    print("")
                    print("Second question: What is 12x5?")
                    stage6b = int(input(name + ": "))
                    print("")
                    print("Third question: What is 32x13?")
                    stage6c = int(input(name + ": "))
                    if (stage6a == 9) and (stage6b == 60) and (stage6c == 416):
                        print("")
                        print(name + " answered " + str(stage6a) + ", " + str(stage6b) + " and " + str(stage6c))
                        print("")
                        print("Stage 7")
                        print("Thats the correct answers. The next door opens up and " + name + " enters the")
                        print("next room. There is another vase and a sign that says: 'Not more than pentagon")
                        print(name + " sees another bucket of stones and tries to fill the vase")
                        print("")
                        print("How many stones this time?")
                        stage7 = int(input(name + ": "))
                        if stage7 < 5:
                            print("")
                            print(name + " puts " + str(stage7) + " stones in the vase")
                            print("")
                            print("Stage 8")
                            print("Good job! Pentagon means something with 5, so that means not more than 5.")
                            print("The next door opens and " + name + " sees a room with 2 paths again.")
                            print("This time there is only 1 sign that says:'Only 1 way correct'.")
                            print("")
                            print("Which way are you going? Left/Right")
                            stage8 = input(name + ": ")
                            if stage8 == "Left" or stage8 == "left":
                                print("")
                                print(name + " choose the left path")
                                print("")
                                print("Stage 9")
                                print("It looks like this is the good path, nothing bad happened")
                                print(name + " sees another closed door. There is a lock and you need")
                                print("to put the right code to open it.")
                                print("")
                                print("What is the code? (hint: the numbers you saw earlier in the game)")
                                stage9 = input(name + ": ")
                                if stage9 == "960416":
                                    print("")
                                    print(name + " type: " + stage9)
                                    print("")
                                    print("Stage 10")
                                    print("Nice! It looks like thats the right code. The door opens.")
                                    print("Another room with a stone guard in front of the last door.")
                                    print("The guard says: 'Intruder!'. The stone guard attacks, but")
                                    print("luckily you have your weapons.")
                                    print("")
                                    print("What is your next move? A/B/C")
                                    print("A: Use sword to strike the guard")
                                    print("B: Use shield to charge")
                                    print("C: Use bow and arrow to shoot")
                                    stage10 = input(name + ": ")
                                    if stage10 == "B" or stage10 == "b":
                                        print("")
                                        print(name + " used shield to charge")
                                        print("")
                                        print(name + " charged the guard and the guard instantly breaks into pieces.")
                                        print("After the guard dies, " + name + " sees the open door that was behind")
                                        print("the guard. " + name + " entered the last room and sees the gem." )
                                        print(name + " picks up the gem and leaves the dangerous cave.")
                                        print("")
                                        print("The end!")
                                        print("")
                                        print("Congratulations!!!!")
                                        print(name + " succesfully stole the gem!")
                                    elif stage10 == "A" or stage10 == "a":
                                        print("")
                                        print(name + " used sword to strike")
                                        print("")
                                        print(name + " strikes the guard multiple times but because of the stone skin,")
                                        print("the sword broke. After the sword broke, the guard attacks with his hammer.")
                                        print("The guard hit " + name + " and " + name + " dies.")
                                        print("")
                                        print("Game over!")
                                    else:
                                        print("")
                                        print(name + " used bow and arrow to shoot")
                                        print("")
                                        print(name + " shoots the guard, but its ineffect because of the stone skin. ")
                                        print("The guard hit " + name + " with a hammer and " + name + " dies.")
                                        print("")
                                        print("Game over!")
                                else:
                                    print("")
                                    print(name + " type: " + stage9)
                                    print("")
                                    print("Thats the wrong code!")
                                    print("The room explodes instantly and " + name + " dies!")
                                    print("")
                                    print("Game over!")   
                            else:
                                print("")
                                print(name + " choose the right path")
                                print("")
                                print("Thats the wrong path." + name + " gets attacked by poisoned bats")
                                print(name + " dies because of the poison")
                                print("")
                                print("Game over!")
                        else:
                            print("")
                            print(name + " puts " + str(stage7) + " stones in the vase")
                            print("")
                            print("Thats too much!")
                            print("Pentagon means something with 5, so that means not more than 5.")
                            print("The room starts to collapse and " + name + " dies!")
                            print("")
                            print("Game over!")
                    else:
                        print("")
                        print(name + " answered " + str(stage6a) + ", " + str(stage6b) + " and " + str(stage6c))
                        print("")
                        print("Thats the wrong answer(s). Suddenly the room gets filled with lava and")
                        print(name + " can't see a way out and dies.")
                        print("Game over!")
                else:
                    print("")
                    print(name + " use " + str(stage5) + " strikes")
                    print("")
                    print("Thats not enough! The dragon wakes up and bites " + name + " lower half.")
                    print(name + " can't do anything, bleeds out and dies.")
                    print("")
                    print("Game over!")
            else:
                print("")
                print(name + " use " + str(stage4) + " arrows")
                print("")
                print(name + " shoots his arrows, but the dragon attacks and " + name + " was")
                print("too focused with his shots. Because " + name + " tries to shoot so many,")
                print("the dragon managed to hit him hard and " + name + " died.")
                print("")
                print("Game over!")
        else:
            print("")
            print(name + " use the bow and arrow")
            print("")
            print("After trying to shoot, the dragon spit fire and burns " + name + ".")
            print("")
            print("Game over!") 
    elif stage2 > 8:
        print("")
        print(name + " put " + str(stage2) + " stones in the vase")
        print("")
        print("Thats too much!")
        print("Suddenly the room starts to collapse. " + name + " tries to run but " + name + " was too late")
        print("to run away. " + name + " got hit by a couple of falling rocks and dies")
        print("")
        print("Game over!")
    else:
        print("")
        print(name + " put " + str(stage2) + " stones in the vase")
        print("")
        print("Thats not enough!") 
        print("The ground opens up and " + name + " falls in a sea of lava")
        print("")
        print("Game over!")
else:
    print("")
    print(name + " choose the left path")
    print("")
    print(name + " enters the left path and suddenly a giant rock falls from above.")
    print("It was impossible to dodge the giant rock.")
    print("It appears the sign was a trap for anyone who tries to steal the gem.")
    print("")
    print("Game Over!")
```