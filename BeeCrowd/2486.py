while True:
    try:
        mgalimentos = {
            "sucodelaranja" : 120,
            "morangofresco" : 85,
            "mamao" : 85,
            "goiabavermelha" : 70,
            "manga" : 56,
            "laranja" : 50,
            "brocolis" : 34,
        }

        calorias = 0
        alimentos = []
        indice = 0
        numalimentos = int(input(""))
        if numalimentos > 0:
            for i in range(0, numalimentos):
                entrada = input().split()
                qntd = entrada[0]
                opc= "".join(entrada[1:])
                calorias += mgalimentos[opc]* int(qntd)
            
            if calorias > 130:
                indicado = calorias-130
                print(f"Menos {indicado} mg")
            elif calorias < 110:
                indicado = calorias-110
                print(f"Mais {abs(indicado)} mg")
            else:
                print(f"{calorias} mg")
    except EOFError:
        break