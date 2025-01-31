# print("Vamos a jugar piedra, papel o tijera")


# def validate_selection(choice, valid_options):
#     if choice not in valid_options:
#         print("No seleccionaste una opción válida")
#         return False
#     return True


# game_options = ["piedra", "papel", "tijera"]


# def get_player1_choice():
#     player1_choice = input("Jugador uno: selecciona uno de los 3: ")
#     if validate_selection(player1_choice, game_options):
#         return player1_choice
#     return get_player1_choice()


# def get_player2_choice():
#     player2_choice = input("Jugador dos: selecciona uno de los 3: ")
#     if validate_selection(player2_choice, game_options):
#         return player2_choice
#     return get_player2_choice()


# try_again_options = ["si", "no"]


# def ask_to_play_again(restart):
#     try_again_choice = input("¿Quieres jugar de nuevo? si|no: ")
#     if validate_selection(try_again_choice, try_again_options):
#         if try_again_choice == "si":
#             return restart()
#         print("Gracias por jugar")
#     else:
#         return ask_to_play_again(restart)


# def determine_winner(player1_choice, player2_choice):
#     if player1_choice == player2_choice:
#         return "Empate"
#     elif (
#         (player1_choice == "tijera" and player2_choice == "papel")
#         or (player1_choice == "papel" and player2_choice == "piedra")
#         or (player1_choice == "piedra" and player2_choice == "tijera")
#     ):
#         return "Gano el jugador 1"
#     else:
#         return "Gano el jugador 2"


# def play_game():
#     player1_choice = get_player1_choice()
#     player2_choice = get_player2_choice()

#     result = determine_winner(player1_choice, player2_choice)
#     print(result)

#     ask_to_play_again(play_game)


# play_game()

import sys
import random

print("🎮 ¡Vamos a jugar piedra, papel o tijera! 🎮")

OPTIONS = ["piedra", "papel", "tijera"]
RETRY_OPTIONS = ["si", "no"]
MODE_OPTIONS = ["jugador", "cpu"]


def get_valid_input(prompt, valid_options):
    while True:
        choice = input(prompt).strip().lower()
        if choice in valid_options:
            return choice
        print("❌ Opción inválida. Inténtalo de nuevo.")


def determine_winner(player1, player2):
    winning_cases = {"piedra": "tijera", "papel": "piedra", "tijera": "papel"}

    if player1 == player2:
        return "🤝 ¡Es un empate!"
    elif winning_cases[player1] == player2:
        return "🏆 ¡Jugador 1 gana!"
    else:
        return "🏆 ¡Jugador 2 gana!"


def play_round():
    mode = get_valid_input(
        "🎭 ¿Quieres jugar contra otro jugador o contra la CPU? (jugador/cpu): ",
        MODE_OPTIONS,
    )

    player1 = get_valid_input("👤 Jugador 1, elige piedra, papel o tijera: ", OPTIONS)

    if mode == "jugador":
        player2 = get_valid_input(
            "👤 Jugador 2, elige piedra, papel o tijera: ", OPTIONS
        )
        print(f"\n🎲 Jugador 1 eligió: {player1}")
        print(f"🎲 Jugador 2 eligió: {player2}\n")
    else:
        player2 = random.choice(OPTIONS)
        print(f"\n🎲 Jugador 1 eligió: {player1}")
        print(f"🤖 La CPU eligió: {player2}\n")

    print(determine_winner(player1, player2))


def main():
    while True:
        play_round()
        retry = get_valid_input("\n¿Quieres jugar de nuevo? (si/no): ", RETRY_OPTIONS)
        if retry == "no":
            print("👋 ¡Gracias por jugar! 🎉")
            sys.exit()


# Ejecutar el juego
if __name__ == "__main__":
    main()
