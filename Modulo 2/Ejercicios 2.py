#Pregunta 1
numeros = int(input('Ingrese un numero entre 1500 - 2700: '))
if(numeros % 7 == 0 and numeros% 5 ==0 ) :
    print('El numero {} es divisible por 7 y es multiplo de 5'.format(numeros))
else:
    print('El numero no es divisible por 7 ni multiplo de 5')
input()

def numeros_divisibles_multiplos(limite_inferiror, limite_superior):
    if limite_superior >  limite_inferiror:
        resultado = []
        for n in range (limite_inferiror, limite_superior+1):
            if n %7 ==0 and n %5 ==0:
                resultado.append(n)
        return resultado  
    raise ValueError('El limite inferior debe ser menor al superior')  

numeros=numeros_divisibles_multiplos(1500, 2700)
print(numeros)           
input()


#Pregunta 2 
altura = int(input('Ingrese un numero para que sea la base del triangulo:'))
print(altura)
for i in range(1,altura+1):
    print('#'*i)

#Pregunta 3

numeros = int(input('Ingrese un numero del 1 - 10: '))
if(numeros%2 == 0 ) :
    print('El numero es par')
else:
    print('El numero no es par')

input()   

def contar_pares_impares(lista):
    pares, impares =0,0
    for n in lista:
        if n % 2 == 0:
            pares+= 1
        else:
            impares +=1
    return pares,impares   

numeros =[1, 2, 3, 4, 5, 6, 7, 8, 9]   
resultado = contar_pares_impares(numeros)
print ('La cantidad de pares es: %i' % resultado [0])           
print ('La cantidad de impares es: %i' % resultado [1]) 
input()  

#Pregunta 4
lista_mixta = [1452, 11.23, 1 + 2j, True, 'Python', (0, -1), [5, 12], {"Clase": 'V', "Seccion": 'A'} ]
for i in range(len(lista_mixta)):
    print('Valor: {} - Tipo de dato: {} '.format(lista_mixta[i], type(lista_mixta[i])))
input() 

#Pregunta 5
def fib(n):
    a=0
    b=1
    for k in range(n):
        c=a+b
        a=b
        b=c
    return b 
for x in range (50):
    print(fib(x))      


numeros = int(input('Ingrese un numero cualquiera: '))
def fib(numeros):
    a=0
    b=1
    for k in range(numeros):
        c=a+b
        a=b
        b=c
    return b 
for x in range (numeros):
    print(fib(x)) 



#Pregunta 6
def leer_frase():
    global Text
    Text=(input('Ingrese un Texto:'))
def contar_letras():
    conta=0
    for i in Text:
        if(i.isalpha()):
            conta+=1
    print('La cantidad de letras es: ',conta)
leer_frase()   
contar_letras()

def contar_digitos_letras(cadena):
    digitos =0
    letras=0
    for c in cadena:
        if c.isdigit():
            digitos+=1
        elif c.isalpha():
            letras+=1
        else:
            pass    
    return digitos, letras
        
texto = input('Escribe un texto con digitos: ')
resultado = contar_digitos_letras(texto)
print ('La cantidad de digitos es: %i' % resultado [0])           
print ('La cantidad de letras es: %i' % resultado [1]) 
input() 

#Pregunta 7
def multiplicar(numeros):
    producto = 1
    for n in numeros:
        producto *= n
    return producto
lista_numeros =   [8, 2, 3, -1, 7]
print(type(lista_numeros))
print(multiplicar(lista_numeros))
input()

#Problema 8
Sucadena = input('Escribe un texto:')
cadena = Sucadena
for i in range(len(cadena) -1,-1,-1):
    print(cadena[i])
input()

cadena = "1234abcd"
for i in range(len(cadena) -1,-1,-1):
    print(cadena[i])
input()

#Pregunta 9
listanueva =input('Escribe una lista de texto:')
lista= listanueva
conjunto = set(lista)
lista = list(conjunto)
print(lista)
input()


#Pregunta 10
numeros = int(input('Ingrese un numero cualquiera: '))
if numeros > 1:
    cont=0
    i=2
    while i<numeros and  cont==0:
        resto=numeros%i
        if resto==0:
            cont+=1
        i+=1
    if cont==0:
        print('El {} es un numero primo'.format(numeros))
    else:  
        print('El {} no es un numero primo'.format(numeros))         
else:
    print('El {} no es primo'.format(numeros))  
input()     

#Pregunta 11
def pares(numeros):
    numeros_pares = []
    for n in numeros:
        if n %2 ==0:
            numeros_pares.append(n)
    return numeros_pares  
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]
resultado = pares (numeros)
print(numeros)
print (resultado)
input()       


#Pregunta 12
numeros = int(input('Ingrese un numero: '))
def factorial (numeros):
    if (numeros==0):
        return 1
    else:
        return numeros * factorial(numeros-1)       
print ('El factorial de: {}  es {} ' .format(numeros,factorial(numeros)))  
input()