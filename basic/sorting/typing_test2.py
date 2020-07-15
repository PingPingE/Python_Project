import random,time,pickle,json,os
w = {}
with open('./basic/sorting/rank.json', 'rt') as f:
    rank =json.load(f)
'''
시간, 이름
'''
name = ''
while True:
    if len(name)==0:
        name = input("이름을 입력하세요 >> ")
    print(f"{name}님 환영합니다.")
    num = int(input('''
    1. 타자게임 \n
    2. 문제불러오기 \n
    3. 문제저장하기 \n
    4. 문제 등록/수정/삭제 \n
    5. 등수 보기\n
    6. 나가기\n
    메뉴 선택 >> \t
    '''))
    if num==1:
        if len(w) == 0:
           print("문제를 불러와주세요")
           continue
        input("엔터를 누르면 시작합니다.")
        q=random.choice(list(w))
        n=1
        start=time.time()
        while n<=len(w)//2:
            print("{}번".format(n))
            if q ==input(f"{q}\n"):
                print("통과!")
                n=n+1
                q=random.choice(list(w))
            else:
                print("오타! 다시도전!")  
        end=time.time()
        rank[name]=end-start
        print(f"{name}님의 타자시간: {rank[name]}")
        with open('./basic/sorting/rank.json','wt') as f:
            json.dump(rank,f,indent=4)

    elif num==2:
         with open('./basic/sorting/word.json','rt') as f:
             w=json.load(f)
    
    elif num==3:
        with open('./basic/sorting/word.json','wt') as f:
            json.dump(w,f,indent=4)
    
    elif num==4:
        if len(w) == 0:
            print("문제를 먼저 불러와주세요")
            continue
        menu = int(input("1. 등록\n2. 수정\n3. 삭제\n"))
        print(menu)
        if menu==1:
            while True:
                new_word = input("등록을 원하시는 단어를 입력하세요>> ")
                if len(new_word)>1 :
                    w[new_word] = new_word
                    print("등록 되었습니다.")
                    break
                elif new_word in w:
                    print("이미 존재하는 단어입니다. 다시 입력해주세요")
                else:
                    print("길이가 너무 짧습니다. 다시 입력해주세요")
        elif menu ==2:
            target_word = ''
            while True:
                while True:
                    target_word = input(f"{w.keys()}\n수정을 원하시는 단어를 입력하세요>> ")
                    if target_word not in w:
                        print("그런 단어가 없습니다. 다시 입력해주세요")
                        continue
                    break
                new_word = input(f"{target_word}에서 어떤 단어로 바꾸시겠습니까?>> ")
                if len(new_word)>1 :
                    w.pop(target_word)
                    w[new_word] = new_word
                    print("수정 되었습니다.")
                    break
                else:
                    print("길이가 너무 짧습니다. 다시 입력해주세요")

        elif menu==3:
            del_target=''
            while True:
                del_target = input(f"{w.keys()}\n 어떤 단어를 삭제하시길 원하십니까?")
                if del_target not in w:
                    print("다시 입력해주세요")
                    continue
                break
            if input(f"{del_target} 해당 단어를 삭제하시길 원하시면 1을 입력해주세요.")=='1':
                w.pop(del_target)
            else:
                print("삭제를 원하지 않으시므로 다시 메뉴로 돌아갑니다.")
                continue
            
            
    elif num==5:
        with open('./basic/sorting/rank.json','rt')as f:
            rank = json.load(f)
        print(sorted(rank.items(), key= lambda x: x[1]))
        
    else:
        print(f"{name}님 bye")
        break