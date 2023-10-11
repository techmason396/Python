'''
    abs(number) : chuyển về  giá trị tuyệt đối
    ascii(str) : chuyển str về bảng mã ascii
    bool(obj) : chuyển đổi các obj thành kiểu bool
    callable(nameFunction): kiểm tra xem nameFuction có được tạo chưa
    chr(number): chuyển đối số sang mã ascii
    dir(datatype) : kiểm tra danh sách các phương thức của datatype
    enumerate(list) : hàm liệt đưa ra các chỉ mục cho list
    eval(str): hàm tính toán dựa trên một chuỗi
    filter(function, iterator): hàm lọc dữ liệu dựa trên function
    float(number): chuyển đổi số về kiểu float
    hash(object): cung cấp mã băm cho object
    help(object.function): cung cấp thông tin phương thức của object
    isinstance(object, class): kiểm tra xem một object có phải là thể hiện của class hay không
    map(function, iterators) : thực hiện một function cho các đối tượng trong iterator
    min(iterable): tìm giá trị nhỏ nhất trong iterable
    max(iterable): tìm giá trị lớn nhất trong iterable
    sorted(iterable,reverse=False) : sắp xếp một đối tượng iterable
    slice(start:end:step): cài đặt phương thức cắt cho slice
    zip(list1, list2): kết hợp 2 list lại làm một
    revesersed(iterable): đảo ngược giá trị của một iterable
    pow(number, lũy thừa): hàm lũy thừa của số n
    round(float number): làm tròn xuống
'''

# abs
print(abs(-15))

# ascii()
letter = '\u0521'
print(letter)
print(ascii(letter))

# bool()
print(bool('trung'))

# callable()
def tinh_tong(a,b):return a+b
print(callable(tinh_tong))

#chr()
print(chr(65))

#dir()
print(dir(dict))

#enumerate()
L = ['a','b','c','d']
for i in enumerate(L):
    print(i)

# eval()
print(eval('10 + 20 * 5 /2'))

# filter()
L = [1,3,5,4,2,9,8,10,12]
def even(number):
    if number % 2 == 0:
        return True
    else:
        return False

filterL = filter(even, L)
for i in filterL:
    print(i)


#hash()
str1 = "trung"
print(hash(str1))
print(help(str1.lower))

# isinstance()
print(isinstance(str1,str))

# map()
L1 = [1,3,5,7,9]
def Double_Value(n):
    return n*2

doubleList = map(Double_Value, L1)
for i in doubleList:
    print(i)

# min, max
print(min(L1))
print(max(L1))

# sorted
sorted1 = sorted(L1)
sorted2 = sorted(L1, reverse=True)
print(sorted1)
print(sorted2)

# slice()
slice1 = slice(0,2)
s1 = L1[slice1]
print(s1)

# zip()
L2 = [20,9,30,15,33]
L3 = zip(L1,L2)
for i in L3:
    print(i)

# reversed()
for i in reversed(L2):
    print(i)

# pow()
print(pow(5,5))
