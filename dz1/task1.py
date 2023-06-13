def check_triangle(a, b, c):
    # Проверка условия треугольника
    if a + b > c and b + c > a and c + a > b:
        # Определение типа треугольника
        if a == b == c:
            return "Равносторонний треугольник"
        elif a == b or b == c or c == a:
            return "Равнобедренный треугольник"
        else:
            return "Разносторонний треугольник"
    else:
        return "Треугольника с такими сторонами не существует"


# Пример использования
a = float(input("Введите длину стороны a: "))
b = float(input("Введите длину стороны b: "))
c = float(input("Введите длину стороны c: "))

result = check_triangle(a, b, c)
print(result)