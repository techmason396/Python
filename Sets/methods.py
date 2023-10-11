'''
    union(iterable) : gôp 2 set lại với nhau và loại bỏ các phần tử trùng lặp

    intersection(iterable): chỉ lấy các phần tử mà set a và b đều có (trả về một set mới kết quả và không làm thay đổi set gốc)
    intersection_update(iterable): như phương thức trên nhưng nó sẽ cập nhật kết quả và thay đổi set gốc

    difference(iterable): lấy các giá trị chỉ có ở set a mà ko có ở set b hoặc ngược lại
    difference_update(iterable): như phương thức trên nhưng nó sẽ cập nhật kết quả và thay đổi set gốc

    symmetric_difference(iterable): lấy các giá khác nhau giữa set a và set b
    symmetric_difference_update(iterable): như phương thức trên nhưng nó sẽ cập nhật kết quả và thay đổi set gốc

    issubset(iterable) : kiểm tra xem một set có phải là tập hợp con của một đối tượng iterable hay không
    issuperset(iterable): kiểm tra xem một set có phải là tập hợp cha của một đối tượng iterable hay không
    isdisjoint(iterable): kiểm tra xem một set có phải có các giá trị khác với các giá trị của một đối tượng iterable

    add() : thêm một phần tử vào trong set
    update(iterable) : thêm nhiều giá trị vào trong set
    coppy() : coppy ra một set mới

    pop() : loại bỏ phần tử cuối cùng và trả về phần tử đó
    discard(value) : loại bỏ phần tử có giá trị value
    remove(value): loại bỏ phần tử có giá trị value (nếu không có thì sẽ báo lỗi)
    clear() : xóa toàn bộ set
'''

s1 = {1,2,3,5,7}
s2 = {5,7,9,10,11}


# union
s3 = s1.union(s2)
print(s3)

# intersection
s4 = s1.intersection(s2)
print(s4)
#s1.intersection_update(s2)
#print(s1)

# difference
s5 = s1.difference(s2)
print(s5)

A = {1,2,3,4,5,6,7,8,9,10}
B = {1,2,3,5,7}
C = {4,6,8,10}
# issubset()
print(B.issubset(A))

# issuperset()
print(A.issuperset(B))
print(A.issuperset(C))

print(B.isdisjoint(C))

# add
C.add(20)
print(C)

# Coppy
Ccoppy = C.copy() 
print(Ccoppy)

# update
C.update([5,7,10,12])
C.update((10,20,30))

print(C)

# pop
print(C.pop())

#discard
C.discard(300)

print(C)