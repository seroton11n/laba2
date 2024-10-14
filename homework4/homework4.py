import random
def find():
    numbers = [random.randint(0, 200) for _ in range(10)]
    while True:
        try:
            x = int(input("введите цифру, на которую будут делиться числа: "))
            break
        except ValueError:
            print("пожалуйста, введите целое число.")
    # Использование лямбда-функции для поиска кратных чисел
    multiples = list(filter(lambda num: num % x == 0, numbers))
    print("сгенерированные числа:", numbers)
    print(f"числа из списка кратные {x}:", multiples)
find()
