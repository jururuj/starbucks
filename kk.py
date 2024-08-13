from enum import Enum

class Menu(Enum):
    ADD = 1
    REMOVE = 2
    CHECK = 3
    ORDER = 4
    END = 5

class ItemList:
    def __init__(self):
        self.items = []
        self.max_items = 10

    def add_item(self, item):
        if len(self.items) < self.max_items:
            self.items.append(item)
            return True
        else:
            return False

    def remove_item(self, item_index):
        if 0 <= item_index < len(self.items):
            self.items.pop(item_index)
            return True
        else:
            return False

    def check_items(self):
        return self.items

    def total_items(self):
        return len(self.items)

def select():
    print("========== What Do You Want ==========")
    print("1. 음료추가")
    print("2. 음료 삭제")
    print("3. 선택 음료 확인")
    print("4. 선택 음료 주문")
    print("5. 프로그램 종료")

def add_menu(item_list):
    print("========== Add Menu ==========")
    for i in range(1, 11):
        print(f"{i}. 음료 {i}")
    print("10. 동작 취소")
    
    choice = int(input("선택: "))
    
    if 1 <= choice <= 9:
        if item_list.add_item(f"음료 {choice}"):
            print(f"음료 {choice}가 추가되었습니다.")
        else:
            print("더 이상 음료를 추가할 수 없습니다.")
    elif choice == 10:
        print("동작이 취소되었습니다.")
    else:
        print("잘못된 입력입니다.")

def remove_menu(item_list):
    print("========== Remove Menu ==========")
    for i, item in enumerate(item_list.check_items()):
        print(f"{i+1}. {item}")
    
    choice = int(input("선택: ")) - 1
    
    if item_list.remove_item(choice):
        print("선택한 음료가 삭제되었습니다.")
    else:
        print("잘못된 선택입니다.")

def check_menu(item_list):
    print("========== 선택 음료 확인 ==========")
    if item_list.total_items() > 0:
        print(", ".join(item_list.check_items()))
    else:
        print("선택한 음료가 없습니다.")

def order(item_list):
    print("========== 선택 음료 주문 ==========")
    if item_list.total_items() > 0:
        print(f"주문 품목 총액 {item_list.total_items() * 1000}원 입니다. 품목은 다음과 같습니다.")
        print(", ".join(item_list.check_items()))
        
        print("주문하시겠습니까?")
        print("1: yes")
        print("2: no")
        
        choice = int(input("선택: "))
        
        if choice == 1:
            print("주문이 완료되었습니다.")
            return True
        else:
            print("주문이 취소되었습니다.")
            return False
    else:
        print("선택한 음료가 없습니다.")
        return False

def main():
    item_list = ItemList()
    while True:
        select()
        choice = int(input("선택: "))
        print("\n\n")

        if choice == Menu.ADD.value:
            add_menu(item_list)
            print("\n\n")
        elif choice == Menu.REMOVE.value:
            remove_menu(item_list)
            print("\n\n")
        elif choice == Menu.CHECK.value:
            check_menu(item_list)
            print("\n\n")
        elif choice == Menu.ORDER.value:
            if order(item_list):
                print("주문 완료. 프로그램을 종료합니다.")
                break
            else:
                print("주문 보류!")
                print("\n\n")
        elif choice == Menu.END.value:
            print("프로그램을 종료합니다.")
            break
        else:
            print("잘못된 입력입니다. 동작을 취소합니다.")
            break

if __name__ == "__main__":
    main()
