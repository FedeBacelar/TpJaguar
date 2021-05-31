
def MensajeDelResultado(PalabraParaAdivinar, cadenaOculta):
    return "FELICIDADES!!! LA PALABRA ERA " + PalabraParaAdivinar if PalabraParaAdivinar == "".join(cadenaOculta) else "PERDISTE!! LA PALABRA ERA "+ PalabraParaAdivinar +" BUENA SUERTE LA PROXIMA!!!"

def salidaAnticipada(Caracter):
    return (Caracter.upper() == 'FIN' or Caracter == '0')

def ValidarCaracter(caracter, PalabraParaAdivinar):
    return(PalabraParaAdivinar.find(caracter) != -1 and caracter != "")

def Mensaje(caracter, PalabraParaAdivinar):
    Mensaje = ""
    if not caracter:
        Mensaje = "Palabra a adivinar: "
    elif ValidarCaracter(caracter, PalabraParaAdivinar):
        Mensaje = "Muy Bien!!! "
    else:
        Mensaje = "Lo siento!!! "
    return(Mensaje)

def armadoDeCadenas(lista):
    cadena = ""
    for letra in lista:
        cadena += letra
    return cadena

def separarLetrasDeCadena(PalabraParaAdivinar):
    return [letra for letra in PalabraParaAdivinar]

def repetido(caracter,cadenaOculta, caracteresErrados):
    return (caracter in separarLetrasDeCadena(cadenaOculta) or caracter in caracteresErrados)

def RevelarCadena(caracter, cadenaOculta, PalabraParaAdivinar):
    cadenaFinal = ""
    i = 0
    if ValidarCaracter(caracter, PalabraParaAdivinar):
        cadena = separarLetrasDeCadena(PalabraParaAdivinar)
        cadenaOculta = separarLetrasDeCadena(cadenaOculta)
        for char in cadenaOculta:
            if char == "?" and caracter == cadena[i]:
                cadenaOculta[i] = caracter
            i += 1
        cadenaFinal = armadoDeCadenas(cadenaOculta)
    else:
        cadenaFinal = cadenaOculta
    return cadenaFinal

def CensuraTotal(PalabraParaAdivinar):
    return "?"*len(PalabraParaAdivinar)

def contarAciertos(aciertos,caracter, PalabraParaAdivinar):
    if ValidarCaracter(caracter, PalabraParaAdivinar):
        aciertos += 1
    return aciertos

def contarDesaciertos(desaciertos, caracter, PalabraParaAdivinar, caracteresErrados):
    if not ValidarCaracter(caracter, PalabraParaAdivinar):
        desaciertos += 1
        caracteresErrados += "-" + caracter if caracter != "" else ""
    return [desaciertos, caracteresErrados]

def Contador(aciertos, desaciertos, caracteresErrados):
    Puntos = " Aciertos: " + str(aciertos) + " Desaciertos: " + str(desaciertos) + caracteresErrados
    return(Puntos)

def ingreso(cadenaOculta, caracteresErrados):
    caracter = str(input("Ingrese Letra_ "))
    if (not (caracter.isalpha() and len(caracter) == 1)) and not(salidaAnticipada(caracter)):
        while not (caracter.isalpha() and len(caracter) == 1) and not(salidaAnticipada(caracter)):
            print("Ingreso invalido: Solo se permiten Letras")
            caracter = str(input("Ingrese Letra_ "))
    elif repetido(caracter, cadenaOculta, caracteresErrados):
        while repetido(caracter,cadenaOculta, caracteresErrados) or not (caracter.isalpha() and len(caracter) == 1) and not(salidaAnticipada(caracter)):
            print("Letra repetida, por favor vuelva a ingresar nueva letra")
            caracter = str(input("Ingrese Letra_ "))
    return caracter.lower()

def CorrerJuego(PalabraParaAdivinar):
    caracter = ""
    aciertos = 0
    desaciertos = 0
    caracteresErrados = ""
    cadenaOculta = CensuraTotal(PalabraParaAdivinar)

    while desaciertos <= 7 and not salidaAnticipada(caracter) and cadenaOculta.count("?") != 0 :
        
        print(Mensaje(caracter, PalabraParaAdivinar) + "--> "  + cadenaOculta + Contador(aciertos, desaciertos, caracteresErrados))
        caracter = ingreso(cadenaOculta, caracteresErrados)
        cadenaOculta = RevelarCadena(caracter, cadenaOculta, PalabraParaAdivinar)
        aciertos = contarAciertos(aciertos, caracter, PalabraParaAdivinar)
        desaciertos = contarDesaciertos(desaciertos, caracter, PalabraParaAdivinar, caracteresErrados)[0]
        caracteresErrados = contarDesaciertos(desaciertos, caracter, PalabraParaAdivinar, caracteresErrados)[1]
    print(MensajeDelResultado(PalabraParaAdivinar, cadenaOculta))


CorrerJuego("mariposa")

'''
Ingreso() capaz se puede modularizar mas (condiciones repetidas y no tan legible)
'''

