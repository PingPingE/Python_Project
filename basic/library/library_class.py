class library:
    def __init__(self, booklist, next_id):
        self.booklist = booklist
        self.next_id = next_id

    def add(self, name, publisher, author, summary,stock):
        book = {}
        book['id'] = self.next_id
        book['name'] = name
        book['publish'] = publisher
        book['author'] = author
        book['summary'] = summary
        book['stock'] = stock
        self.next_id += 1
        self.booklist.append(book)

    def check(self,target_func):
        target_id =-1   
        while True:
            target_name = ''
            target_author = ''
            target_publisher = ''
            target_name = input(f"{target_func}하실 도서의 제목을 입력해주세요 >> ")
            cnt =0
            for i in self.booklist:
                if i['name'] ==target_name:
                    target_id = i['id']
                    cnt += 1
            if cnt == 0:
                print("존재하지 않습니다. 다시 입력해주세요.")
                continue
            elif cnt == 1:

                break
            elif cnt >1:
                print("같은 제목의 도서가 존재합니다. 추가 정보를 입력해주세요.")
                target_author = input("저자를 입력해주세요 >> ")
                target_publisher=input("출판사를 입력해주세요 >> ")
                cnt =0
                target_list = []
                for i in self.booklist:
                    if i['name']==target_name and i['author'] == target_author and i['publisher'] == target_publisher:
                        target_id=i['id']
                        target_list.append(i)
                        
                if len(target_list) == 0:
                    print("존재하지 않습니다. 다시 입력해주세요.")
                    continue
                elif len(target_list) == 1:
                    break
                else:
                    print("중복된 도서가 많습니다. 다음 목록을 보시고 id를 입력해주십시오.")
                    target_id = int(input(f"{target_list} \n id를 입력해주십시오."))
                    break
        return target_id

    def update_name(self, target_id, new_name):
        self.booklist[target_id]['name'] = new_name

    def update_publisher(self, target_id, new_publisher):
        self.booklist[target_id]['publisher'] = new_publisher

    def update_author(self, target_id, new_author):
        self.booklist[target_id]['authoer'] = new_author

    def update_summary(self, target_id, new_summary):
        self.booklist[target_id]['summary'] = new_summary
    
    def update_stock(self, target_id, new_stock):
        self.booklist[target_id]['stock'] = new_stock
    
    def delete(self, target_id):
        del(self.booklist[target_id])
    
    def show_list(self):
        print(self.booklist)
    


    