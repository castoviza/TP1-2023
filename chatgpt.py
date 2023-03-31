# Lista de palabras
palabras = ["delfin"]



# Crear variables
intentos = 6
letras_adivinadas = []

# Mostrar mensaje de bienvenida
print("¡Bienvenido al juego del ahorcado!")

# Bucle del juego
while intentos > 0:
    # Mostrar la palabra con las letras adivinadas
    resultado = ""
    for letra in palabras:
        if letra in letras_adivinadas:
            resultado += letra
        else:
            resultado += "_"
    print(resultado)

    # Pedir al jugador que adivine una letra
    letra = input("Adivina una letra: ").lower()

    # Comprobar si la letra ya fue adivinada
    if letra in letras_adivinadas:
        print("Ya adivinaste esa letra. Intenta con otra.")
    else:
        # Agregar letra adivinada a la lista
        letras_adivinadas.append(letra)

        # Comprobar si la letra está en la palabra
        if letra in palabras:
            print("¡Muy bien! Adivinaste una letra.")
        else:
            print("Oops, esa letra no está en la palabra.")
            intentos -= 1

    # Mostrar número de intentos restantes
    print(f"Te quedan {intentos} intentos.")

    # Comprobar si el jugador adivinó la palabra completa
    if resultado == palabras:
        print("¡Felicidades! Adivinaste la palabra.")
        break

# Mostrar la palabra completa si el jugador no adivinó
if resultado != palabras:
    print(f"Lo siento, la palabra era {palabras}. Mejor suerte la próxima vez.")