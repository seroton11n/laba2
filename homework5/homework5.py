def get_number():
    return [num for num in range(30) if num % 2 != 0]
numbers = get_number()
first = numbers[0]
fifth = numbers[4]
last = numbers[-1]
print(f"Первое нечетное число: {first}")
print(f"Пятое нечетное число: {fifth}")
print(f"Последнее нечетное число: {last}")
