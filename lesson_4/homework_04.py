adwentures_of_tom_sawer = """\
Tom gave up the brush with reluctance in his .... face but alacrity
in his heart. And while
the late steamer
"Big Missouri" worked ....
and sweated
in the sun,
the retired artist sat on a barrel in the .... shade close by, dangled his legs,
munched his apple, and planned the slaughter of more innocents.
There was no lack of material;
boys happened along every little while;
they came to jeer, but .... remained to whitewash. ....
By the time Ben was fagged out, Tom had traded the next chance to Billy Fisher for
a kite, in good repair;
and when he played
out, Johnny Miller bought
in for a dead rat and a string to swing it with—and so on, and so on,
hour after hour. And when the middle of the afternoon came, from being a
poor poverty, stricken boy in the .... morning, Tom was literally
rolling in wealth."""

#  ПЕРЕЗАПИСУЙТЕ зміст змінної adwentures_of_tom_sawer у завданнях 1-3
# task 01 ==
""" Дані у строці adwentures_of_tom_sawer розбиті випадковим чином, через помилку.
треба замінити кінець абзацу на пробіл .replace("\n", " ")"""
print('task_01')
adwentures_of_tom_sawer = adwentures_of_tom_sawer.replace('\n', ' ')
print(adwentures_of_tom_sawer)
print('==================================')
# task 02 ==
""" Замініть .... на пробіл
"""
print('task_02')
adwentures_of_tom_sawer = adwentures_of_tom_sawer.replace('....', ' ')
print(adwentures_of_tom_sawer)
print('==================================')

# task 03 ==
""" Зробіть так, щоб у тексті було не більше одного пробілу між словами.
"""
print('task_03')
adwentures_of_tom_sawer_list = adwentures_of_tom_sawer.split()
adwentures_of_tom_sawer = ' '.join(adwentures_of_tom_sawer_list)
print(adwentures_of_tom_sawer)
print('==================================')
# task 04
""" Виведіть, скількі разів у тексті зустрічається літера "h"
"""
print('task_04')
print(adwentures_of_tom_sawer.count('h') + adwentures_of_tom_sawer.count('H'))
print('==================================')
# task 05
""" Виведіть, скільки слів у тексті починається з Великої літери?
"""
print('task_05')
a = 0
for i in adwentures_of_tom_sawer_list:
    if i.istitle():
        a += 1
print(f'Кількість великих літер - {a}')
print('==================================')
# task 06
""" Виведіть позицію, на якій слово Tom зустрічається вдруге
"""
print('task_06')
second_Tom = adwentures_of_tom_sawer.find('Tom') + 1  # пошук першого Tom
print(adwentures_of_tom_sawer.find('Tom', second_Tom))
print('==================================')

# task 07
""" Розділіть змінну adwentures_of_tom_sawer по кінцю речення.
Збережіть результат у змінній adwentures_of_tom_sawer_sentences
"""
print('task_07')
adwentures_of_tom_sawer_sentences = adwentures_of_tom_sawer.split('. ')
# Питання. Якщо поставити розділення по '.', зїявляється зайвий єлемент.
# Якщо не ставити, то в останньому буде крапка
print(adwentures_of_tom_sawer_sentences)
print('===================================')
# task 08
""" Виведіть четверте речення з adwentures_of_tom_sawer_sentences.
Перетворіть рядок у нижній регістр.
"""
print('task_08')
print(adwentures_of_tom_sawer_sentences[3].lower())
print('==================================')
# task 09
""" Перевірте чи починається якесь речення з "By the time".
"""
print('task_09')
for i in adwentures_of_tom_sawer_sentences:
    if i.startswith('By the time'):
        print(i)
print('==================================')

# task 10
""" Виведіть кількість слів останнього речення з adwentures_of_tom_sawer_sentences.
"""
print('task_10')
last_sentence = adwentures_of_tom_sawer_sentences[4]
print(f'Kількість слів останнього речення - {last_sentence.count(" ") + 1}')
