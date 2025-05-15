# ceacer cicyper

# import pyperclip

#the string to be encrypted/decryped
message = 'This is my secert message.'

#the key
key = 13

# whether the program encrypts or decrypts
mode = 'encrypt' 

# everypossible symbol that can be encrypted
# python constant
SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'

#store the encrypted/decryped form of the messgae
translated = ""

for symbol in message:
    # note: only symbols in the SYMOBLS string can be encrypted/decrypted
    if symbol in SYMBOLS:
        symbolIndex = SYMBOLS.find(symbol)

        #perform encrypted/decrytpion:
        if mode == 'encrypt':
            translatedIndex = symbolIndex + key
        elif mode == 'decrypy':
            translatedIndex = symbol - key

        # handle wraparound if needed:
        if translatedIndex >= len(SYMBOLS):
            translatedIndex = translatedIndex - len(SYMBOLS)
        elif translatedIndex < 0:
            translatedIndex = translatedIndex + len(SYMBOLS)
    
        translated = translated + SYMBOLS[translatedIndex]
    else:
        #append the symboil without encrytipng/decryying
        translated = translated + symbol
        
# output the translated string
print(translated)
#pyperclip.copy(translated)