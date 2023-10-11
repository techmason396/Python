'''
    index [] : truy cập phần tử tại ví trí index
    slice [:] 
        + [:] -> lấy ra các phần tử từ 0 - len(list)
        + [start: ] -> lấy ra các phần tử từ vị trí index start đến len(list)
        + [start:end:step] -> lấy ra các phần tử từ vị trí index start đến end và nhảy cóc số lần step
        + [::-1] -> đảo ngược list
'''

list1 = [1,2,3,4,5,6,7,8,9,10]
# truy cập và in ra đối tượng có giá trị là 7 trong list
# cách 1
print(list1[6])

#cách 2
print(list1[-4])


#Slice
print(list1[:])
print(list1[3:])
print(list1[0:9:2])
print(list1[::-1])

# xóa các phần tử từ 0 -> end sau đó thay thế bằng  list mới
list1[0:3] = [10,20,30, 40 , 50]
print(list1)


