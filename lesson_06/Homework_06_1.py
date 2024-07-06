while True:
    text = input('Input text: ')
    a = 0
    for i in set(text):
        a += 1
    print(f'Unique symbols: {a}')
    if a > 10:
        print(True)
        print('=='*20)
    else:
        print(False)
        break