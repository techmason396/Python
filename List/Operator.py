'''
    + : tạo ra một list mới chứa 2 list gộp lại với nhau
    .extend([object]): thêm phẩn tử cho list (thay đổi trên list cũ và ko tạo ra list mới)
    * : lặp lại các phần tử trong list và trả về một list mới
    in : kiểm tra một giá trị có tồn tại trong một list hay không
    not in : kiểm tra một giá trị có không tòn tại trong list hay không
'''

list1 = [1,2,3]

# extend
list1.extend(['trung','vui','quang'])
list2 = [8,9,10]
#  +
list3 = list1 + list2
print(list3)

# *
list4 = list1 * 3
print(list4)

# in
print('quang' in list1)

# not in
print('hello' in list1)