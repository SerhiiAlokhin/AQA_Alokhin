def sred_aref(list_a, count_of_elements=0, sum_of_elements=0):
        for i in list_a:
            count_of_elements += 1
            sum_of_elements += i
        return sum_of_elements / count_of_elements



'''деление на ноль, пустой лист
голден пасс
test_all_non_digits
test_zero_and_non_digits
'''

def perimetr(a: int ,b: int ):
    '''
    функція рахує периметр квадрата (lesson 1, task 6)
    :param a: довжина
    :param b: ширина
    :return:
    '''
    if a*b > 0 and a+b >= 0:
        return 2*(a + b)
    pass

'''голден пасс
отрицательные значения
не валидные значения
'''

def page_counter(photo: int, photo_per_list: int):
    '''
    calculate page for album (lesson 3 task 9)
    :param photo: count of users photo
    :param photo_per_list: photo on page
    :return:
    '''
    pages = photo // photo_per_list
    if photo % photo_per_list == 0:
        return pages
    return (pages + 1)

''' 0 photo
0 photo per list
golden pass +0
golden pass +1
'''