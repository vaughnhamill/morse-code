MORSE_CODE_DICT = {'A':'.-', 'B':'-...', 'C':'-.-.', 'D':'-..', 'E':'.', 'F':'..-.', 'G':'--.', 'H':'....', 'I':'..',
                   'J':'.---', 'K':'-.-', 'L':'.-..', 'M':'--', 'N':'-.', 'O':'---', 'P':'.--.', 'Q':'--.-', 'R':'.-.',
                   'S':'...', 'T':'-', 'U':'..-', 'V':'...-', 'W':'.--', 'X':'-..-', 'Y':'-.--', 'Z':'--..', '1':'.----',
                   '2':'..---', '3':'...--', '4':'....-', '5':'.....', '6':'-....', '7':'--...', '8':'---..', '9':'----.',
                   '0':'-----', ',':'--..--', '.':'.-.-.-', '?':'..--..', '/':'-..-.', '-':'-....-', '(':'-.--.',
                   ')':'-.--.-'}

user_text = input('Type a word or sentence to convert to Morse code: ')
char_list = [char.upper() for char in user_text]

morse_code = []

for char in char_list:
    for morse in MORSE_CODE_DICT:
        if char == morse:
            morse_code.append(MORSE_CODE_DICT.get(morse))
        if char == '':
            morse_code.append('')

morse_str = ' '.join(morse_code)

print(f'Your Morse code message: {morse_str}')
