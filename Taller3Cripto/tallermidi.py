import mido
import optparse
parse = optparse.OptionParser()


def get_arguments():
    parse.add_option("-o", "--origin", dest="origen", help="archivo midi original")
    parse.add_option("-d", "--destiny", dest="destino", help="archivo midi destino, si este valor es nulo, se sobreescribirá el archivo origen, este parámetro no es necesario si se desea hacer un decode")
    parse.add_option("-m", "--message", dest="mensaje", help="mensaje a esconder")
    parse.add_option("-a", "--action", dest="accion", help="acción que desea realizar: encode o decode")
    (options, arguments) = parse.parse_args()
    return options 

def encode(message):
    normal_string = message
    hex_string = normal_string.encode().hex()
    message_hex=[]
    for i in range(0,len(hex_string),2):
        message_hex.append("0x"+hex_string[i]+hex_string[i+1])

    hex_numbers = [int(x, 16) for x in message_hex]
    hex_numbers.insert(0,124)
    hex_numbers.insert(0,124)
    return hex_numbers

def decode(ascii_val):
    characters = [chr(letter) for letter in ascii_val]
    result_string = ''.join(characters)
    return result_string



opciones = get_arguments()
if opciones.accion.lower()=="encode":
    midi = mido.MidiFile(opciones.origen, clip=True)

    
    track = midi.tracks[0]
    new_message=[]
    new_message.append(mido.Message('sysex', data=encode(opciones.mensaje)))
    track.extend(new_message)
    if opciones.destino is not None:
        midi.save(opciones.destino)
    else:
        midi.save(opciones.origen)
elif opciones.accion.lower()=="decode":
    midi = mido.MidiFile(opciones.origen, clip=True)
    track = midi.tracks[0]
    index=0
    for msg in track:
        if msg.type=="sysex":
            lista=list(msg.data)
            if lista[0]==124 and lista[1]==124:
                lista=lista[2:]
                mensaje=decode(lista)
                print(mensaje)
                del track[index]
                midi.save(opciones.origen)
        index+=1
else:
    print("invalid action")