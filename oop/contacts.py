'''
이름, 전화번호, 이메일, 주소를 받아서
연락처 입력, 출력, 삭제하는 프로그램을 완성하시오
'''
class Contacts:
    def __init__(self, name, tel, email, address):
        self.name = name
        self.tel = tel
        self.email = email
        self.address = address

    def print_info(self):
        print(f"이름:{self.name}, 전화번호{self.tel}"
              f",이메일:{self.email}, 주소:{self.address}")

    @staticmethod
    def set_contact():
        name = input("이름 : ")
        tel = input("전화번호 : ")
        email = input("이메일 : ")
        address = input("주소 : ")

        return Contacts(name, tel, email, address)

    @staticmethod
    def get_contacts(lsContact):
        print("####### 주소록 ###################")
        for i in lsContact:
            i.print_info()
        print("#################################")

    @staticmethod
    def del_contact(lsContact, name):
        for i, j in enumerate(lsContact):
            if j.name == name:
                print(f"-----{i}")
                del lsContact[i]

    @staticmethod
    def print_menu():
        print("---------------------------------------------")
        print("1.연락처 입력")
        print("2.연락처 출력")
        print("3.연락처 삭제")
        print("4.종료")
        menu = input("메뉴를 입력하세요 : ")

        return menu

    @staticmethod
    def main():
        ls = []

        while 1:

            menu = Contacts.print_menu()

            if menu == "1":
                contact = Contacts.set_contact()
                ls.append(contact)
            elif menu == "2":
                Contacts.get_contacts(ls)
            elif menu == "3":
                name = input("삭제할 이름을 입력하세요.")
                Contacts.del_contact(ls, name)
            elif menu == "4":
                break


if __name__ == '__main__':
    Contacts.main()