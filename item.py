class ItemList:
    def __init__(self):
        self.beverage = []
        self.total_price = 0
        
    def add_item(self, item):
        if len(self.beverage) <= 10:
            self.beverage.append(item)
            return True
        else:
            return False
        
    def select():
        print("========== What Do You Want ==========")
        print("1. 음료추가")
        print("2. 음료 삭제")
        print("3. 선택 음료 확인")
        print("4. 선택 음료 주문")
        print("5. 프로그램 종료")
    
    def add_menu(item_list):
        total = 0
        while (total > 10):
            user_input = int(input('선택: '))
            
            if user_input == 10:
                print('음료 추가를 취소합니다')
                break
            elif (user_input >= 1) and (user_input <= 6):
                menu_name = self.menu[num]
                self.select_menu.append(menu_name)
                total += 1
                print(f'{menu_name} 추가')
            else:
                print('메뉴 번호는 1~6까지입니다.')