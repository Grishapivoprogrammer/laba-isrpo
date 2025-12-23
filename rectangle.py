def area(a, b):
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
        raise TypeError("Стороны должны быть числами")
    if a < 0 or b < 0:
        raise ValueError("Стороны не могут быть отрицательными")
    return a * b


def perimeter(a, b):
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
        raise TypeError("Стороны должны быть числами")
    if a < 0 or b < 0:
        raise ValueError("Стороны не могут быть отрицательными")
    return 2 * (a + b)


if __name__ == "__main__":
    # Пример использования
    print("Демонстрация работы модуля:")
    print(f"Площадь прямоугольника 5x10: {area(5, 10)}")
    print(f"Периметр прямоугольника 5x10: {perimeter(5, 10)}")