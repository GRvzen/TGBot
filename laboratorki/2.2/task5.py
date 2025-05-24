class DemoClass:
    def __init__(self, prop1="default1", prop2="default2"):
        self.property1 = prop1
        self.property2 = prop2
        print(f"Создан объект со свойствами: {self.property1}, {self.property2}")

    def __del__(self):
        print(f"Удаление объекта со свойствами: {self.property1}, {self.property2}")

    def display_properties(self):
        print(f"Свойство 1: {self.property1}")
        print(f"Свойство 2: {self.property2}")


def main():
    print("1. Создание объекта с параметрами по умолчанию:")
    obj1 = DemoClass()
    obj1.display_properties()

    print("\n2. Создание объекта с заданными параметрами:")
    obj2 = DemoClass("value1", "value2")
    obj2.display_properties()

    print("\n3. Создание временного объекта:")
    DemoClass("temp1", "temp2").display_properties()

    print("\n4. Явное удаление объекта:")
    obj3 = DemoClass("to_delete1", "to_delete2")
    del obj3

    print("\nКонец работы программы (автоматическое удаление оставшихся объектов)...")


if __name__ == "__main__":
    main()