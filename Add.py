def __init__(self):
    self.select_menu = []

def add_menu(itme_list):
    print("""
        ========== Add Menu ==========
        
        1. 아메리카노: 4500
        2. 카페라떼: 5000
        3. 콜드브루: 4900
        4. 에스프레소: 4000
        5. 아이스티: 5900
        6. 말차라떼: 6100
        
        10. 동작 취소
        
        """)
    
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
            