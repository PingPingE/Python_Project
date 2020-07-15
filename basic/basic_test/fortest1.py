str="abcdefg"
list1 = list(range(1,7))
list2 = list(range(7,13))
dic = {1:'hi',2:'hello'}
set1 = {1,2,3,3,3,4,4,5,5,5,1}
tuple1 = (1,2,3,4,5,4,4,5,5)
# for i in list1:
#     print(i)
# for s in set1:
#     print(s)

for t in tuple1:
    print(t)

for i in list1:
    for j in list2:
        print(i,j)
        