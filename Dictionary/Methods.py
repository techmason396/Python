'''
    copy() : copy ra một dict mới tách biệt dict cũ
    update() : thêm nhiều giá trị cho một dict
    setdefault(key, default) : phương thức này lấy giá trị value thông qua key như phương thức get()
            + nếu không tìm thấy key thì nó sẽ tự động thêm key, value vào dict

    fromkeys(sequence, value) : sử dụng tập hợp iterable làm key và cài đặt giá trị mặc định là value

    pop(key, default) : xóa một phần đối tượng key trong dict và trả về giá trị của key đó
            + nếu không tìm thấy để tránh lỗi thì nên đặt giá trị default để trả về

    popitem() : xóa phần tử cuối cùng trong dict và trả về giá trị xóa
    clear() : xóa sạch dict về rỗng
'''

dict1 = {101: 'Production', 102: 'Accounts', 103:'Sale & Marketing', 104:'Inventory'}

# copy()
dict2 = dict1.copy()
dict2[102] = 'Developer'
print(dict1)
print(dict2)

# update()
dict3 = {105 : 'Help desk', 106: 'Training Manager'}
dict1.update(dict3)
print(dict1)

# setdefault()
print(dict1.setdefault(105,"hello World"))

# fromkeys()
dict4 = {}
keyDict4 = [1,2,3,4]
dict4 = dict4.fromkeys(keyDict4, 'Hello')
print(dict4)

# pop()
d1 = dict1.pop(102, 'not found')
print(dict1)

# popitem()
d2 = dict1.popitem()
print(d2)
print(dict1)

D = dict()

for x in enumerate(range(2)):

    D[x[0]] = x[1]

    D[x[1]+7] = x[0]

print(D)