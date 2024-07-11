# task 1
""" Задача - надрукувати табличку множення на задане число, але
лише до максимального значення для добутку - 25.
Код майже готовий, треба знайти помилки та випраавити доповнити.
"""
print('Task_1')

def multiplication_table(number: int):
    # Initialize the appropriate variable
    multiplier = 1

    # Complete the while loop condition.
    while True:
        result = number * multiplier
        # десь тут помила, а може не одна
        if result > 25:
            break
        print(str(number) + "x" + str(multiplier) + "=" + str(result))

        # Increment the appropriate variable
        multiplier += 1


multiplication_table(2)
# Should print:
# 3x1=3
# 3x2=6
# 3x3=9
# 3x4=12
# 3x5=15
print('==' * 20)
# task 2
"""  Написати функцію, яка обчислює суму двох чисел.
"""
print('Task_2')
a = int(input('A= '))
b = int(input('B= '))
print('==Case with def==')


def count_of_two(a: int, b: int):
    return a + b


print(f'{a} + {b} = {count_of_two(a, b)}')
print('==Case with lambda==')
add_1 = lambda x, y: x + y
print(f'{a} + {b} = {add_1(a, b)}')
# task 3
"""  Написати функцію, яка розрахує середнє арифметичне списку чисел.
"""

print('==' * 20)
print('Task_3')

def new_list():
    '''
    Function for creating new list
    :return:
    '''
    newlist = []
    a = int(input('Count of elements of list:'))
    for i in range(a):
        newlist.append(input(f'Element {i + 1}: '))
    return newlist


list_1 = new_list()


def sred_aref(list_a, count_of_elements=0, sum_of_elements=0):
    for i in list_a:
        if i.isdigit():
            count_of_elements += 1
            sum_of_elements += int(i)
        else:
            pass
    if count_of_elements == 0:
        return 0
    return sum_of_elements / count_of_elements


print(f'середнє арифметичне списку = {sred_aref(list_1)}')

# task 4
"""  Написати функцію, яка приймає рядок та повертає його у зворотному порядку.
"""

print('==' * 20)
print('Task_4')
print('==Case with def==')


def reverse_stringa(stringa):
    return stringa[::-1]


print(reverse_stringa(input('Enter row to reverse:\n')))
print('==Case with lambda==')
stringa_1 = input('Enter row to reverse:\n ')
stringa = lambda x: x[::-1]
print(stringa(stringa_1))

# task 5
"""  Написати функцію, яка приймає список слів та повертає найдовше слово у списку.
"""
print('==' * 20)
print('Task_5')
print('==Case with def==')
list_2 = new_list()


def max_len_in_list(list_b):
    max_len_word = list_b[0]
    for i in list_b:
        if len(i) > len(max_len_word):
            max_len_word = i
    return max_len_word

print(f' Longest word is ~ {max_len_in_list(list_2)}')

# task 6
"""  Написати функцію, яка приймає два рядки та повертає індекс першого входження другого рядка
у перший рядок, якщо другий рядок є підрядком першого рядка, та -1, якщо другий рядок
не є підрядком першого рядка."""

print('==' * 20)
print('Task_6')
print('==Case with def==')
def find_substring(str1, str2):
    index = str1.find(str2)
    if index:
        return index
    return -1

str1 = "Hello, world!"
str2 = "world"
print(find_substring(str1, str2))  # поверне 7

str1 = "The quick brown fox jumps over the lazy dog"
str2 = "cat"
print(find_substring(str1, str2))  # поверне -1

print('==Case with lambda==')
index_1 = lambda str1, str2: str1.find(str2)

str1 = "Hello, world!"
str2 = "world"
print(index_1(str1, str2))

str1 = "The quick brown fox jumps over the lazy dog"
str2 = "cat"
print(index_1(str1, str2))  # поверне -1


# task 7
print('==' * 20)
print('Task_7')
def page_counter(photo: int, photo_per_list: int):
    '''
    calculate page for album (lesson 3 task 9)
    :param photo: count of users photo
    :param photo_per_list: count of photo on page
    :return: 
    '''
    pages = photo // photo_per_list
    if photo % photo_per_list == 0:
        return pages
    return (pages + 1)

a7 = int(input('Count of photo: '))
b7 = int(input('Photo on page: '))
print(f'Count of page {page_counter(a7, b7)}')

# task 8
print('==' * 20)
print('Task_8')
people_records = [
  ('John', 'Doe', 28, 'Engineer', 'New York'),
  ('Alice', 'Smith', 35, 'Teacher', 'Los Angeles'),
  ('Bob', 'Johnson', 45, 'Doctor', 'Chicago'),
  ('Emily', 'Williams', 30, 'Artist', 'San Francisco'),
  ('Michael', 'Brown', 22, 'Student', 'Seattle'),
  ('Sophia', 'Davis', 40, 'Lawyer', 'Boston'),
  ('David', 'Miller', 33, 'Software Developer', 'Austin'),
  ('Olivia', 'Wilson', 27, 'Marketing Specialist', 'Denver'),
  ('Daniel', 'Taylor', 38, 'Architect', 'Portland'),
  ('Grace', 'Moore', 25, 'Graphic Designer', 'Miami'),
  ('Samuel', 'Jones', 50, 'Business Consultant', 'Atlanta'),
  ('Emma', 'Hall', 31, 'Chef', 'Dallas'),
  ('William', 'Clark', 29, 'Financial Analyst', 'Houston'),
  ('Ava', 'White', 42, 'Journalist', 'San Diego'),
  ('Ethan', 'Anderson', 36, 'Product Manager', 'Phoenix')
]
check_index = [6,10,13]
def age_check(people_list, check_index):
    '''
    Перевіряє вік людей у списку (lesson 5, task 2)
    :param people_list:
    :param check_index:
    :return:
    '''
    for i in check_index:
        if people_list[i][2] > 30:
            print(f'{people_list[i][0]} {people_list[i][1]} старше 30')
        else:
            print(f'{people_list[i][0]} {people_list[i][1]} молодше 30')

age_check(people_records,check_index)

# task 9
print('==' * 20)
print('Task_9')

def perimetr(a: int ,b: int ):
    '''
    функція рахує периметр квадрата (lesson 1, task 6)
    :param a: довжина
    :param b: ширина
    :return:
    '''
    return 2*(a + b)
a9 = int(input('Довжина = '))
b9 = int(input('Ширина = '))
print('==Case with def==')
print(f'Периметр дорівнює {perimetr(a9, b9)}')

print('==Case with lambda==')
perimetr_2 = lambda x, y: print(f'Периметр дорівнює {2*(x+y)}')

perimetr_2(a9, b9)
# task 10
print('==' * 20)
print('Task_10')
list_3 = new_list()

def sred_arefm_parnyh(lst, a=0):
    '''
    Рахує середнє арифметичне усіх парних чисел у лісті (lesson 6 task 4)
    :param lst:
    :param a:
    :return:
    '''
    for i in lst:
        if i.isdigit() == True:
            if (int(i) % 2) == 0:
                a += int(i)
    return a

print(f'Сумма усіх парних чисел - {sred_arefm_parnyh(list_3)}')


"""  Оберіть будь-які 4 таски з попередніх домашніх робіт та
перетворіть їх у 4 функції, що отримують значення та повертають результат.
Обоязково документуйте функції та дайте зрозумілі імена змінним.
"""
