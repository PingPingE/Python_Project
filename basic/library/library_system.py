import re
from library_class import library
book = library([], 0)
while True:
    choice=input('''
    다음 중에서 하실 일을 골라주세요 :
    1. 도서 추가\n
    2. 도서 정보 수정\n
    3. 도서 정보 삭제\n
    4. 도서 목록\n
    5. 나가기
    ''')  

    if choice=="1":        
        print("도서 정보 입력")
        book.add(input("제목을 입력해주세요 >> "),input("출판사를 입력해주세요 >> "),
        input("저자를 입력해주세요 >> "), input("책에 대해 간단한 소개를 해주세요 >> "),
        input("재고를 입력해주세요 >> "))
        print("새로운 도서가 추가되었습니다.")

    elif choice=="2":
        if len(book.booklist)==0:
            print("도서정보가 없습니다.")
            continue
        print("도서 정보 수정")
        target_id = book.check("수정")
        print(f"{book.booklist[target_id]} 정보 수정")
        while True:
            num = input("어떤 정보를 수정하시겠습니까?\n제목:0\n출판사:1\n저자:2\n소개:3\n재고:4\n취소:5\n")
            if num == '0':
                book.update_name(target_id,input("제목을 입력해주세요. >> "))
            elif num == '1':
                book.update_publisher(target_id,  input("출판사를 입력해주세요. >> "))
            elif num=='2':
                book.update_author(target_id,input("저자를 입력해주세요. >> ") )
            elif num=='3':
                book.update_summary(target_id,input("책소개를 입력해주세요. >> ") )
            elif num =='4':
                book.update_stock(target_id,input("재고를 입력해주세요. >> ") )
            else:
                break

    elif choice == '3':
        if len(book.booklist)==0:
            print("도서정보가 없습니다.")
            continue
        print("도서 정보 삭제")
        target_id = book.check("삭제")
        if input(f"{book.booklist[target_id]}을 삭제하시겠습니까? y/n >> ").lower() == 'y':
            book.delete(target_id)
        else:
            print("삭제를 취소하셨습니다.")

    elif choice == '4':
        print("도서 목록 조회")
        book.show_list()
        
    else:
        print("Bye~")
        break