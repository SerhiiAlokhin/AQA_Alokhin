def count_par (lst, a=0):
    for i in lst:
        if i.isdigit() == True:
            if (int(i) % 2) == 0:
                a += int(i)
    return a

while True:
    lst1 = []
    count_of_elem = input('Need to create new list, choose count of element: ')
    if count_of_elem.isdigit():
        for i in range(int(count_of_elem)):
            element = input(f'Enter {i} element: ')
            lst1.append(element)
        print(lst1)
        print(f'Сумма усіх парних чисел - {count_par(lst1)}')
        print('=='*20)
    else:
        print('Not valid value')
        break