class Calculation:
    def __init__(self):
        self.__calculationLine = ""

    def SetCalculationLine(self, value):
        self.__calculationLine = value

    def SetLastSymbolCalculationLine(self, symbol):
        self.__calculationLine += str(symbol)

    def GetCalculationLine(self):
        return self.__calculationLine

    def GetLastSymbol(self):
        if len(self.__calculationLine) > 0:
            return self.__calculationLine[-1]
        return None

    def DeleteLastSymbol(self):
        if len(self.__calculationLine) > 0:
            self.__calculationLine = self.__calculationLine[:-1]

if __name__ == "__main__":
    calc = Calculation()

    calc.SetCalculationLine("2+3")
    print("Текущая строка:", calc.GetCalculationLine())  # 2+3

    calc.SetLastSymbolCalculationLine("*")
    print("После добавления '*':", calc.GetCalculationLine())  # 2+3*

    print("Последний символ:", calc.GetLastSymbol())  # *

    calc.DeleteLastSymbol()
    print("После удаления последнего символа:", calc.GetCalculationLine())  # 2+3

    calc.SetLastSymbolCalculationLine("4")
    calc.SetLastSymbolCalculationLine("/")
    calc.SetLastSymbolCalculationLine("2")
    print("После добавления '4/2':", calc.GetCalculationLine())  # 2+34/2

    calc.SetCalculationLine("10*5")
    print("Новая строка вычислений:", calc.GetCalculationLine())  # 10*5