import random

def play_game():
    secret_number = random.randint(1, 100)
    attempts = 0

    print("Добро пожаловать в игру 'Угадай число'!")

    while True:
        guess = int(input("Введите число от 1 до 100: "))
        attempts += 1

        if guess &lt; secret_number:
            print("Загаданное число больше.")
        elif guess &gt; secret_number:
            print("Загаданное число меньше.")
        else:
            print(f"Поздравляю! Вы угадали число за {attempts} попыток.")
            break

if __name__ == "__main__":
    play_game()
