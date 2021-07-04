fichero = open('./src/texto.txt','r')  
texto = fichero.read() 
fichero.close()  
print(texto)
input()

with open('./src/texto.txt', "r") as fichero:
    for linea in fichero:
        print(linea)

fichero = open('./src/fichero2.txt','w')
texto = "Línea 1\nLínea 2\nLínea 3\nLínea 4"
fichero.write(texto)
fichero.close()
input()

fichero = open('./src/fichero2.txt','r+')
fichero.write("0123456")
input()

fichero = open('./src/fichero2.txt','r+')
texto = fichero.readlines()
input()

with open('./src/fichero_esp.txt','r') as f:
    texto = f.read()
    print(texto)
input()

with open('./src/fichero_esp.txt',encoding='utf-8') as f:
    texto = f.read()
    print(texto)
input()


