from IPython.testing.plugin.show_refs import C

from oop.titanic.views.controller import Controller
from oop.titanic.templates.plot import Plot

if __name__ == '__main__':
    def print_menu():
        print('0. Exit')
        print('1. 시각화')
        print('2. 모델링')
        print('3. 머신러닝')
        print('4. 머신생성')

        return input("메뉴를 입력해주세요.\n")

    app = Controller()

    while 1:
        menu = print_menu()

        if menu == '1':
            print("---------- 1 시각화실행 ----------")
            plot = Plot('train.csv')

            menu = input('차트내용 선택 \n'
                         '1. 생존자 vs 사망자 \n'
                         '2. 생존자 성별 대비 \n')
            if menu == '1':
                plot.plot_survived_dead()
            if menu == '2':
                plot.plot_sex()

        elif menu == '2':
            print("---------- 2 모델링 ----------")
            app.modeling('train.csv', 'test.csv')
        elif menu == '3':
            print("---------- 3 머신러닝 ----------")
        elif menu == '4':
            print("---------- 4 머신생성 ----------")
        elif menu == '0':
            break
