letter = input('Choose letter: ')
letter = list(letter)
while True:
    text1 = input(f'Input text with {letter[0]}: ')

    for i in set(text1.lower()):
        if i == letter[0].lower():
            True
            #print(f'Contains {letter}')  # Якщо потрібна індикація існування літери в тексті
        else:
            continue