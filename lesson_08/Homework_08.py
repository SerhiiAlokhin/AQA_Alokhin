list_1 = ["1,2,3,4", "1,2,3,4,50", "qwerty1,2,3"]

def summ(list_a):
    try:
        for item in list_a:
            list_b = item.split(',')
            sum_of_elements = 0
            for i in list_b:
                sum_of_elements += int(i)
            print(sum_of_elements)
    except ValueError:
        print('Не можу це зробити!')



print(list_1)
summ(list_1)


