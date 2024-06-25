alice_in_wonderland = '"Would you tell me, please, which way I ought to go from here?"\n"That depends a good deal on where you want to get to" said the Cat.\n"I don\'t much care where" —— said Alice.\n"Then it doesn\'t matter which way you go" said the Cat.\n"—— so long as I get somewhere" Alice added as an explanation.\n"Oh, you\'re sure to do that" said the Cat, "if you only walk long enough."'
# task 01 == Розділіть змінну alice_in_wonderland так, щоб вона займала декілька фізичних лінії
# task 02 == Знайдіть та екрануйте всі символи одинарної дужки у тексті
# task 03 == Виведіть змінну alice_in_wonderland на друк
print(alice_in_wonderland)

"""
    # Задачі 04 -10:
    # Переведіть задачі з книги "Математика, 5 клас"
    # на мову пітон і виведіть відповідь, так, щоб було
    # зрозуміло дитині, що навчається в п'ятому класі
"""
# task 04
"""
Площа Чорного моря становить 436 402 км2, а площа Азовського
моря становить 37 800 км2. Яку площу займають Чорне та Азов-
ське моря разом?
"""
print('task 04')
S1 = 436_402
S2 = 37_800
print(f'Загальна полща = {S1+S2} км2')


# task 05
"""
Мережа супермаркетів має 3 склади, де всього розміщено
375 291 товар. На першому та другому складах перебуває
250 449 товарів. На другому та третьому – 222 950 товарів.
Знайдіть кількість товарів, що розміщені на кожному складі.
"""
print('task 05')
sklad1_plus_sklad2 = 250_449
sklad2_plus_sklad3 = 222_950
summa = 375_291
sklad_2 =sklad1_plus_sklad2 + sklad2_plus_sklad3 - summa
sklad_1 = 250_449 - sklad_2
sklad_3 = 222_950 - sklad_2

"""solution check"""
# print(summa == (sklad_3 + sklad_1 + sklad_2))

print(f'склад 1 = {sklad_1} товарів, склад 2 = {sklad_2} товарів, склад 3 = {sklad_3} товарів ')


# task 06
"""
Михайло разом з батьками вирішили купити комп’ютер, ско-
риставшись послугою «Оплата частинами». Відомо, що сплачу-
вати необхідно буде півтора року по 1179 грн/місяць. Обчисліть
вартість комп’ютера.
"""
print('task 06')
sum1 = 1179
month = 18
PC_price = sum1 * month
print('Вартість компьютера',PC_price,'грн.')

# task 07
"""
Знайди остачу від діленя чисел:
a) 8019 : 8     d) 7248 : 6
b) 9907 : 9     e) 7128 : 5
c) 2789 : 5     f) 19224 : 9
"""
print('task 07')
mas1 = [8019, 9907, 2789, 7248, 7128, 19224]
mas2 = [   8,    9,    5,    6,    5,     9]
for i in range(6):
    print(f'Oстачa від діленя {mas1[i]}:{mas2[i]} = {mas1[i] % mas2[i]}')


# task 08
"""
Іринка, готуючись до свого дня народження, склала список того,
що їй потрібно замовити. Обчисліть, скільки грошей знадобиться
для даного її замовлення.
Назва товару    Кількість   Ціна
Піца велика     4           274 грн
Піца середня    2           218 грн
Сік             4           35 грн
Торт            1           350 грн
Вода            3           21 грн
"""
print('task 08')
position_1 = {'name' : 'Піца велика', 'count': 4, 'price': 274}
position_2 = {'name' : 'Піца середня', 'count': 2, 'price': 218}
position_3 = {'name' : 'Сік', 'count': 4, 'price': 35}
position_4 = {'name' : 'Торт', 'count': 1, 'price': 350}
position_5 = {'name' : 'Вода', 'count': 3, 'price': 21}

result = position_1['count'] * position_1['price']
result = result + position_2['count'] * position_2['price']
result = result + position_3['count'] * position_3['price']
result = result + position_4['count'] * position_4['price']
result = result + position_5['count'] * position_5['price']

print(f'{result} грн.')

# task 09
"""
Ігор займається фотографією. Він вирішив зібрати всі свої 232
фотографії та вклеїти в альбом. На одній сторінці може бути
розміщено щонайбільше 8 фото. Скільки сторінок знадобиться
Ігорю, щоб вклеїти всі фото?
"""
print('task 09')
photo = 232
photo_per_list = 8
if photo % photo_per_list == 0 :
    print(f'{photo // photo_per_list} сторінок')
else:
    print(f'{(photo // photo_per_list) + 1} сторінок')


# task 10
"""
Родина зібралася в автомобільну подорож із Харкова в Буда-
пешт. Відстань між цими містами становить 1600 км. Відомо,
що на кожні 100 км необхідно 9 літрів бензину. Місткість баку
становить 48 літрів.
1) Скільки літрів бензину знадобиться для такої подорожі?
2) Скільки щонайменше разів родині необхідно заїхати на зап-
равку під час цієї подорожі, кожного разу заправляючи пов-
ний бак?
"""
print('task10')
dist = 1600 # Відстань між містами
v_tank = 48 # Місткість баку
consumption = 9 # на кожні 100 км необхідно 9 літрів бензину
v_total = (1600 / 100) * 9
print('Скільки літрів бензину знадобиться для такої подорожі?\n', int(v_total), 'літрів')
print(f'Кількість заїздов на заправку - {int(v_total / v_tank)}')

