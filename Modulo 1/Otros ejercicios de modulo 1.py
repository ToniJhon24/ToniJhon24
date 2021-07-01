#Salundando

nombre = input('Ingrese su nombre: ')

print('Hola {}!'.format(nombre))
input()


nombre = input('Ingrese su nombre: ')
if nombre == 'Gonzalo':
    print('Bienvenido {}!'.format(nombre))
else:
    print('Tu no eres Gonzalo')
input()

#Elevar un numero al cuadrado
import sys
x = int(sys.argv[1])
potencia = x ** 3
print(f'el valor de x ({x}) elevado a la potencia de 3 es : {potencia}')
input()

x = int(input('Por favor ingrese un dato numerico: '))
potencia = x ** 3
print('El numero {} elevado al cubo es: {}'.format(x, potencia))
input()

a = int(input('Ingrese el primero numero: '))
b = int(input('ingrese el segundo numero: '))
a==b
input()


a = int(input('Ingrese el primero numero: '))
a = 85
if x == 8 :
    print('el valor de x es 8')  # 4 espacios
else:
    print('el valor de x = {} es distinto de 8'.format(x))
input()



semaforo = input('Ingrese el color de la luz del semáforo: ')
semaforo = semaforo.lower()
if semaforo == 'verde':
    print('Puede cruzar')
elif semaforo == 'amarillo' or semaforo == 'rojo':
    print ('No puede cruzar')
else:
    print('Valide ingreso de datos!')
input()