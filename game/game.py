import random
def play_rps():
    options = ['камень', 'ножницы', 'бумага']
    user_choice = input("Выберите: камень, ножницы или бумага: ").lower()
    if user_choice not in options:
        print("Неверный выбор. Пожалуйста, выберите 'камень', 'ножницы' или 'бумага'.")
        return
    computer_choice = random.choice(options)
    print(f"Ваш выбор: {user_choice}")
    print(f"Выбор компьютера: {computer_choice}")
    if user_choice == computer_choice:
        print("Ничья!")
    elif (user_choice == 'камень' and computer_choice == 'ножницы') or \
         (user_choice == 'ножницы' and computer_choice == 'бумага') or \
         (user_choice == 'бумага' and computer_choice == 'камень'):
        print("Вы победили!")
    else:
        print("Вы проиграли!")
play_rps()
