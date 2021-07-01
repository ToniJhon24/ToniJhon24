#Pregunta 1
nombre = input('Coloque su nombre:')

print ('Hola {}!' . format(nombre))

#Pregunta 2
shows = int(input('¿Cuantos shows musicales logro ver en el año? :'))
if(shows >= 3):
    print('El usuario a visto mas de 3 shows : True')
else:
    print('El usuario no a visto mas de 3 shows : False')

#Pregunta 3
a = int(input('Ingrese un numero: '))
b = int(input('Escribe otro numero:'))
suma = a + b
print('La suma  de es:',suma)

#Pregunta 4
a = int(input('Ingrese la cantidad de payasos: '))
peso= a * 112
print('El peso de {} payasos es: {} g.'.format(a,peso))

b = int(input('Ingrese la cantidad de muñecas: '))
pesom= b * 75
print('El peso de {} muñecas es: {} g.'.format(b,pesom))


#Pregunta 5
x = int(input('Porfavor ingrese un numero:' ))
suma= (x * (x+1))/2
print('La suma de los {} primeros enteros positivos es: {}'.format(x,suma))

#Pregunta 7
a = int(input('Ingrese un numero: '))
b = int(input('Escribe otro numero distinto:'))
if(a > b):
    print('El mayor es: ',a)
else:
    print('el mayor es: ' ,b)

#Pregunta 8
a = int(input('Ingrese un numero: '))
b = int(input('Escribe otro numero:'))
x = a/b 
if(x > 0.1):
    print('El valor de la división es: ',x)
else:
    print('error')

#Pregunta 9
letra = input('Ingrese una letra: ')
letra = letra.lower()
if letra == 'a':
    print('Es vocal')
if letra == 'e':
    print('Es vocal')
if letra == 'i':
    print('Es vocal') 
if letra == 'o':
    print('Es vocal')          
elif letra == 'u':
    print ('Es vocal')
else:
    print('No es vocal')

#Pregunta 10
año = int(input('Ingrese un año: '))
if año/4 == abs or año/400:
    print('El año es bisiesto:')
elif año/100:
    print('No es bisiesto')    
else:
    print('No es bisiesto') 

#Pregunta 11
edad = int(input('Ingresa tu edad: '))
if edad<=4 :
    print('Usted puede ingresar gratis')
elif 18> edad>=5 : 
    print('Usted debe pagar S/ 5.00')
elif edad>=18:
    print('Usted debe pagar S/ 10.00')
else:
    print('Vuelva a ingresar su edad ')
input()       

#Pregunta 12
palabras = ['Di', 'buen', 'día', 'a', 'papa']
for o in reversed(palabras):
    print(o)
input()      

#Pregunta 13   
palabras = ['Rojo', 'Verde', 'Blanco', 'Negro', 'Rosa', 'Amarillo']
palabras.remove('Rojo')
palabras.remove('Rosa')
palabras.remove('Amarillo')
print(palabras)
input()   

#Pregunta 14
a = [1, 1, 2]
b = [3, 4, 4, 5, 1]
c = [a,b]
print(c)
input()   

#Pregunta 15
lista =['rojo', 'verde', 'blanco', 'negro', 'naranja']
print(lista[0],lista[1],lista[3],lista[4],lista[2])

lista =['rojo', 'verde', 'blanco', 'negro', 'naranja']
print(lista[1],lista[2],lista[3],lista[4],lista[0])

lista =['rojo', 'verde', 'blanco', 'negro', 'naranja']
print(lista[0],lista[1],lista[2],lista[4],lista[3])
input()   