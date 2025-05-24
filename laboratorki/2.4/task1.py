import sqlite3
from dataclasses import dataclass


@dataclass
class Student:
    first_name: str
    last_name: str
    middle_name: str
    group: str
    grades: list[int]


class StudentDatabase:
    def __init__(self, db_name='students.db'):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self._create_table()

    def _create_table(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS students (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            first_name TEXT NOT NULL,
                            last_name TEXT NOT NULL,
                            middle_name TEXT,
                            group_name TEXT NOT NULL,
                            grade1 INTEGER NOT NULL,
                            grade2 INTEGER NOT NULL,
                            grade3 INTEGER NOT NULL,
                            grade4 INTEGER NOT NULL)''')
        self.conn.commit()

    def add_student(self, student: Student):
        self.cursor.execute('''INSERT INTO students 
                            (first_name, last_name, middle_name, group_name, grade1, grade2, grade3, grade4)
                            VALUES (?, ?, ?, ?, ?, ?, ?, ?)''',
                            (student.first_name, student.last_name, student.middle_name,
                             student.group, *student.grades))
        self.conn.commit()

    def get_all_students(self):
        self.cursor.execute('SELECT id, first_name, last_name, group_name FROM students')
        return self.cursor.fetchall()

    def get_student(self, student_id):
        self.cursor.execute('''SELECT * FROM students WHERE id = ?''', (student_id,))
        data = self.cursor.fetchone()
        if data:
            return Student(
                first_name=data[1],
                last_name=data[2],
                middle_name=data[3],
                group=data[4],
                grades=list(data[5:9])
            )
        return None

    def update_student(self, student_id, student: Student):
        self.cursor.execute('''UPDATE students SET
                            first_name = ?,
                            last_name = ?,
                            middle_name = ?,
                            group_name = ?,
                            grade1 = ?,
                            grade2 = ?,
                            grade3 = ?,
                            grade4 = ?
                            WHERE id = ?''',
                            (student.first_name, student.last_name, student.middle_name,
                             student.group, *student.grades, student_id))
        self.conn.commit()

    def delete_student(self, student_id):
        self.cursor.execute('DELETE FROM students WHERE id = ?', (student_id,))
        self.conn.commit()

    def get_group_average(self, group_name):
        self.cursor.execute('''SELECT grade1, grade2, grade3, grade4 
                            FROM students WHERE group_name = ?''', (group_name,))
        grades = self.cursor.fetchall()
        if not grades:
            return 0

        total = 0
        count = 0
        for student_grades in grades:
            total += sum(student_grades)
            count += len(student_grades)
        return round(total / count, 2) if count > 0 else 0

    def close(self):
        self.conn.close()


def print_menu():
    print("\nМеню:")
    print("1. Добавить нового студента")
    print("2. Просмотреть всех студентов")
    print("3. Просмотреть одного студента")
    print("4. Редактировать студента")
    print("5. Удалить студента")
    print("6. Просмотреть средний балл группы")
    print("7. Выход")


def input_student():
    first_name = input("Введите имя: ")
    last_name = input("Введите фамилию: ")
    middle_name = input("Введите отчество: ")
    group = input("Введите группу: ")
    grades = []
    for i in range(1, 5):
        grade = int(input(f"Введите оценку {i}: "))
        grades.append(grade)
    return Student(first_name, last_name, middle_name, group, grades)


def main():
    db = StudentDatabase()

    while True:
        print_menu()
        choice = input("Выберите действие: ")

        if choice == "1":
            student = input_student()
            db.add_student(student)
            print("Студент успешно добавлен!")

        elif choice == "2":
            students = db.get_all_students()
            if not students:
                print("Нет студентов в базе данных")
            else:
                print("\nСписок студентов:")
                for student in students:
                    print(f"{student[0]}. {student[1]} {student[2]} ({student[3]})")

        elif choice == "3":
            student_id = int(input("Введите ID студента: "))
            student = db.get_student(student_id)
            if student:
                avg = sum(student.grades) / len(student.grades)
                print(f"\nИнформация о студенте:")
                print(f"ФИО: {student.last_name} {student.first_name} {student.middle_name}")
                print(f"Группа: {student.group}")
                print(f"Оценки: {student.grades}")
                print(f"Средний балл: {avg:.2f}")
            else:
                print("Студент не найден")

        elif choice == "4":
            student_id = int(input("Введите ID студента для редактирования: "))
            student = db.get_student(student_id)
            if student:
                print("Текущие данные:")
                print(f"1. Имя: {student.first_name}")
                print(f"2. Фамилия: {student.last_name}")
                print(f"3. Отчество: {student.middle_name}")
                print(f"4. Группа: {student.group}")
                print(f"5. Оценки: {student.grades}")

                field = input("Введите номер поля для редактирования (1-5): ")
                if field == "1":
                    student.first_name = input("Новое имя: ")
                elif field == "2":
                    student.last_name = input("Новая фамилия: ")
                elif field == "3":
                    student.middle_name = input("Новое отчество: ")
                elif field == "4":
                    student.group = input("Новая группа: ")
                elif field == "5":
                    grades = []
                    for i in range(4):
                        grades.append(int(input(f"Новая оценка {i + 1}: ")))
                    student.grades = grades

                db.update_student(student_id, student)
                print("Данные обновлены")
            else:
                print("Студент не найден")

        elif choice == "5":
            student_id = int(input("Введите ID студента для удаления: "))
            db.delete_student(student_id)
            print("Студент удален")

        elif choice == "6":
            group = input("Введите название группы: ")
            avg = db.get_group_average(group)
            print(f"Средний балл группы {group}: {avg:.2f}")

        elif choice == "7":
            db.close()
            print("Выход из программы")
            break

        else:
            print("Неверный ввод. Попробуйте снова.")


if __name__ == "__main__":
    main()