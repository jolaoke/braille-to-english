import os

# Braille to English dictionary
conv = {
'100000': 'A',
'101000': 'B',
'110000': 'C ',
'110100': 'D',
'100100': 'E',
'111000': 'F',
'111100': 'G',
'101100': 'H',
'011000': 'I',
'011100': 'J',
'100010': 'K',
'101010': 'L',
'110010': 'M',
'110110': 'N',
'100110': 'O',
'111010': 'P',
'111110': 'Q',
'101110': 'R',
'011010': 'S',
'011110': 'T',
'100011': 'U',
'101011': 'V',
'011101': 'W',
'110011': 'X',
'110111': 'Y',
'100111': 'Z',
'001011': '?',
'001110': '!',
'000010': '"',
'001000': ',',
'000011': '-',
'001101': '.',
'010111': '#',
'': ' '
}

numConv = {
'100000': '1',
'101000': '2',
'110000': '3',
'110100': '4',
'100100': '5',
'111000': '6',
'111100': '7',
'101100': '8',
'011000': '9',
'011100': '0',
'010111': '#',
'': ' '
}

phrase = ''

# Enter Braille data
run = True
while run:
    # if row1 is 'end', end the process and translate the phrase
    row1 = input('Row 1:')
    if row1 == 'end':
        print('')
        run = False
        break
    # if row1 is an empty string, this is a space
    if row1 == '' or row1 == ' ':
        row2 = ''
        row3 = ''
    else:
        row2 = input('Row 2:')
        row3 = input('Row 3:')
    print('')
    cell = row1 + row2 + row3
    phrase = phrase + cell + ' '
# print(phrase)

# Convert Braille to English
phraseCharacters = phrase.split(' ')
translatedPhrase = ['']
num = False
for character in phraseCharacters:
    if conv[character] == '#':
        num = True
        for character in phraseCharacters[phraseCharacters.index(character):]:
            if numConv[character] != ' ' and num == True:
                translatedPhrase.append(numConv[character])
            else:
                translatedPhrase.append(' ')
                num = False
            if num == False:
                break
                
                
                
    else:
        if num == False:
            translatedPhrase.append(conv[character])

# Say translation out loud
if '#' in translatedPhrase:
    translatedPhrase.remove('#')
translation = ''.join(translatedPhrase)
print(translation)
os.system('say %s' %(translation))

