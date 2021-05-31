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
    return texto 

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