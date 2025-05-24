class Train:
    def __init__(self, destination, number, departure_time):
        self.destination = destination
        self.number = number
        self.departure_time = departure_time

    def display_info(self):
        print(f"Поезд №{self.number}")
        print(f"Пункт назначения: {self.destination}")
        print(f"Время отправления: {self.departure_time}")

    @staticmethod
    def find_train(trains, number):
        for train in trains:
            if train.number == number:
                return train
        return None


def main():
    trains = [
        Train("Томск-1", "409И", "01:11"),
        Train("Новосибирск-главный", "637Н", "08:51"),
        Train("Новокузнецк", "409Н", "20:25")
    ]

    while True:
        print("\nМеню:")
        print("1. Вывести информацию о поезде")
        print("2. Вывести список всех поездов")
        print("3. Выход")

        choice = input("Выберите действие: ")

        if choice == "1":
            number = input("Введите номер поезда: ")
            train = Train.find_train(trains, number)

            if train:
                print("\nИнформация о поезде:")
                train.display_info()
            else:
                print("Поезд с таким номером не найден!")

        elif choice == "2":
            print("\nСписок всех поездов:")
            for train in trains:
                train.display_info()
                print()

        elif choice == "3":
            print("Выход из программы...")
            break

        else:
            print("Неверный ввод! Попробуйте снова.")


if __name__ == "__main__":
    main()