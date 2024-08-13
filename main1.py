# Main function
from enum import Enum

class Menu(Enum):
    ADD = 1
    REMOVE = 2
    CHECK = 3
    ORDER = 4
    END = 5
    
class ItemList:
    def __init__(self):
        self.name = []
        self.total = 0
        self.menu = {
            '아메리카노': 4500,
            '카페라떼': 5000,
            '콜드브루': 4900,
            '에스프레소': 4000,
            '아이스티': 5900,
            '말차라떼': 6100
        }

def select():
    print('======== What do you wnat? ==========')
    print('1.음료추가')
    print('2.음료삭제')
    print('3.선택 음료 확인')
    print('4.선택 음료 주문')
    print('5.프로그램 종료')

def add_menu(list_):
    print('====== ADD MENU =====')
    print('1. 아메리카노')
    print('2. 카페라떼')
    print('3. 콜드브루')
    print('4. 에스프레소')
    print('5. 아이스티')
    print('6. 말차라떼')

    n = int(input('선택: '))
    if len(list_.name) > 10:
        print('음료는 10개까지 주문가능')
        return

    for idx, name in enumerate(list_.menu):
        if n == idx+1:
            list_.name.append(name)
            list_.total += list_.menu[name]
    if not 0 < n < 7:
        print('존재하지 않는 번호입니다')

def remove_menu(list_):
    print('====== REMOVE MENU =====')

    n = int(input('선택: '))
    for idx, name in enumerate(list_.menu):
        if n == idx+1:
            list_.name.remove(name)
            list_.total -= list_.menu[name]
        else:
            print('주문한 메뉴가 없습니다. 다시 확인해주세요')
            break
        
        
    if not 0 < n < 7:
        print('존재하지 않는 번호입니다')
    print(list_.name)
    
def check_menu(list_):
    print(f'주문메뉴 : {list_.name}')
    print(f'주문 총액 : {list_.total}')

def order(list_):
    print(f'주문메뉴 : {list_.name}')
    print(f'주문 총액 : {list_.total}')
    print('주문하시겠습니까?')
    print('1. YES')
    print('2. NO')
    ch = int(input('선택:'))
    
    if ch == 1:
        return 1
    else:
        return 0

def main():
    item_list = ItemList()
    while True:
        select()
        choice = int(input("선택: "))
        print("\n\n")

        if choice == Menu.ADD.value:
            add_menu(item_list)
            print(item_list.name)
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
            print("프로그램을 종료합니다")
            break
        else:
            print("잘못된 입력입니다. 동작을 취소합니다.")
            break

if __name__ == "__main__":
    main()
