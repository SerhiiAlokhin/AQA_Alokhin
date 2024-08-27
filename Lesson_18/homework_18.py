def generator1(n):
    a = 0
    while a<=n:
        yield a
        a += 2

N = 15 # Певне число N
for number in generator1(N):
    print(number)

print('=='*20)

def generator2(n):
    a, b = 0, 1
    while a<=n:
        yield a
        a, b = b , a+b

for number in generator2(N):
    print(number)

print('==' * 20)

def track_back(lst):  # ітератор для зворотного виведення елементів списку
    list1 = lst[::-1]
    for item in list1:
        print(item)

test_list =  [0, 2, 4, 6, 8, 10, 11, 14]
track_back(test_list)
print('==' * 20)
def pair_iter(n):
    for i in range(n):
        if i % 2 == 0:
            print(i)

pair_iter(N)

print('==' * 20)
def log_args_and_result(func):
    def wrapper(*args, **kwargs):
        print(f"Виклик функції: {func.__name__}")
        print(f"Аргументи: {args}")
        result = func(*args, **kwargs)
        print(f"Результат: {result}")
        return result
    return wrapper

@log_args_and_result
def add(a, b):
    return a + b

add(2, 1)

print('==' * 20)
def handle_exceptions(exception_type=Exception):
    def decorator(func):
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except exception_type as e:
                print(f"Error: {e}")
        return wrapper
    return decorator

# Використання декоратора
@handle_exceptions(ZeroDivisionError)
def divide(a, b):
    return a / b

divide(10, 0)