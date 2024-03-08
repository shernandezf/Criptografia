def string_to_ascii(input_string):
    ascii_values=[]
    for char in input_string:
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
    print(characters)
    result_string = ''.join(characters)
    return result_string    


# Example usage:
input_string = "áéíóúÁÉÍÓÚñÑASDFASDASDF"
result = string_to_ascii(input_string)
print(result)


result_decode = decode(result)
print(result_decode)