import random

def jugar():
    usuario = input("Escoge una opción Piedra (P) | Papel (H) | Tijera (T):\n").lower()
    ia = random.choice(["p", "h", "t"])

    if usuario == ia:
        return "Empate!"
    
    if gana_usuario(usuario, ia):
        return "Ganaste!"
    
    return "Perdiste!"


def gana_usuario(jugador, oponente):
    if ((jugador == "p" and oponente == "t") or (jugador == "t" and oponente == "h") or (jugador == "h" and oponente == "p")):
        return True
    else:
        return False
    

print(jugar())