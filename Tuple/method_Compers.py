'''
    count() : đếm số lần xuất hiện của giá trị trong tuple
    index()

'''

# phương pháp viết rút gọn tạo tuple bằng for
t1 =  (*(x for x in range(10)),)
print(t1)

# truy cập gái trị tại vị trí index
print(t1.index(8))