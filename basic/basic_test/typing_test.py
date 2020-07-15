import time
import random
li = ['딱딱하기는 삼 년 묵은 박달나무 같다', '하루에 3시간을 걸으면 7년 후에 지구를 한바퀴 돌 수 있다.', '언제나 현재에 집중할수 있다면 행복할것이다.','한번의 실패와 영원한 실패를 혼동하지 마라.']
cnt = 0
print("---타자게임---")
input("엔터를 누르면 시작합니다")
start = time.time()
for i in range(0,2):
    target = li[random.randint(0,len(li))]
    ans = input(target+"\n")
    if ans == target:
        print("정답")
        cnt += 1
    else:
        print("오답")
end = time.time()
print(f"{cnt}개 맞췄고, {end-start}초 걸렸음")

