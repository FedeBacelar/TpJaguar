def Puntaje(Aciertos,Desaciertos,Puntos=0):
    Puntos += (Aciertos*10 - Desaciertos*5)
    return Puntos

def SeguirJuego():
    seguir = str(input("Desea seguir jugando? (s/n)"))
    return seguir.lower() == "s"