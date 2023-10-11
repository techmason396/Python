'''
    .append(object) : thêm một đối tượng vào cuối list
    .extend(iterable) : thêm nhiều đối tượng vào list
    .insert(i, x) : chèn đối tượng x vào vị trí index i
    .copy() : coppy list ra một list mới và sẽ không ảnh hưởng đến list cũ
    .pop(index)
        - mặc định không truyền tham sô lấy ra phần tử cuối cùng trong list và trả về phần tử vừa lâý ra
        - lấy phần tử tại vị trí index ra khỏi list và trả về phần tử đó

    del list[start:end] : xóa các phần tử từ vị trí index start đến end trong list
    .remove(x): xóa phần tử dựa trên giá trị (xóa phần tử có giá trị x đầu tiên được tìm thấy) nếu ko tìm thấy giá trị trong list sẽ báo lỗi
    .clear(): xóa tất cả các phần tử trong list

    .index(x,start,end) : tìm vị trí index của giá trị x đầu tiên được tìm thấy trong đoạn từ start đến end
                          nếu không tìm thấy sẽ báo lỗi
    .count(x):  đếm số lần xuất hiện của giá trị x trong list
    .reverse(): đảo ngược một list
    .sort(): sắp xếp giá trị list theo mức tăng dần
        + sort(reverse=True): sắp xếp giá trị giảm dần
        + sort(key=str.lower): sắp xếp các giá trị chữ cái với key = str.lower (chuyển tất cả các chữ thành chữ thường)

        
'''

list1 = [1,2,3,4]

# append()
list1.append(5)
print(list1)

# extend()
list1.extend([6,7,8])
print(list1)

# insert()
list1.insert(3, 4.5)
print(list1)

list2 = list1.copy()
list2[0]= 100
print(list1)
print(list2)

#pop()
pop1 = list2.pop()
print(pop1)
print(list2)

#pop(index)
pop2 = list2.pop(0)
print(list2)
print(pop2)

#del
del list2[0:3]
print(list2)

# remove
list3 = [1,5,5,2,7,3,4]
list3.remove(5)
print(list3)

# clear
list3.clear()
print(list3)

# index
l1 = [5,6,7,5,8,9,6,10,6]
print(l1.index(5,1,8))

#count
print(l1.count(5))

# reverse
l1.reverse()
print(l1)

# sort
l1.sort()
print(l1)
#sort(reverse=True)
l1.sort(reverse=True)
print(l1)

lstr = ['yy','jj','mm','BB','aa','ZZ']
lstr.sort(key=str.lower)
'''
    lưu ý chữ hoa nhỏ hơn chữ thường
    ord('char') : dùng để xem giá trị của chữ cái
'''
print(lstr)

print(ord('A'))
print(ord('a'))

lstr.sort(key=str.lower, reverse=True)
print(lstr)

