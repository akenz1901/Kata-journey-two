prexies = 'JKLMNOPQ'
left_characters = 'ACK'
distinguished = 'U'

for letter in prexies:
    if letter == 'O' or letter == 'Q':
        conc = letter + distinguished
        print(conc + left_characters, end=".\n")
    else:
        print(letter + left_characters, end=".\n")
