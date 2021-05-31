#Se comienza generando el diccionario (etapa 2) LISTO
#Se sigue con la eleccion de palabra (etapa3)
#Se comienza a adivinar la palabra (etapa1)
import random
from texto import obtener_texto

def separar(texto, palabra):
    """
    Funciona junto a desmembrar: retorna una lista de palabras separadas
    Firma: Alejo
    """
    return texto.split(palabra)

def desmembrar(texto):
    """
    Desmembra el texto devolviendo solamente palabras
    Firma: Alejo
    """
    caracteres_posibles = [",", ".", "?", "¿", "!", "¡", ";", ".", "_", "-", ":", "\n"]
    for i in range(len(caracteres_posibles)):
        texto = separar(texto, caracteres_posibles[i])
        texto = " ".join(texto)
    texto = texto.split()
    return texto #Retorna el texto con todas las palabras

def EliminarAcentosYMayusculas(Palabra):
    """
    Recibe como parametro una palabra para luego eliminarle los acentos y mayusculas
    """
    remplazar = (("á", "a"),("é", "e"),("í", "i"),("ó", "o"),("ú", "u"))
    for a,b in remplazar:
        Palabra = Palabra.replace(a,b).replace(a.upper(),b.upper())
    return(Palabra.lower())

def ListaDePalabrasSinRepetir(Texto):
    """
    Recibe una lista de palabras. Retorna la misma obviando las palabras repetidas
    """
    NuevaLista = []
    for Palabra in Texto:
        NuevaLista.append(Palabra) if NuevaLista.count(Palabra) == 0 and Palabra.isalpha() else None
    return NuevaLista

def GenerarClaves(Texto):
    """
    Proporciona mediante una lista de palabras, 'claves' para ser utilizadas en un diccionario
    """
    LONGITUD_MAXIMA = 5
    Texto = ListaDePalabrasSinRepetir(Texto)
    return [Palabra for Palabra in Texto if (Palabra.isalpha and len(Palabra) >= LONGITUD_MAXIMA)] 

def GenerarValores(Texto):
    """
    Genera las claves de nuestro diccionario: lista con la cantidad de veces que se repite cada palabra
    """
    return [Texto.count(Palabra) for Palabra in ListaDePalabrasSinRepetir(Texto) if (Palabra.isalpha and len(Palabra) >= 5)]

def dicPalabrasCandidatas(Texto):
    """
    Recibe como parametro un texto
    Arma un diccionario utilizando como clave cada palabra en un texto y como valor las veces repetidas
    """
    Diccionario = dict(zip(tuple(GenerarClaves(Texto)), tuple(GenerarValores(Texto))))
    return Diccionario

def OrdenarClaves(Diccionario):
    """
    Recibe un diccionario como parametro
    Ordena las claves alfabeticamente retornando una lista con las mismas
    """
    keys = list(Diccionario.keys())
    keys.sort(key = EliminarAcentosYMayusculas)
    return keys

def OrdenarDiccionario(Diccionario):
    """
    Recibe como parametro un diccionario
    Ordena el diccionario segun sus claves; las mismas ordenadas alfabeticamente
    """
    NuevoDiccionario = {}
    for key in OrdenarClaves(Diccionario):
        NuevoDiccionario[key.lower()] = Diccionario[key]
    return NuevoDiccionario


"""def CaracteristicasDelDiccionario(Diccionario):
    print("Hay {} palabras en el diccionario. Las cuales son: ".format(len(Diccionario)))
    for Palabra in Diccionario:
        print("{} : Cantidad repetida: {}".format(Palabra, Diccionario[Palabra]))

Funcion fuera de servicio: Muestra caracteristicas del diccionario        
"""
def GenerarDiccionario():
    texto_a_procesar = desmembrar(obtener_texto())
    Diccionario = dicPalabrasCandidatas(texto_a_procesar)
    Diccionario = (OrdenarDiccionario(Diccionario))
    return Diccionario
    #CaracteristicasDelDiccionario(Diccionario)



#              Fin Etapa 2 INTEGRADA


def ExtraerPalabrasCondicionadas(Lista, Longitud):
    """
    Toma como parametros una lista de palabras y una longitud
    Retorna una lista palabras que cumplan con la longitud especificada
    """
    ListaCondicionada = [palabra for palabra in Lista if len(palabra) == Longitud]
    return ListaCondicionada

def elegirPalabra(Diccionario, Longitud=None):
    """
    Toma como parametro una lista y una condicion de longitud; si no se detalla, la misma sera ignorada.
    Si se ingresa un numero menor a la longitud maxima(5) se ignora la condicion
    Retorna una palabra aleatoria de un diccionario
    """
    Lista = list(Diccionario.keys())
    LONGITUD_MINIMA = 5
    if Longitud: #Si se ingreso una Longitud
        Longitud = LONGITUD_MINIMA if Longitud <= LONGITUD_MINIMA else Longitud
        Lista = ExtraerPalabrasCondicionadas(Lista, Longitud)
    #Una vez obtenida la lista con palabras candidatas a elegir
    palabraElegida = random.choice(Lista)
    return palabraElegida

def LongitudOpcional():
    """
    Condiciona el uso de parametros en la funcion elegirPalabra
    """
    Condicion = str(input("Desea condicionar la longitud de la palabra a adivinar? (s/n): "))
    if Condicion.lower() == "s":
        return int(input("Ingrese Longitud (Si el numero ingresado es menor a la longitud minima(5) se tomara el valor minimi): "))
    
