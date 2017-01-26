def alphabet_position(letter):
    '''
    Receives a letter and returns the 0-based numerical position of that letter
    within the alphabet. It should be case-insensitive.
    '''
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    return alphabet.index(letter.lower())


def rotate_character(char,rot):
    '''
    Receives a char and an int.
    Returns a new string of length 1, the result of rotating char by rot number
    of places to the right
    '''
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    if char.isupper():
        new_pos = (alphabet_position(char)+rot)%26
        return alphabet[new_pos].upper()
    elif char.islower():
        return alphabet[(alphabet_position(char)+rot)%26]
    else:
        return char


def encrypt(text,rot):
    result = ''
    for char in text:
        result += rotate_character(char,rot)
    return result
