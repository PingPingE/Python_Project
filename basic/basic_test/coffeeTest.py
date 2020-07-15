menudic = {"아메리카노":4000, "카페라떼":4500}
while True:
    menu = int(input("----------------------------------------\n 1:메뉴 추가 2:메뉴 보기 3:주문 4:나가기 \n----------------------------------------\n"))
    if menu==1:
        item=''
        money = 0
        while True:
            item = input("추가하시길 원하는 메뉴를 적어주세요>> ")
            if item in menudic:
                print("이미 존재하는 메뉴입니다.")
                continue
            break
        
        while True:
            money =int( input("희망금액을 적어주세요>> "))
            if money<3000:
                print("너무 낮은 금액입니다.")
                continue
            elif money > 10000:
                print("너무 높은 금액입니다")
                continue
            break
        print(item)
        menudic[item] = money+500
        print(f"{item}을(를) {menudic[item]}원에 등록했습니다.")

    elif menu == 2:
        print("-------------메뉴 입니다-------------")
        for k,v in menudic.items():
            print(f"{k} : {v}원")
    elif menu == 3:
        print("커피자판기 시작!\n\n")
        print("-------------메뉴 입니다-------------")
        for k,v in menudic.items():
            print(f"{k} : {v}원")
        choicemenu =''
        while True:
            choicemenu = input("커피메뉴를 선택하세요 >> ")
            if choicemenu not in menudic:
                print("팔지않는 메뉴입니다.")
                continue
            break
        inputmoney = int(input("금액을 투입하세요 >> "))
        if menudic[choicemenu] > inputmoney:
            print("금액이 부족합니다")
        else:
            print(f"{choicemenu}음료가 나옵니다")
            print(f"남은 금액 {inputmoney-menudic[choicemenu]}을 받으세요")
    else:
        print("프로그램 종료")
        break
