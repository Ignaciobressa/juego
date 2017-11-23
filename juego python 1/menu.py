import os
 
def menu():
	
	os.system('cls')#vacia pantalla
	print ("Selecciona una opción")
	print ("Jugador 1")
	print ("Jugador 2 ")
	print ("Jugador 3")
	print ("salir")
 
 
while True:
	# Mostramos el menu
	menu()
 
	# solicituamos una opción al usuario
	opcionMenu = input("Elije un jugador ")
 
	if opcionMenu=="1":
		print ("")
		input("Jugador 1, pulse una tecla para continuar")
	elif opcionMenu=="2":
		print ("")
		input("Jugador 2 , pulse una tecla para continuar")
	elif opcionMenu=="3":
		print ("")
		input("Jugador 3, pulse una tecla para continuar")
	elif opcionMenu=="9":
		break
	else:
		print ("")
		input("No has pulsado ninguna opción correcta...\npulsa una tecla para continuar")