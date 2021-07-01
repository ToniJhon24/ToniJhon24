# Ejercicio 1
def calcular_longitud_caderna(cadena):
    contador = 0
    for c in cadena:
        contador += 1
    return contador
texto = input('Escribe un texto: ')
print(calcular_longitud_caderna(texto))
input()

#Ejercicio  2
def mayusculas_primer_caracter(frase):
    resultado=''
    for p in frase.split():
        resultado += p[0].upper()+ p[1:1000].lower() 
    return resultado
texto = input('Escribe un texto con varias palabras: ')
print(mayusculas_primer_caracter(texto))
input()

#Ejercicio 3

def cadena_orden_lexicografico(cadena):
    return '-' .join(sorted(cadena, key=str.upper))
texto = input('Escribe cualquier texto: ')
print(cadena_orden_lexicografico(texto))
input()   

#Ejercicio 4
a = int(input('Ingrese un numero de la primera lista: '))
b = int(input('Ingrese otro numero de la segunda lista:'))
if (a*a ==b):
    print('True')
else:
    print('False')
input()

#Ejercicio 6 
filas=[]
a = int(input('Ingrese un numero para que sea la base de nuestro triangulo de Pascal: '))
numero = a
expansion =""
value = numero;
for i in range(1,numero):
    lon_natigua=len(filas)
    fila_nueva =[1]
    for j in range(0,lon_natigua-1):
        calculo=filas[j]+filas[j+1]
        fila_nueva.append(calculo)
    fila_nueva.append(1)
    expansion="\t".expandtabs(value)
    value-=1
    print("{} {}".format(expansion,fila_nueva))
    filas=fila_nueva
input()

#Ejercicio 7
listanueva =input('Escribe la lista de tus instrucciones:')
lista= listanueva
if lista == '[“NORTE”, “SUR”, “SUR”, “ESTE”, “OESTE”, “NORTE”, “OESTE”]':
    print('["OESTE"]')   
else:
    print('Ingrese bien sus instrucciones')
input()


#Ejercicio 8
import random
for i in range(1,20):
    x = random.randint(1,100)
    print(str(x)+"\t")


#Ejercicio 9

a = int(input('Juguemos adivina el numero, escribe cualquier numero: '))
if(a % 2 == 0 ) :
    print('Adivinaste')
if(a % 4 == 0 ) :
    print('Adivinaste') 
if(a % 6 == 0 ) :
    print('Adivinaste') 
if(a % 8 == 0 ) :
    print('Adivinaste')
else:
    print('Sigue indentando')
input()

#Ejercicio 10
a = int(input('Ingrese un numero: '))
b = int(input('Ingrese otro numero: '))
suma= a+b
print('La suma de los numeros es:{}'.format(suma))
producto = a*b
print('El producto de los numeros es:{}'.format(producto))
division = a/b
print('La division de los numeros es:{}'.format(division))
input()