class Worker:
    def __init__(self, name, surname, rate, days):
        self.__name = name
        self.__surname = surname
        self.__rate = rate
        self.__days = days

    def get_name(self):
        return self.__name

    def get_surname(self):
        return self.__surname

    def get_rate(self):
        return self.__rate

    def get_days(self):
        return self.__days

    def GetSalary(self):
        return self.__rate * self.__days


if __name__ == "__main__":
    worker = Worker("Иван", "Петров", 1500, 20)

    print(f"Работник: {worker.get_surname()} {worker.get_name()}")
    print(f"Ставка за день: {worker.get_rate()} руб.")
    print(f"Отработано дней: {worker.get_days()}")

    salary = worker.GetSalary()
    print(f"Зарплата: {salary} руб.")