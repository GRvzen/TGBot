class NumberPair:
    def __init__(self, num1=0, num2=0):
        self.num1 = num1
        self.num2 = num2

    def display_numbers(self):
        print(f"Число 1: {self.num1}")
        print(f"Число 2: {self.num2}")

    def set_numbers(self, new_num1, new_num2):
        self.num1 = new_num1
        self.num2 = new_num2

    def calculate_sum(self):
        return self.num1 + self.num2

    def find_max(self):
        return max(self.num1, self.num2)


def main():
    pair = NumberPair()
    print("Создан объект с числами по умолчанию:")
    pair.display_numbers()

    while True:
        print("\nМеню:")
        print("1. Изменить числа")
        print("2. Вывести текущие числа")
        print("3. Вычислить сумму чисел")
        print("4. Найти наибольшее число")
        print("5. Выход")

        choice = input("Выберите действие (1-5): ")

        if choice == "1":
            try:
                num1 = int(input("Введите первое число: "))
                num2 = int(input("Введите второе число: "))
                pair.set_numbers(num1, num2)
                print("Числа успешно изменены!")
            except ValueError:
                print("Ошибка! Вводите только целые числа.")

        elif choice == "2":
            print("\nТекущие числа:")
            pair.display_numbers()

        elif choice == "3":
            print(f"Сумма чисел: {pair.calculate_sum()}")

        elif choice == "4":
            print(f"Наибольшее число: {pair.find_max()}")

        elif choice == "5":
            print("Выход из программы...")
            break

        else:
            print("Неверный ввод! Пожалуйста, выберите действие от 1 до 5.")


if __name__ == "__main__":
    main()