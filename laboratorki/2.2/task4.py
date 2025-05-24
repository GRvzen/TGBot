class Counter:
    def __init__(self, initial_value=0):
        self.__value = initial_value

    def increment(self):
        self.__value += 1

    def decrement(self):
        self.__value -= 1

    @property
    def value(self):
        return self.__value


def main():
    print("Создаем счетчик со значением по умолчанию (0):")
    counter1 = Counter()
    print(f"Текущее значение: {counter1.value}")

    print("\nСоздаем счетчик с начальным значением 5:")
    counter2 = Counter(5)
    print(f"Текущее значение: {counter2.value}")

    while True:
        print("\nМеню:")
        print("1. Увеличить счетчик")
        print("2. Уменьшить счетчик")
        print("3. Показать текущее значение")
        print("4. Выход")

        choice = input("Выберите действие: ")

        if choice == "1":
            counter2.increment()
            print("Значение увеличено на 1")

        elif choice == "2":
            counter2.decrement()
            print("Значение уменьшено на 1")

        elif choice == "3":
            print(f"Текущее значение счетчика: {counter2.value}")

        elif choice == "4":
            print("Выход из программы")
            break

        else:
            print("Неверный ввод! Пожалуйста, выберите 1-4")


if __name__ == "__main__":
    main()