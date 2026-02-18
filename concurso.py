 # crear una lista de 200 notas

#En py debo usar librerias para facilitar mi trabajo
import random
numeroAleatorio = random.randint(1,5)
print(f"El numero aleatorio es: {numeroAleatorio}")

notas = []
for i in range(5):
    nota=random.randint(1,5)
    print(nota)
    # como agregar un elemento a una lista
    notas.append(nota)


#Probando los metodos de las listas(listMethods)
#notas.insert(0,45)
#notas.remove(2)
#notas.pop(0)
#print(notas)

#notas.sort(reverse=True)
#print(notas)
#valor = notas.index(45)
notas.clear()
print(notas)

