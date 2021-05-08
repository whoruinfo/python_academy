'''
이름, 전화번호, 이메일, 주소를 받아서
연락처 입력, 출력, 삭제하는 프로그램을 완성하시오
'''
from astropy.extern.configobj.configobj import ConfigObj


class Contacts:

    # 간소화 구조
    name = ''
    tel = ''
    email = ''
    address = ''

    def __str__(self):
        return f"이름:{self.name} \n" \
               f"전화번호 : {self.tel}\n" \
               f"이메일:{self.email}\n" \
               f" 주소:{self.address} \n"

class ContactService :

    def set_contact(self):
        obj = Contacts()
        obj.name = input("이름 : ")
        obj.tel = input("전화번호 : ")
        obj.email = input("이메일 : ")
        obj.address = input("주소 : ")

        return obj

    def get_contacts(self, ls):
        for i in ls:
            print(i)

    def del_contact(self, ls, name):
        for i, j in enumerate(ls):
            if j.name == name:
                print(f"-----{i}")
                del ls[i]

    def print_menu(self):
        print(" 1.연락처 입력 \n 2.연락처 출력 \n 3.연락처 삭제 \n 4.종료")
        menu = input("메뉴를 입력하세요 : ")

        return int(menu)

    @staticmethod
    def main():
        ls = []

        service = ContactService()

        while 1:
            menu = service.print_menu()
            if menu == 1:
                contact = service.set_contact()
                ls.append(contact)
            elif menu == 2:
                service.get_contacts(ls)
            elif menu == 3:
                name = input("삭제할 이름을 입력하세요.")
                service.del_contact(ls, name)
            elif menu == 4:
                break

if __name__ == '__main__':
    ContactService.main()