class Worker:
    def __init__(self, name, surname, rate, days):
        self.name = name
        self.surname = surname
        self.rate = rate
        self.days = days

    def get_salary(self):
        return self.rate * self.days


if __name__ == "__main__":
    worker = Worker("Иван", "Петров", 1500, 20)

    print(f"Работник: {worker.surname} {worker.name}")
    print(f"Ставка за день: {worker.rate} руб.")
    print(f"Отработано дней: {worker.days}")

    salary = worker.get_salary()
    print(f"Зарплата: {salary} руб.")