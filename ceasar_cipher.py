
while True:  # Keep asking until the user enters e or d.26.
    print('Do you want to (e)ncrypt or (d)ecrypt?')
    response = input('> ').lower()
    if response.startswith('e'):
        mode = 'encrypt' 
        print(f'the mode is in: {mode}')
        break
    elif response.startswith('d'):
        mode = 'decrypt'
        print(f'the mode is in: {mode}')
        break
    print('Please enter the letter e or d.')

#2 Ask the user what key to use

SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

while True:
    max_key = len(SYMBOLS)
    print(f'Please enter the key (0 to {max_key}) to use')
    response = input('> ')
    if not response.isdecimal():
        print("not a decimal")

    key = int(response)
    break


#3. Get the input from the user of what the word to be encrypt/decrypt
print('Please enter the message')
message = input('> ')

encrypted_symbols = ""
for symbol in message:
    num = SYMBOLS.find(symbol)
    num = num + key
    encrypted_symbol = SYMBOLS[num]
    encrypted_symbols = encrypted_symbols + encrypted_symbol

print(f'{message} when encrypted with key {key} is: {encrypted_symbols}')