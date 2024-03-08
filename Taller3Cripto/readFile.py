import math
def read_file(nombre):
    
    with open(nombre, 'r',encoding='utf-8') as file:
        file_content = file.read()
    return file_content
def encode(message):
    ascii_values=[]
    for char in message:
        ascii_val=ord(char)
        if ascii_val > 127:
            ascii_val=ascii_val-127
            ascii_values.append(19)
            ascii_values.append(ascii_val)
        else:
            ascii_values.append(ascii_val)
    ascii_values.insert(0,124)
    ascii_values.insert(0,124)
    
    return ascii_values

def dividir_lista(lista_inicial):
    divisiones_num=int(len(lista_inicial)/1000000)+1
    tamanio=int(len(lista_inicial)/divisiones_num)+1
    return [lista_inicial[i:i + tamanio] for i in range(0, len(lista_inicial), tamanio)]


lista=encode(read_file("elQuijote.txt"))

listas=dividir_lista(lista)
for i in listas:
    print(len(i))