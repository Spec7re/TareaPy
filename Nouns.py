from nltk import pos_tag, word_tokenize

#Abrir Archivo-----------------------------#
Flag=True
while Flag:
    try:
        direccion=raw_input("Ingrese la ruta del archivo: ")
        archivo_entrada=open(direccion,"r")
        Flag=False
    except IOError:
        print "La ruta espcificada no existe."
        Flag=True
#-------------------------------------------------------------------#

#Leer archivo----------------------------------------------------#
Texto = archivo_entrada.read()
tokens = word_tokenize(Texto)
archivo_entrada.close()
[temp.lower() for temp in tokens]
tuplas=pos_tag(tokens)#(lista de tuplas (palabra,tipo))#
#Verificar nouns#
Nouns={}
for tupla in tuplas:
    if tupla[1]=="NN":
        if tupla[0] not in Nouns:
            Nouns[tupla[0]]=(1,tupla[0])
        else:
            a,b=Nouns[tupla[0]]
            a+=1
            Nouns[tupla[0]]=(a,b)
Lista=Nouns.values()
Lista.sort()
Lista.reverse()
archivo_salida=open("Rankings.txt","w")
for elemento in Lista:
    archivo_salida.write(elemento[1]+"\n")

archivo_salida.close()
