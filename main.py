
"""
Ejercicio1: Definir un programa que decida quién es el ganador en un juego de Piedra, Papel o Tijera. El programa pide primero ingresar la jugada del primer jugador y luego del segundo. Las respuestas pueden ser únicamente PIEDRA, PAPEL o TIJERA. Las preguntas son: 
-¿Cuál es la jugada del primer jugador?
-¿Cuál es la jugada del segundo jugador?
Las respuestas pueden ser:
-Ganó el primer jugador
-Ganó el segundo jugador
-Hubo empate

jugador1= input ("Jugador 1 ingrese su jugada ")
jugador2= input ("Jugador 2 ingrese su jugada ")

if jugador1 == jugador2:
  print ("Hubo empate")
elif jugador1 == "Piedra" and jugador2 == "Papel":
  print ("Ganó el jugador 2")
elif jugador1 == "Tijera" and jugador2 == "Piedra":
  print ("Ganó el jugador 2")
else: 
  print ("Ganó el jugador 1")

#Ejercicio 2
Definir un programa que reciba 5 números enteros y luego muestre cuál de los valores ingresados fue el mayor. Resuélvalo utilizando estructuras iterativas y estructuras condicionales.

max= 0
for i in range (5):
  número= int(input ("Ingrese un número entero"))
  if número > max:
    max = número

print ("El número mayor es ", max)
  
#Ejercicio 3

Definir un programa que reciba números enteros y luego muestre cuál es la suma de los números pares. Se siguen solicitando nuevos números hasta que se ingrese un “no”. Resuélvalo utilizando en forma conjunta estructuras iterativas y estructuras condicionales.

sumapar= 0
pregunta = "si"
while pregunta != "no":
  número= int (input( "Ingresa un número entero"))
  if número%2==0:
    sumapar= sumapar + número
  pregunta = input ("Querés ingresar otro número?")
  #pregunta2 = input ("Querés ingresar otro número?")
print ( "La suma de los números pares es ", sumapar)


Ejercicio 4 : Crear un programa que permita a un usuario adivinar un número secreto entre 1 y 100. El programa debe solicitar al jugador 1 que ingrese un número secreto y luego el jugador 2 ingresa números hasta acertar el número secreto. Finalmente el programa informa cuantos intentos fueron necesarios. Si el jugador 2 adivina el número, el programa debe mostrar un mensaje de felicitaciones; de lo contrario, debe mostrar un mensaje indicando si el número ingresado es mayor o menor que el número secreto y solicitar al usuario que intente adivinar nuevamente. Ejemplo de datos ingresados:
(Jugador1:Ingreseunnúmero) 50 
(Jugador2:Ingreseunnúmero) 1 
(Elnúmerosecretoesmásgrande.Intentenuevamente)
(Jugador2:Ingreseunnúmero)60
(Elnúmerosecretoesmáschico.Intentenuevamente)
(Jugador2:Ingreseunnúmero)50
(Acertóalnúmerosecreto)
(Uso3intentosparaadivinar)
Notarqueentreparéntesisaparecelapreguntaqueselemuestraal/alausuario/ayenmayúsculaseslarespuestadel/delausuario/a


contador=0
pregunta1= int (input("Jugador 1: Ingrese un número entre el 1 y el 100"))
pregunta2= "no"

while pregunta1 != pregunta2:
  pregunta2= int (input ("Jugador 2: Ingrese un número"))
  contador= contador + 1
  if pregunta2 > pregunta1:
    print ("El número secreto es más chico. Intente nuevamente")
  elif pregunta1 > pregunta2:
    print ("El número secreto es más grande. Intentelo nuevamnete")
  else :
    print ("Acertó al número secreto. Uso ", contador, "intentos para adivinar")
  



Ejercicio 5: Crear una implementación del juego el ahorcado que sea lo más completo posible.


# Lista de palabras
palabras = "delfin"



# Crear variables
intentos = 6
letras_adivinadas = ""

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



Ejercicio 6:
Escribe un programa que te permita jugar a una versión simplificada del juego Código Oculto. El juego consiste en
adivinar una cadena de 4 números distintos. El usuario debe ingresar números hasta adivinar la cadena de números
y tiene 8 intentos para adivinar. En cada intento, el programa informará de cuántos números han sido acertados (es
decir, acertar en número si coincide el valor y la posición).

    """
contador_intentos = 0
codigo_secreto = []
input_codigo = input("Ingrese el codigo secreto: ")

for i in range(len(input_codigo)):
  codigo_secreto.append(input_codigo[i])

while(contador_intentos<8):
  contador_acierto = 0
  lista_de_adivinar = []
  input_adivinar = input("Ingrese el núm. con el que quiere adivinar el codigo secreto: ")
  for i in range(len(input_adivinar)):
    lista_de_adivinar.append(input_adivinar[i])
  for i in range(len(codigo_secreto)):
    if (codigo_secreto[i] == lista_de_adivinar[i]):
      contador_acierto = contador_acierto + 1
  if (contador_acierto == 4):
    print("Felicitaciones gano!")
    break
  print("Usted tuvo ", contador_acierto, " aciertos")
  print("Le quedan ", 7-contador_intentos, " intentos")
  contador_intentos = contador_intentos + 1

if (contador_acierto != 4):
  print("Que mal no gano!")

