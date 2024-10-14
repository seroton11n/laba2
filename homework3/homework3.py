from datetime import datetime
def calculate_age():
    while True:
        date_of_birth = input("Введите дату рождения в формате день/месяц/год: ")
        try:
            birth_date = datetime.strptime(date_of_birth, "%d/%m/%Y")
            break
        except ValueError:
            print("Неправильный формат или несуществующая дата. Попробуйте снова.")    
    today = datetime.today()    
    age = today.year - birth_date.year    
    # Проверяем, прошел ли день рождения в этом году
    if (today.month, today.day) < (birth_date.month, birth_date.day):
        age -= 1
    print(f"Ваш возраст: {age} лет")
calculate_age()
