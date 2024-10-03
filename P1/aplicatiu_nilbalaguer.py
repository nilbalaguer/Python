#Tres Jocs
#Importar coses
import random

#Jocs
def num10():
    numero = random.randint(1,10)
    cont = 0
    adivinado = False
    print("Endivina el numero:")

    while (cont < 3):
        print(f"{cont+1} intento")

        prueba = int(input(": "))
        if (prueba == numero):
            adivinado = True
            cont = 4
        elif (prueba >= numero):
            print("Masa Gran")
        elif (prueba <= numero):
            print("Masa Petit")
        cont += 1

    if (adivinado == True):
        print("Felicitats Has Endivinat El Numero!!!")
    else:
        print("Has fallado vuelve a intentarlo")

def pedrapapertisores():
    puntosplayer = 0
    puntosb = 0
    while (puntosplayer < 2 and puntosb < 2):
        numero = random.randint(1,3)
        select = int(input("1-Pedra 2-paper 3-tisora: "))
        if (numero == 1 and select == 1):
            print("Pedra ambdos")
        elif (numero == 1 and select == 2):
            print("Paper guanya a pedra +1")
            puntosplayer += 1
        elif (numero == 1 and select == 3):
            print("Pedra guanya a tisora -1")
            puntosb += 1

        elif (numero == 2 and select == 1):
            print("Paper guanya a tisora -1")
            puntosb += 1
        elif (numero == 2 and select == 2):
            print("Paper ambdos")
        elif (numero == 2 and select == 3):
            print("Tisora guanya a paper +1")
            puntosplayer += 1

        elif (numero == 3 and select == 1):
            print("Pedra guanya a tisora +1")
            puntosplayer += 1
        elif (numero == 3 and select == 2):
            print("Tisora guanya a paper -1")
            puntosb += 1
        elif (numero == 3 and select == 3):
            print("Ambdos Tisora")

    if (puntosplayer > 2):
        print("Has Guanyat!!!")
    else:
        print("Has Perdut")

def elpenjat():
    print("El Penjar (Sense accens)")

    #Carrega el arxiu
    print("Carregant paraules...")
    f = open("elpenjat.csv", "r")
    raw = f.read()
    f.close
    paraules = raw.split(",")
    if len(paraules) > 0:
        print("Paraules carregades")
    else:
        print("Error en la carrega, no paraules o no s'ha trobat el fitxer")


    paraula = paraules[random.randint(0, len(paraules)-1)]
    intents = 2*len(paraula)

    adivinado = []

    contb = 1

    adivinado.append(paraula[0])
    while (contb < len(paraula)):
        adivinado.append("")
        contb += 1

    casa = 0
    contc = 0
    while intents > contc:
        conta = 0
        casa = 0
        rest = ""
        while conta < len(paraula):
            if adivinado[conta] == paraula[conta]:
                rest += paraula[conta]
                casa += 1
            else:
                rest += "_"

            conta += 1


        print(f"""
        Longitud de la Paraula a endivinar: {len(paraula)}
        Intents restants: {intents-contc}
        {rest}
        """)

        if (casa >= len(paraula)):
            print(f"Felicitats!! has endivinat la paraula {paraula}")
            contc = intents
        else:
            intento = input("Introdueix una lletra: ")

            if (paraula[casa] == intento):
                adivinado[casa] = intento
                print("Lletra correcta!!")
            else:
                print("Lletra incorrecta")

        contc += 1

    if (intents/2 > casa):
        print(f"Has fallat endivinant la paraula {paraula}")


#Imprimeix el missatge de benvinguda
print("""
      Escull un dels 3 Jocs disponibles:
      1 - Fins al Numero 10
      2 - Pedra Paper Tisores
      3 - El Penjat
      4 - Sortir del Programa
      """)

#Executa el joc seleccionat
executar = True
while (executar):
    seleccio = input(": ")

    if (seleccio == "1"):
        num10()
    elif (seleccio == "2"):
        pedrapapertisores()
    elif (seleccio == "3"):
        elpenjat()
    elif (seleccio == "4"):
        executar = False