#             Fin Etapa 3 INTEGRADA


def MensajeDelResultado(PalabraParaAdivinar, cadenaOculta):
    """
    Retorna un mensaje al finalizar el juego    
    """
    return "FELICIDADES!!! LA PALABRA ERA " + PalabraParaAdivinar if PalabraParaAdivinar == "".join(cadenaOculta) else "PERDISTE!! LA PALABRA ERA "+ PalabraParaAdivinar +" BUENA SUERTE LA PROXIMA!!!"

def salidaAnticipada(Caracter):
    """
    Valida si el usuario quiere salir del juego
    """
    return (Caracter.upper() == 'FIN' or Caracter == '0')

def ValidarCaracter(caracter, PalabraParaAdivinar):
    """
    Valida que el caracter ingresado este en la palabra a adivinar
    """
    return(PalabraParaAdivinar.find(caracter) != -1 and caracter != "")

def Mensaje(caracter, PalabraParaAdivinar):
    """
    Imprime un mensaje para el juego
    """
    if not caracter:
        Mensaje = "Palabra a adivinar: "
    elif ValidarCaracter(caracter, PalabraParaAdivinar):
        Mensaje = "Muy Bien!!! "
    else:
        Mensaje = "Lo siento!!! "
    return(Mensaje)

def armadoDeCadenas(lista):
    """
    Arma una cadena
    """
    cadena = ""
    for letra in lista:
        cadena += letra
    return cadena

def separarLetrasDeCadena(PalabraParaAdivinar):
    """
    Arma una lista de separando los caracteres de la palabra a adivinar
    """
    return [letra for letra in PalabraParaAdivinar]

def repetido(caracter,cadenaOculta, caracteresErrados):
    """
    Evalua si se ingreso caracteres repetidos
    """
    return (caracter in separarLetrasDeCadena(cadenaOculta) or caracter in caracteresErrados)

def RevelarCadena(caracter, cadenaOculta, PalabraParaAdivinar):
    """
    Revela la cadena en los caracteres descubiertos
    """
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
    """
    Arma una cadena censurada
    """
    return "?"*len(PalabraParaAdivinar)

def contarAciertos(aciertos,caracter, PalabraParaAdivinar):
    """
    Cuenta los aciertos
    """
    if ValidarCaracter(caracter, PalabraParaAdivinar):
        aciertos += 1
    return aciertos

def contarDesaciertos(desaciertos, caracter, PalabraParaAdivinar, caracteresErrados):
    """
    Cuenta los desaciertos
    """
    if not ValidarCaracter(caracter, PalabraParaAdivinar):
        desaciertos += 1
        caracteresErrados += "-" + caracter if caracter != "" else ""
    return [desaciertos, caracteresErrados]

def Contador(aciertos, desaciertos, caracteresErrados):
    """
    Arma un contador con las caracteristicas de la partida
    """
    Puntos = " Aciertos: " + str(aciertos) + " Desaciertos: " + str(desaciertos) + caracteresErrados
    return(Puntos)

def ingreso(cadenaOculta, caracteresErrados):
    """
    Evalua los ingresos
    """
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

def CorrerJuego(PalabraAdivinar,Puntos):
    """
    Inicia la partida
    """
    PalabraParaAdivinar = EliminarAcentosYMayusculas(PalabraAdivinar)
    caracter = ""
    aciertos = 0
    desaciertos = 0
    caracteresErrados = ""
    cadenaOculta = CensuraTotal(PalabraParaAdivinar)

    while desaciertos <= 7 and not salidaAnticipada(caracter) and cadenaOculta.count("?") != 0 :
        
        PuntosEnPartida = Puntaje(aciertos,desaciertos) + Puntos
        print(Mensaje(caracter, PalabraParaAdivinar) + "--> "  + cadenaOculta + Contador(aciertos, desaciertos, caracteresErrados) + " Puntos:" + str(PuntosEnPartida))
        caracter = ingreso(cadenaOculta, caracteresErrados)
        cadenaOculta = RevelarCadena(caracter, cadenaOculta, PalabraParaAdivinar)
        aciertos = contarAciertos(aciertos, caracter, PalabraParaAdivinar)
        desaciertos = contarDesaciertos(desaciertos, caracter, PalabraParaAdivinar, caracteresErrados)[0]
        caracteresErrados = contarDesaciertos(desaciertos, caracter, PalabraParaAdivinar, caracteresErrados)[1]
    print(MensajeDelResultado(PalabraParaAdivinar, cadenaOculta))
    return([aciertos,desaciertos, PuntosEnPartida])

#             Fin  Etapa 1 INTEGRADA

def Puntaje(Aciertos,Desaciertos,Puntos=0):
    Puntos += (Aciertos*10 - Desaciertos*5)
    return Puntos

def SeguirJuego():
    seguir = str(input("Desea seguir jugando? (s/n)"))
    return seguir.lower() == "s"



def main():
    Puntos= 0
    Diccionario = GenerarDiccionario()
    seguir = True
    while seguir:
        PalabraParaAdivinar = elegirPalabra(Diccionario,LongitudOpcional())
        Puntuacion = CorrerJuego(PalabraParaAdivinar,Puntos)
        Puntos = Puntuacion[2]
        seguir = SeguirJuego()
    


#ERORR: palabras con tildesssss:
#Ya corre bien pero se tiene que mostrar las palabras con los tildes mientras se revela la cadena
main()
