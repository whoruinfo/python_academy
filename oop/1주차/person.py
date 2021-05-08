class Person:
    def __init__(self):
        self.name = input("누구예요?")
        self.age = input("몇살이예요?")
        self.address = input("어디서 살아요??")

    def greeting(self):
        print(f"안녕하세요. 제 이름은 {self.name} 이고,"
              f"나이는 {self.age}살 입니다."
              f"{self.address}에서 거주합니다.")

    @staticmethod
    def main():
        maria = Person()
        maria.greeting()

        tom = Person()
        tom.greeting()

if __name__ == '__main__':
    Person.main()
