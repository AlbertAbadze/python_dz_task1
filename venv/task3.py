import random

# Загадываем число
secret_number = random.randint(0, 1000)

print("Привет! Я загадал число от 0 до 1000. Попробуй угадать его!")

attempts_left = 10

while attempts_left > 0:
    try:
        guess = int(input("Введи свою попытку: "))
        if guess < 0 or guess > 1000:
            print("Число должно быть в диапазоне от 0 до 1000.")
            continue
    except ValueError:
        print("Некорректный ввод. Введи целое число.")
        continue

    if guess == secret_number:
        print("Поздравляю! Ты угадал число!")
        break
    elif guess < secret_number:
        print("Загаданное число больше.")
    else:
        print("Загаданное число меньше.")

    attempts_left -= 1
    if attempts_left > 0:
        print(f"У тебя осталось {attempts_left} попыток.")
    else:
        print("У тебя закончились попытки. Желаю удачи в следующий раз!")

print(f"Загаданное число было: {secret_number}.")