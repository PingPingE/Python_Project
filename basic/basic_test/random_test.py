import random
import time
cnt = 0
# for x in range(0,10):
#     a = random.randint(1,50)
#     b = random.randint(1,50)
#     print(f"{a}+{b}=",a+b)
#     c = int(input())
#     if a+b == c:
#         print("정답")
#         cnt +=1
#     else:
#         print("오답")
# print(f"총 {cnt}개 맞추셨습니다.")

total = 3
input("엔터를 누르면 시작")
start = time.time()
for x in range(0,total):
    a = random.randint(1,50)
    b= random.randint(1,50)
    op = random.choice(["+","-","/","*"])
    ans = int(input(f"{a}{op}{b}=?\n"))
    if ans == int(eval(f"{a}{op}{b}")):
        print("정답")
        cnt += 1
    else:
        print("오답")
        print(f"정답은 {int(eval(f'{a}{op}{b}'))}입니다.")
end = time.time()
print(f"{total}개 중 {cnt}개를 맞추셨고 {end-start}초 걸리셨습니다.")