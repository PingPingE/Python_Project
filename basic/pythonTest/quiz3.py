class StudentClass:
    def __init__(self, students_list, next_id):
        self.students_list = students_list
        self.next_id = next_id
    
    def create(self):
        print("학생 정보 입력")
        student = {'s_id':self.next_id}
        student['name'] = input("이름을 입력해주세요 >> ")
        student['major'] = input("학과를 입력해주세요 >> ")
        student['phone'] = input("전화번호를 입력해주세요 >> ")
        student['address'] = input("주소를 입력해주세요 >> ")
        
        self.students_list.append(student)
        self.next_id += 1
        print(f"{student['name']}님의 정보가 저장되었습니다.")

    def get_index(self, func):
        stat =True
        target_index=-1
        while stat:
            print("----학생 정보----")
            for i in self.students_list:
                for k,v in i.items():
                    print(f"{k}: {v}")
            target_id = int(input(f"위 학생 정보를 확인하시고 {func}을/를 원하시는 학생의 s_id를 입력해주세요:"))
            for e,i in enumerate(self.students_list):
                if i['s_id'] == target_id:
                    target_index=e
                    stat= False
                    break
            else:
                print("해당하는 학생이 없습니다. 다시 입력하십시오.")
        return target_index

    def update(self):
        print("학생 정보 수정")
        if len(self.students_list) == 0:
            print("저장된 정보가 없습니다.")
            return
        target_index= self.get_index("수정")
        while True:
            print(f"{self.students_list[target_index]['name']}님의 정보 수정")
            num = input("어떤 정보를 수정하시겠습니까?\n이름:0\n학과:1\n전화번호:2\n주소:3\n취소:4\n")
            if num == '0':
                self.students_list[target_index]['name'] = input("이름을 입력해주세요. >> ")
            elif num == '1':
                self.students_list[target_index]['major'] = input("학과를 입력해주세요 >> ")
            elif num=='2':
                self.students_list[target_index]['phone'] = input("전화번호를 입력해주세요 >> ")
            elif num=='3':
                self.students_list[target_index]['address'] = input("주소를 입력해주세요 >> ")
            else:
                break

    def delete(self):
        print("학생 정보 삭제")
        if len(self.students_list) == 0:
            print("저장된 정보가 없습니다.")
            return
        target_index= self.get_index("삭제")
        if input(f"{self.students_list[target_index]} 정보를 삭제하시겠습니까? y/n >> ").lower() == 'y':
            del(self.students_list[target_index])
    
    def print(self):
        if len(self.students_list) >0:
            print("학생 정보 출력")
            for i in self.students_list:
                for k,v in i.items():
                    print(f"{k}: {v}")
                
        else:
            print("저장된 정보가 없습니다.")

st = StudentClass([],0)
while True:
    choice=input('''
    다음 중에서 하실 일을 골라주세요
    C - 학생 정보 입력
    R - 학생 정보 출력
    U - 학생 정보 수정
    D - 학생 정보 삭제
    Q - 프로그램 종료
    >> ''')  

    if choice=="C":        
        st.create()

    elif choice=="R":
        st.print()

    elif choice=="U": 
        st.update()
      
    elif choice=='D':
        st.delete()
        
    elif choice=="Q":
        print("Bye~")
        break