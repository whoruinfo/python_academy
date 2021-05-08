class Calculator:
    remember = 0

    #  초기화 함수
    def __init__(self, first, second):
        self.first = first
        self.second = second

    # 덧셈 함수
    def sum(self):
        return self.first + self.second

    # 뺄셈 함수
    def sub(self):
        return self.first - self.second

    # 곱셈 함수
    def mul(self):
        return self.first * self.second

    # 나눗셈 함수
    def div(self):
        return self.first / self.second

    # 나머지 함수
    def mod(self):
        return self.first % self.second

    @staticmethod
    def execute():
        calc = Calculator(int(input("첫번째 수 : ")), int(input("두번째 수 : ")))
        print(f"{calc.first} + {calc.second} = {calc.sum()}")
        print(f"{calc.first} - {calc.second} = {calc.sub()}")
        print(f"{calc.first} * {calc.second} = {calc.mul()}")
        print(f"{calc.first} / {calc.second} = {calc.div()}")
        print(f"{calc.first} % {calc.second} = {calc.mod()}")

if __name__ == '__main__':
    Calculator.execute()