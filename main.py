import os
import random

print('Bienvenid@ al juego de piedra, papel o tijeras')

print('----------------------------------------------')
nombre_jugador = str(input('¿Cómo te llamas?: ')) # Nombre del jugador
if nombre_jugador == '':
    nombre_jugador = 'Jugador' # Si no da nombre, se pone como invitado
print('----------------------------------------------')

print(f'Hola {nombre_jugador.capitalize()}, soy IA-chan. :)\n')
print(f'Instrucciones del juego:')
print("Debes insertar la cantidad de veces a jugar, con lo que después, deberás escribir entre: 'Piedra', 'Papel' "
      "ó 'Tijera' (sin las comillas), para hacer tu movimiento.")
print('Al final del juego se te mostrarán los resultados finales de la partida con la IA.')


def main(): # Función principal
    try: # Un try para captar el error en la entrada
        print('--------------------------------------------')
        turns = int(input('¿Cuántas veces quieres jugar?: '))
        print('--------------------------------------------')
    except ValueError:
        turns = None # Si no provee las veces, turnos se pone nulo

    while turns is None: # Mientras turnos sea nulo vuelve a pedir la cantidad
        try:
            print('ERROR | Debes escribir un número. No letras o símbolos.')
            turns = int(input('¿Cuántas veces quieres jugar?: '))
            print('--------------------------------------------')
        except ValueError:
            turns = None

    while turns <= 0 or turns > 10: # Mientras la cantidad sea igual o menor a 0 o mayor a 10, vuelve a pedir el valor
        print('ERROR | Especifica un numero entre el 1 al 10')
        turns = int(input('Veces a jugar: '))
        print('--------------------------------------------')

    print('--------------------------------------')
    print(f'¡Muy bien {nombre_jugador.capitalize()}, jugaremos {turns} veces!\n¡INICIEMOS!')
    print('--------------------------------------')

    user_wins = 0 # Variables para los marcadores
    ia_wins = 0
    empate = 0

    for i in range(turns): # Bucle del juego
        i += 1 # Suma la cantidad de turnos llevados

        cpu = ['Piedra', 'Papel', 'Tijera']  # Lista y elección random de la IA
        ia = random.choice(cpu)

        move = input(f'Turno {i} de {turns}\nIngresa tu movimiento: ')

        if move.capitalize() == 'Piedra' and ia == 'Tijera':
            print('------------------------------')
            print(f'Elegiste: {move.capitalize()}\nEleccion de IA-chan: {ia}\nResultado: !Ganaste! :D')
            print('------------------------------')
            user_wins += 1 # Suma un punto al jugador
        elif move.capitalize() == 'Papel' and ia == 'Piedra':
            print('------------------------------')
            print(f'Elegiste: {move.capitalize()}\nEleccion de IA-chan: {ia}\nResultado: !Ganaste! :D')
            print('------------------------------')
            user_wins += 1
        elif move.capitalize() == 'Tijera' and ia == 'Papel':
            print('------------------------------')
            print(f'Elegiste: {move.capitalize()}\nEleccion de IA-chan: {ia}\nResultado: !Ganaste! :D')
            print('------------------------------')
            user_wins += 1
        elif move.capitalize() == 'Piedra' and ia == 'Papel': # Para la IA
            print('------------------------------')
            print(f'Elegiste: {move.capitalize()}\nEleccion de IA-chan: {ia}\nResultado: !Te gané! >:D')
            print('------------------------------')
            ia_wins += 1 # Suma punto a la IA
        elif move.capitalize() == 'Papel' and ia == 'Tijera':
            print('------------------------------')
            print(f'Elegiste: {move.capitalize()}\nEleccion de IA-chan: {ia}\nResultado: !Te gané! >:D')
            print('------------------------------')
            ia_wins += 1
        elif move.capitalize() == 'Tijera' and ia == 'Piedra':
            print('------------------------------')
            print(f'Elegiste: {move.capitalize()}\nEleccion de IA-chan: {ia}\nResultado: !Te gané! >:D')
            print('------------------------------')
            ia_wins += 1
        elif move.capitalize() == ia: # Si es empate
            print('------------------------------')
            print(f'Elegiste: {move.capitalize()}\nEleccion de IA-chan: {ia}\nResultado: !Empate! OwO')
            print('------------------------------')
            empate += 1
        else: # Si escribe otra cosa
            print('------------------------------')
            print('Selección erronéa.')
            print('------------------------------')
            main()

    print('\n--------------------------------')
    print('Juego terminado - Resultados')
    print('--------------------------------\n')
    print(f'Ganadas por ti ({nombre_jugador.capitalize()}): {user_wins}')
    print(f'Ganadas por IA-chan: {ia_wins}')
    print(f'Empates: {empate}')

    if user_wins > ia_wins: # Si el marcador es mayor del jugador a la IA
        print('\n--------------------------------')
        print('RESULTADO FINAL:')
        print(f'{nombre_jugador.capitalize()} {user_wins} - {ia_wins} IA-chan')
        print('¡¡HAS GANADO, FELICIDADES!! :D')
        print('--------------------------------')
    elif user_wins == ia_wins: # Si el marcador es empate
        print('\n-----------------------------------')
        print('RESULTADO FINAL:')
        print(f'{nombre_jugador.capitalize()} {user_wins} - {ia_wins} IA-chan')
        print('¡Es un empate, bien jugado!\n¿Te parece al mejor de tres? ;)')
        print('-----------------------------------')
    else: # Si gana la IA
        print('\n-----------------------------------')
        print('RESULTADO FINAL:')
        print(f'{nombre_jugador.capitalize()} {user_wins} - {ia_wins} IA-chan')
        print('¡¡TE HE GANADO!! :DD\n¿Quieres una revancha?')
        print('-----------------------------------')

    print('------------------------------------------') # Opciones por si quiere jugar de nuevo
    opc = input('\n--> S - Para jugar de nuevo\n--> Pulsa cualquier tecla para terminar\n¿Jugamos de nuevo?: ')
    print('\n------------------------------------------')

    if opc.capitalize() == 'S': # Si escribe que si, se reinicia toda la función
        main()
    else: # Si pulsa cualquier tecla, termina el juego
        print('----------------------------------------------------')
        print(f'Gracias por jugar conmigo {nombre_jugador.capitalize()}, ¡hasta pronto! :D')
        print('Juego terminado.\nPulsa una vez más para salir.')
        print('----------------------------------------------------')
        os.system('PAUSE')


main() # Funcion main que se ejecuta al primer duelo
