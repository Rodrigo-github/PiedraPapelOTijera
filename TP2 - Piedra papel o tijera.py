#Juego: Piedra-Papel-Tijera
#Consigna:
#Cree la clase Persona, el método estático mostrarPersona(), que devuelve aleatoriamente una de las cadenas de piedra, 
# papel o tijera; cree la clase Computadora, el método de clase mostrarCompu(),
# Devuelve aleatoriamente uno de los resultados: de piedra, papel, tijera; crea la clase Juego, los atributos de clase del 
# objeto Persona y el objeto Computadora, y el método de clase ComenzarJuego().
# Muestre resultado de cada partida y muestre si la computadora gana o la persona gana o fue empate

#El usuario tiene que poder elegir: Piedra, Papel o Tijera para jugar en cada partida y se juegan 3 rondas para tener el resultado final

#Persona
#-mostrarPersona() - recibe elección de usuario

#Computadora
#-mostrarCompu() - devuelve resultado

#Juego - derivada de persona y computadora
#-comenzarJuego() - muestra resultado y ganador

#3 rondas en total (necesitaré un contador)

import random

class Persona(object): #clase a cargo de los movimientos del usuario, recibidos por teclado
    def __init__(self):
        self=self

    def mostrarPersona(self): #Declaración de métodos
        auxp = ""
        x = 0
        while x != 1 and x != 2 and x != 3:
            x = int(input("Elija piedra (1), papel (2) o tijera (3). \n"))
            if x == 1:
                auxp = "piedra"
                print("Eligió piedra.")
            elif x == 2:
                auxp = "papel"
                print("Eligió papel.")
            elif x == 3:
                auxp = "tijera"
                print("Eligió tijera.")
            else:
                print("Error, por favor ingrese un valor válido.")
                #no cambio el valor de auxp para que el ciclo continúe

        return auxp

class Computadora(object): #clase a cargo de los movimientos de la computadora (al azar)
    def __init__(self):
        self=self

    def mostrarCompu(self): #Declaración de métodos
        x = random.randrange(1, 4)#el 4 no está incluido por lo que solo da 1, 2 o 3
        #transformo el número al azar en una cadena
        if x == 1:
            auxc = "piedra"
        elif x == 2:
            auxc = "papel"
        elif x == 3:
            auxc = "tijera"
        
        print("La computadora eligió " + auxc + ".")
        return auxc

class Juego(Persona, Computadora):#clase a cargo de dar inicio al juego
    def __init__(self):
        self=self

    def comenzarJuego(self):
        #nuestro contador
        turnos = 1

        #contador de puntos
        contadorPuntos = 0
        #ya que los puntos a favor de la persona son positivos y los a favor de la máquina son negativos, puedo saber quien ganó con una sola cifra

        #variables auxiliares que guarda los movimientos elegidos

        while turnos < 4:
            print("Turno", turnos)
            Persona1 = Persona()
            auxp = Persona1.mostrarPersona()
            Computadora1 = Computadora()
            auxc = Computadora1.mostrarCompu()
            MarcadorNuevo = Marcador()#crear un partida nuevo crea un marcador nuevo
            contadorPuntos += MarcadorNuevo.Contar(auxp,auxc)
            turnos +=1

            if turnos == 4:#una manera poco elegante de reemplazar la línea en el último turno
                MarcadorNuevo.Ganador(contadorPuntos)
                print("//-----//-GRACIAS POR JUGAR-//-----//")
                break

            print("//-----//-----//-----//-----//-----//")
    

class Marcador(object):#clase que mantiene el cálculo de los puntos y estado de la partida
    def __init__(self):
        self=self

    def Contar(self, persona, compu):
        contadorPuntos = 0

        #si elijo piedra
        if persona == "piedra":
            if compu == "piedra":
                print("Empate.")
            if compu == "papel":
                print("Punto para la computadora.")
                contadorPuntos -=1
            if compu == "tijera":
                print("Punto para usted.")
                contadorPuntos +=1

        #si elijo papel    
        if persona == "papel":
            if compu == "piedra":
                print("Punto para usted.")
                contadorPuntos +=1
            if compu == "papel":
                print("Empate.")
            if compu == "tijera":
                print("Punto para la computadora.")
                contadorPuntos -=1

        #si elijo tijera    
        if persona == "tijera":
            if compu == "piedra":
                print("Punto para la computadora.")
                contadorPuntos -=1
            if compu == "papel":
                print("Punto para usted.")
                contadorPuntos +=1
            if compu == "tijera":
                print("Empate.")

        return contadorPuntos

        #los empates se resuelven dandole ningún punto a nadie

    def Ganador(self, Puntaje):
        if Puntaje == 0:
            print("Empate.")
        if Puntaje > 0:
            print("Gana usted.")
        if Puntaje < 0:
            print("Gana la computadora.")

#-----------------------//-----------------------//-----------------------//-----------------------//-----------------------//-----------------------//

print("Hola.")

JuegoNuevo=Juego()
JuegoNuevo.comenzarJuego()