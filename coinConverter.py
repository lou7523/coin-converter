print("Welcome to the coin converter!\n==============================\nInsert your coin value:")
coin = float(input())

print("Choose your currency: (Yuan, Dollar, Krone, Real, PesoArg)")
currency = str(input())
match currency:
    case "Yuan" | "yuan": 
        yuan = coin * 7.48
        print(f"You have:\n\n\t{yuan:.2f} Yuan")
    case "Dollar" | "dollar" | "dol" | "usd":
        dollar = coin * 1.12
        print(f"You have:\n\n\t{dollar:.2f} Dollars")
    case "Krone" | "Danish Krone" | "dkk":
        danishKrone = coin * 7.47
        print(f"You have:\n\n\t{danishKrone:.2f} Krones")
    case "real" | "reais" | "pila":
        real = coin * 5.58
        print(f"You have:\n\n\t{real:.2f} Reais")
    case "peso" | "peso argentino" | "pesos" | "Peso Argentino" | "PesoArg":
        pesoArgentino = coin * 1706.45
        print(f"You have:\n\n\t{pesoArgentino:.2f} Pesos")
    case _:
        print("Sorry currency not suported yet!")

