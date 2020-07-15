class FourCal:
    mode = 1
    def __init__(self, first=1, second = 4):
        self.first =first
        self.second = second
        print("생성자")

    def setdata(self, first, second):
        self.first = first
        self.second = second

    def add(self):
        return self.first + self.second
    
    
a = FourCal()
print(a.first, a.second)
a.setdata(3,6)
a.mode= 1
result_a = a.add()

b= FourCal()
b.setdata(2,2)
result_b = b.add()

print(a.first, a.second)
print(b.first, b.second)
print(a.mode, b.mode)
print(result_a, result_b)
print("mode: ",a.mode, b.mode)

a.mode=10
print("mode: ",a.mode, b.mode)