contador = 1
limite = 3

nombre1 = input("Como se llamará el jugador1 ")
nombre2 = input("Como se llamará el jugador2 ")

Puntos_1 = 0
Puntos_2 = 0

while Puntos_1 != 2 and Puntos_2 != 2:
    print("Partida: ", contador)
    
    print(nombre1)
    jugador1 = input("Que eliges? Piedra, papel o tijera?: ")

    print(nombre2)
    jugador2 = input("Que eliges? Piedra, papel o tijera?: ")

    condicion1 = jugador1.lower() == "piedra" and jugador2.lower() == "tijera"
    condicion2 = jugador1.lower() == "papel" and jugador2.lower() == "piedra"
    condicion3 = jugador1.lower() == "tijera" and jugador2.lower() == "papel"

    if jugador1 == jugador2:
        print("Empate, vamos a jugar de nuevo")
    elif condicion1 or condicion2 or condicion3:
        Puntos_1 += 1
        print("Ganó: ", nombre1, "y tiene: ", Puntos_1, " puntos")
        contador += 1
        
    else:    
        Puntos_2 += 1
        print("Ganó: ", nombre2, "y tiene: ", Puntos_2, " puntos")
        contador += 1
    
    print("Puntos ", nombre1, ": ", Puntos_1)
    print("Puntos ", nombre2, ": ", Puntos_2)

    if Puntos_1 == 2:
        print("El juego terminó y el ganador es: ", nombre1)
    elif Puntos_2 == 2:
        print("El juego terminó y el ganador es: ", nombre2)
    else:
        print("Vamos a jugar la próxima partida")

        