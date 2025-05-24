class Student:
    def __init__(self, surname, birth_date, group_number, grades):
        self.surname = surname
        self.birth_date = birth_date
        self.group_number = group_number
        self.grades = grades if len(grades) == 5 else [0] * 5

    def set_surname(self, new_surname):
        self.surname = new_surname

    def set_birth_date(self, new_birth_date):
        self.birth_date = new_birth_date

    def set_group_number(self, new_group_number):
        self.group_number = new_group_number

    def display_info(self):
        print(f"Фамилия: {self.surname}")
        print(f"Дата рождения: {self.birth_date}")
        print(f"Номер группы: {self.group_number}")
        print(f"Успеваемость: {self.grades}")

    @staticmethod
    def find_student(students, surname, birth_date):
        for student in students:
            if student.surname == surname and student.birth_date == birth_date:
                return student
        return None

def main():
    students = [
        Student("Иванов", "01.01.2000", "ГР-101", [5, 4, 3, 5, 4]),
        Student("Петров", "15.05.2001", "ГР-102", [4, 4, 4, 3, 5]),
        Student("Сидорова", "20.11.1999", "ГР-101", [5, 5, 5, 5, 5])
    ]

    while True:
        print("\nМеню:")
        print("1. Изменить данные студента")
        print("2. Найти студента по фамилии и дате рождения")
        print("3. Вывести список всех студентов")
        print("4. Выход")

        choice = input("Выберите действие: ")

        if choice == "1":
            surname = input("Введите фамилию студента для изменения: ")
            birth_date = input("Введите дату рождения студента (в формате ДД.ММ.ГГГГ): ")
            student = Student.find_student(students, surname, birth_date)

            if student:
                print("\nТекущие данные студента:")
                student.display_info()

                print("\nКакие данные изменить?")
                print("1. Фамилию")
                print("2. Дату рождения")
                print("3. Номер группы")
                print("4. Вернуться в меню")

                sub_choice = input("Выберите действие: ")

                if sub_choice == "1":
                    new_surname = input("Введите новую фамилию: ")
                    student.set_surname(new_surname)
                    print("Фамилия изменена успешно!")
                elif sub_choice == "2":
                    new_birth_date = input("Введите новую дату рождения (в формате ДД.ММ.ГГГГ): ")
                    student.set_birth_date(new_birth_date)
                    print("Дата рождения изменена успешно!")
                elif sub_choice == "3":
                    new_group = input("Введите новый номер группы: ")
                    student.set_group_number(new_group)
                    print("Номер группы изменен успешно!")
                elif sub_choice == "4":
                    continue
                else:
                    print("Неверный ввод!")
            else:
                print("Студент не найден!")

        elif choice == "2":
            surname = input("Введите фамилию студента: ")
            birth_date = input("Введите дату рождения студента (в формате ДД.ММ.ГГГГ): ")
            student = Student.find_student(students, surname, birth_date)

            if student:
                print("\nИнформация о студенте:")
                student.display_info()
            else:
                print("Студент не найден!")

        elif choice == "3":
            print("\nСписок всех студентов:")
            for idx, student in enumerate(students, 1):
                print(f"\nСтудент #{idx}")
                student.display_info()

        elif choice == "4":
            print("Выход из программы...")
            break

        else:
            print("Неверный ввод! Попробуйте снова.")


if __name__ == "__main__":
    main()