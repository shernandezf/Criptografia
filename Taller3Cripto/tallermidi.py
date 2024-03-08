#Taller midi hecho por Santiago Hernández Facio Lince 201922432
import mido
import optparse
parse = optparse.OptionParser()


def get_arguments():
    parse.add_option("-o", "--origin", dest="origen", help="archivo midi original")
    parse.add_option("-d", "--destiny", dest="destino", help="archivo midi destino, si este valor es nulo, se sobreescribirá el archivo origen, este parámetro no es necesario si se desea hacer un decode")
    parse.add_option("-m", "--message", dest="mensaje", help="mensaje a esconder")
    parse.add_option("-f", "--file", dest="archivo", help="Si se desea escnonder el contenido de un archivo, se debe omitir el uso del flag -m y hacer uso de la flag -f con el nombre del archivo, debe ser txt.")
    parse.add_option("-a", "--action", dest="accion", help="acción que desea realizar: encode o decode")
    (options, arguments) = parse.parse_args()
    return options 

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
    return ascii_values

def decode(ascii_values):
    especial=False
    characters=[]
    for letter in ascii_values:
        if especial:
            letter=127+letter
            especial=False
        if letter == 19:
            especial=True
        else:
            characters.append(chr(letter))
    result_string = ''.join(characters)
    return result_string    

def read_file(nombre):
    
    with open(nombre, 'r',encoding='utf-8') as file:
        file_content = file.read()
    
    return file_content

def dividir_lista(lista_inicial):
    divisiones_num=int(len(lista_inicial)/1000000)+1
    tamanio=int(len(lista_inicial)/divisiones_num)+1
    return [lista_inicial[i:i + tamanio] for i in range(0, len(lista_inicial), tamanio)]

opciones = get_arguments()
if opciones.accion.lower()=="encode":
    midi = mido.MidiFile(opciones.origen, clip=True)

    
    track = midi.tracks[0]
    new_message=[]
    if opciones.mensaje is not None:
        lista=encode(opciones.mensaje)
        if len(lista)<1000000:
            lista.insert(0,124)
            lista.insert(0,124)
            new_message.append(mido.Message('sysex', data=lista))
        else:
            listas=dividir_lista(lista)
            for i in listas:
                i.insert(0,124)
                i.insert(0,124)
                new_message.append(mido.Message('sysex', data=i))
    else:
        lista=encode(read_file(opciones.archivo))
        if len(lista)<1000000:
            lista.insert(0,124)
            lista.insert(0,124)
            new_message.append(mido.Message('sysex', data=lista))
        else:
            listas=dividir_lista(lista)
            for i in listas:
                i.insert(0,124)
                i.insert(0,124)
                new_message.append(mido.Message('sysex', data=i))


    track.extend(new_message)
    if opciones.destino is not None:
        midi.save(opciones.destino)
    else:
        midi.save(opciones.origen)
elif opciones.accion.lower()=="decode":
    midi = mido.MidiFile(opciones.origen, clip=True)
    track = midi.tracks[0]
    index_list=[]
    index=0
    mensaje = ""
    for msg in track:
        if msg.type=="sysex":
            lista=list(msg.data)
            if lista[0]==124 and lista[1]==124:
                lista=lista[2:]
                mensaje +=decode(lista)
                index_list.append(index)
                
        index+=1
    for index in reversed(index_list):
        track.pop(index)
    midi.save(opciones.origen)
    print(mensaje)
else:
    print("invalid action")