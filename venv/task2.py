def is_prime(num):
    if num < 2:  # Проверка на отрицательные числа и 1
        return False
    if num == 2:  # 2 является простым числом
        return True
    if num % 2 == 0:  # Проверка на четность
        return False
    for i in range(3, int(num ** 0.5) + 1, 2):  # Проверка делителей до квадратного корня числа
        if num % i == 0:
            return False
    return True


while True:
    try:
        num = int(input("Введите число: "))
        if num < 0 or num > 100000:
            print("Введите число в допустимом диапазоне.")
        else:
            break
    except ValueError:
        print("Введите целое число.")

if is_prime(num):
    print(f"{num} - простое число.")
else:
    print(f"{num} - составное число.")
