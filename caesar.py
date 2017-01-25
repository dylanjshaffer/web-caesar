import string

def alphabet_position(letter):
    letter = letter.lower()
    alphabet = string.ascii_lowercase
    ix = alphabet.find(letter)

    return ix


def rotate_character(char, rot):
    if char.isalpha():
        alphabet = string.ascii_lowercase
        ix = (alphabet_position(char) + rot) % 26
        newChar = alphabet[ix]
        if char.isupper():
            newChar = newChar.upper()
    else:
        return char

    return newChar


def encrypt(text, rot):
    newText = ''
    for char in text:
        newChar = rotate_character(char, rot)
        newText += newChar

    return newText
