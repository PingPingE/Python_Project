import re
custlist=[]
page=-1
def checkDup(origin, target,target_info):
    for o in origin:
        if target == o[target_info]:
            return True
    return False
while True:
    choice=input('''
    다음 중에서 하실 일을 골라주세요 :
    I - 고객 정보 입력
    C - 현재 고객 정보 조회
    P - 이전 고객 정보 조회
    N - 다음 고객 정보 조회
    U - 고객 정보 수정
    D - 고객 정보 삭제
    Q - 프로그램 종료
    ''')  

    if choice=="I":        
        print("고객 정보 입력")
        gender,email,birthyear = '','',''
        customer = {'name':'','gender':'', 'email':'','birthyear':''}
        customer['name'] = input("이름을 입력해주세요 >> ")
        while True:
            gender = input("여성분은 F 남성분은 M을 입력해주세요. >> ")
            if gender.upper() not in ['M','F']:
                print("다시 입력해주세요")
                continue
            customer['gender'] = gender
            break
        while True:
            p = re.compile('[a-zA-Z0-9]{3,}@[a-z]{1,}[.][a-z]{1,}')
            email = input("email을 입력해주세요. 형식은 [a-zA-Z0-9]{3,}@[a-z] >> ")
            check =re.match(p,email)
            if check == None or check.group() != email:
                print("형식을 맞춰주세요")
                continue
            elif checkDup(custlist, email,'email'):
                print("이미 존재하는 이메일입니다.")
                continue
            customer['email'] = email
            break
        while True:
            birthyear = input("출생년도를 입력해주세요(4자리). >> ")
            if len(birthyear) != 4:
                print("4자리가 아닙니다. 다시 입력해주세요.")
                continue
            customer['birthyear'] = birthyear
            break
        custlist.append(customer)
        page += 1
        print("고객님의 정보가 저장되었습니다.")

    elif choice=="C":
        try:
            print("현재 고객 정보 조회")
            print(custlist[page])
        except:
            print("고객 정보가 없습니다.")

    elif choice == 'P':
        print("이전 고객 정보 조회")
        if page-1<0:
            print("현재 페이지가 첫번째 페이지 입니다.")
            print(custlist[page])
        else:
            print(custlist[page-1])
            page -= 1

    elif choice == 'N':
        print("다음 고객 정보 조회")
        if page+1>=len(custlist):
            print("현재 페이지가 마지막 페이지 입니다.")
            print(custlist[-1])
        else:
            print(custlist[page+1])
            page += 1

    elif choice=='D':
        print("고객 정보 삭제")
        target_email = input("이메일 입력 >> ")
        delok=0
        target_index = -1
        for e,i in enumerate(custlist):
            if i['email'] == target_email:
                delok=1
                target_index = e
                break
        else:
            print("존재하지 않습니다.")
            continue
        if delok:
            del(custlist[target_index])
        
    elif choice=="U": 
        print("고객 정보 수정")
        target_email = input("이메일 입력 >> ")
        target_index = -1
        for e,i in enumerate(custlist):
            if i['email'] == target_email:
                target_index = e
                break
        else:
            print("존재하지 않습니다.")
            continue
        while True:
            print(f"{custlist[target_index]}정보 수정")
            num = input("어떤 정보를 수정하시겠습니까?\n이름:0\n성별:1\nemail:2\n출생년도:3\n취소:4\n")
            if num == '0':
                custlist[target_index]['name'] = input("이름을 입력해주세요. >> ")
            elif num == '1':
                while True:
                    gender = input("여성분은 F 남성분은 M을 입력해주세요. >> ")
                    if gender.upper() not in ['M','F']:
                        print("다시 입력해주세요")
                        continue
                    custlist[target_index]['gender'] = gender
                    break
            elif num=='2':
                 while True:
                    p = re.compile('[a-zA-Z0-9]{3,}@[a-z]{1,}[.][a-z]{1,}')
                    email = input("email을 입력해주세요. 형식은 [a-zA-Z0-9]{3,}@[a-z] >> ")
                    check =re.match(p,email)
                    if check == None or check.group() != email:
                        print("형식을 맞춰주세요")
                        continue
                    customer['email'] = email
                    break
            elif num=='3':
                while True:
                    birthyear = input("출생년도를 입력해주세요(4자리). >> ")
                    if len(birthyear) != 4:
                        print("4자리가 아닙니다. 다시 입력해주세요.")
                        continue
                    custlist[target_index]['birthyear'] = birthyear
                    break   
            else:
                break
    elif choice=="Q":
        print("Bye~")
        break