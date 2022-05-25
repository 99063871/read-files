import zakelijk
import yaml

with open('settings.yml', 'r') as file:
    settings = yaml.safe_load(file)

errorMessages = "Sorry dat is geen optie die we aanbieden..."

print("Welkom bij Papi Gelato.")
def whoFunc():
    who = input("Bent u 1) particulier of 2) zakelijk?")
    if who == "1":

        def welkeSmaakFunc():
            for a in range(1, int(amount)+1):
                smaak = input("Welke smaak wilt u voor bolletje nummer "+ str(a) +"? A) Aardbei, C) Chocolade of V) Vanille?").lower()
                if smaak != 'a' and smaak != 'c' and smaak != 'v':
                    a=0
                    smaak=0
                    print(errorMessages)
                    welkeSmaakFunc()

        def papiGelatoFunc():
            global amount, bakOfhoorn
            amount = input("Hoeveel bolletjes wilt u?")
            settings["bolletjesAmount"] += int(amount)
            if amount < "9":
                welkeSmaakFunc()
            if amount <= "3":
                inWhat()
            elif amount >= "4" and amount <= "8":
                bakOfhoorn = 'bakje'
                settings["bakjesAmount"] +=1
                toppingFunc()
                orderMoreFunc()
            elif amount > "8" and amount == int:
                print("Sorry, zulke grote bakken hebben we niet")
                papiGelatoFunc()
            else:
                print(errorMessages)
                papiGelatoFunc()

        def orderMoreFunc():
            another = input("Hier is uw " + bakOfhoorn + " met " + amount + " bolletje(s). Wilt u nog meer bestellen? (Y/N)")
            if another == "y":
                papiGelatoFunc()
            elif another == "n":
                print("Bedankt en tot ziens!")
                bonnetje()
            elif another !="y" or another != "n":
                print(errorMessages)
                orderMoreFunc()

        def inWhat():
            global bakOfhoorn
            bakOfhoorn = input("Wilt u deze " + str(amount) + " bolletje(s) in \nA) een hoorntje of \nB) een bakje?")
            if bakOfhoorn != "a" and bakOfhoorn != "b":
                print(errorMessages)
                inWhat()
            else:
                if bakOfhoorn == "a":
                    bakOfhoorn = "hoorntje"
                    settings["hoorentjesAmount"] += 1
                    toppingFunc()
                elif bakOfhoorn == "b":
                    bakOfhoorn = 'bakje'
                    settings["bakjesAmount"] += 1
                    toppingFunc()
                orderMoreFunc()
                
        def toppingFunc():
            topping = input("Wat voor topping wilt u: A) Geen, B) Slagroom, C) Sprinkels of D) Caramel Saus?").lower()
            if topping != "a":
                if topping == "b":
                    settings["toppingTotalPrice"] += settings["toppings"]["slagroom"]
                    settings["toppingTotal"] +=1
                elif topping == "c":
                    settings["toppingTotalPrice"] += settings["toppings"]["sprinkles"] * settings["bolletjesAmount"]
                    settings["toppingTotal"] +=1
                elif topping == "d":
                    if bakOfhoorn == "bakje":
                        settings["toppingTotalPrice"] += settings["toppings"]["caramel"]["bakje"] * settings["bolletjesAmount"]
                        settings["toppingTotal"] +=1
                    else:
                        settings["toppingTotalPrice"] += settings["toppings"]["caramel"]["hoorentje"] * settings["bolletjesAmount"]
                        settings["toppingTotal"] +=1
                    if bakOfhoorn == "hoorntje":
                        settings["toppingTotalPrice"] += settings["hoorentjes"]
                    elif bakOfhoorn == "bakje":
                        settings["toppingTotalPrice"] += settings["bakjes"]
                else:
                    print(errorMessages)
                    toppingFunc()

        def bonnetje():
            if settings["bolletjesAmount"] != 0:
                bolletjesTotal = settings["bolletjesAmount"]*settings["bolletjes"]
                horrentjeTotal = settings["hoorentjesAmount"]*settings["hoorentjes"]
                bakjeTotal = settings["bakjesAmount"]*settings["bakjes"]
                total = bolletjesTotal + horrentjeTotal + bakjeTotal + settings["toppingTotalPrice"]
                print('---------["Papi Gelato"]---------\n')
                print('Bolletjes     ',settings["bolletjesAmount"], ' x €',str(settings["bolletjes"]) + '=€',round(bolletjesTotal, 2))
                if settings["hoorentjesAmount"] != 0:
                    print('Horrentje     ',settings["hoorentjesAmount"], ' x €',str(settings["hoorentjes"]) + '=€',round(horrentjeTotal, 2))
                elif settings["bakjesAmount"] != 0:
                    print('Bakje         ',settings["bakjesAmount"], ' x €',str(settings["bakjes"]) + '=€',round(bakjeTotal, 2))
                if settings["toppingTotal"] != 0:
                    print('Topping        1  x €', round(settings["toppingTotalPrice"]),   '  =€',round(settings["toppingTotalPrice"], 2))
                    
                print('                           -------- +')
                print('Totaal                      =€',round(total, 2))

        papiGelatoFunc()

    elif who == "2":
        zakelijk.zakelijk()
    else:
        print(errorMessages)
        whoFunc()

whoFunc()
input("klik op enter om verder te gaan")