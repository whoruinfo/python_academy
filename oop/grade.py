'''
클래스에 학생의 이름을 입력하면
해당 학생이 얻은 3과목의 평균점수에 따라 A~F 까지 출력하세요.
'''

class Grade:
    def __init__(self, name, marks):
        self.name = name
        self.marks = []

    def addMarks(self, sMark):
       self.marks.append(int(sMark))

    def avg(self):
        #총계
        self.sum = 0

        for i in self.marks:
            self.sum += i
        return self.sum/len(self.marks)

    def grade(self, avg):
        if (avg > 90) :
            return "A"
        elif (avg > 80 and avg <= 90) :
            return "B"
        elif (avg > 70 and avg <= 80) :
            return "C"
        elif (avg > 60 and avg <= 70) :
            return "D"
        elif (avg > 50 and avg <= 60):
            return "E"
        else:
            return "F"

    @staticmethod
    def main():
        #이름 Prompt
        student = Grade(input("이름을 입력하세요."), [])

        #점수 Prompt
        for sub in ['국어', '영어', '수학']:
            try:
                student.addMarks(int(input(f"{sub} 점수는 몇점인가요?")))
            except:
                print("숫자만 입력해주세요.")
                student.addMarks(input(f"{sub} 점수는 몇점인가요?"))

        #평균 계산
        avg = student.avg()

        #등급 계산
        grade = student.grade(avg)

        if (grade != 'A' and grade != 'B' ):
            addText = "좀 더 노력하세요."
        else:
            addText = "정말 잘 하셨어요."

        # 결과
        print(f"{student.name}님의 평균점수는 {avg} 이며,"
              f"학점은 {grade}입니다."
              + addText)

if __name__ == '__main__':
    Grade.main()