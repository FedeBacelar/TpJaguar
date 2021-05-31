import random

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
        return int(input("Ingrese Longitud (Si el numero ingresado es menor a la longitud minima(5) se tomara el valor minima): "))
 