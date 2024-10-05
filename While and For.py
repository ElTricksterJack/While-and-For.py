print("\nNombre: Ruvalcaba Valverde Miguel Angel")
print("-----♞---While---♞-----")
print("Descrision: este es un bucle o Loop que esta activo hasta que la variable desiganada tenga un valor espesifico como que Varaible x tiene que ser < 0 para acabr con el bucle")
print("- ♫ Ejemplo 1 ♫ -")
i = 1
while i < 6:
  print(i)
  i += 1
print("que paso qui, simple, definimos que este bulcle solo se acabaria hasta que i balga igual que 6 \ny por eso se detubo en 5 porque como i ya balia 6 el bucle se cerro antes de escribir 6")
print("\n- ♫ Ejemplo 2 ♫ -")
i = 1
while i < 6:
  print(i)
  if i == 3:
    break #esto permite terminar un conjunto de codigo si terminar el programa.
    print("www")#Nota:No se muestra porque esta parte esta inavilitada.
  elif i > 6:
    print("www")#Nota:Por sierto priorisa el break sobre cualquier cosa.
  i += 1
print("que paso aqui, beran el break termina este codigo hasiendo \nque el if aga que cuando i sea igual a 3, sin importal que el codigo termina cuando i sea < 6")
print("\n- ♫ Ejemplo 3 ♫ -")
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  elif i > 6:
    print("www")  
  print(i)
print("qui el codigo si puede continuar, por el continue que es lo contrario de break, pero como ya se cumplio la primera \ncondison de i igual a 3 ya se cumplio, pero heso hase que la otra opcion no se puede realisar.")
#Nota:cuando estoy hasiendo esto me di cuenta que hay algien dras de mi pero mis papas y heramno estan dormidos, me esta mierando desde las escaleras y siento su mirada tengo miedo.
#Nota:era mi hermano perdon, bueno segir programando biendo underad unluck
print("\n- ♫ Ejemplo 4 ♫ -")
i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i es 6")
print("aqui si lo detecta porque es una opcion final")
#Nota: Cuando estaba haciendo esto comencé a ver Spoiled Undead Unluck, la pelea con Spoiled y me emocionó mucho la parte donde el profesor zombie muere para ayudar a destruir a Spoiled. Me duele, fue simplemente hermoso.
print("\n\n\n-----♘---For---♘-----")
print("Descripción: El bucle for en Python permite ejecutar un determinado bloque de código un número de veces que viene determinado por la clase iterable que es usada.")
print("Tradusion para simples mortales: Se repite la cantidad de veses que tenga un valor por ejemplo, si escribes que se repitas 3 veses lo hara, o con una lista, dira todos los items de una lista.")
#este si se puede husar con mas que solo numeros el otro, que es el while es un asta que.
print("- ♠ Ejemplo 1 ♠ -")
nomi = ["Goro Goro No Mi", "Suna Suna No Mi", "Yami Yami No Mi"]
for x in nomi:
  print(x)
print("Repito, dise todos los items de la variable nomi")
print("- ♠ Ejemplo 2 ♠ -")
for x in "Ope Ope No Mi":
  print(x)
print("Aqui muestodos los elementos de lap albra ya que es un string")
print("- ♠ Ejemplo 3 ♠ -")
nomi = ["Goro Goro No Mi", "Suna Suna No Mi", "Yami Yami No Mi"]
for x in nomi:
  print(x)
  if x == "Suna Suna No Mi":
    break
#  print(x) #si dejamos esto no se bera el resultado Suna Suna, y igual que con el continue pasara lo mismo
print("aqui pasa lo mismo con el while pero con for")
print("- ♠ Ejemplo 4 ♠ -")
for x in range(6):
  print(x)
print("------")
for x in range(2, 6):
  print(x)
print("------")
for x in range(2, 30, 3):
  print(x)
print("------")
print("Tambien funsiona con numeros la segunda relga")
print("- ♠ Ejemplo 5 ♠ -")
fru = ["manzana", "naranja"]
nomi = ["Goro Goro No Mi","Yami Yami No Mi"]
for x in fru:
  for y in nomi:
    print(x, y)
print("por sierto, puedes combinar los for en entre si")
