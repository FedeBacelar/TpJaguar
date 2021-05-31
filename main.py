from texto import obtener_texto
from Etapa1 import CorrerJuego
from Etapa2 import GenerarDiccionario
from Etapa3 import elegirPalabra,LongitudOpcional
from Etapa5 import Puntaje, SeguirJuego

def main():
    Puntos= 0
    Diccionario = GenerarDiccionario()
    seguir = True
    while seguir:
        PalabraParaAdivinar = elegirPalabra(Diccionario,LongitudOpcional())
        Puntuacion = CorrerJuego(PalabraParaAdivinar,Puntos)
        Puntos = Puntuacion[2]
        seguir = SeguirJuego()
main()

