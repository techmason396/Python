'''
    {}
    dùng để lưu trữ danh sách các giá trị có giá trị duy nhất và không bị trùng lặp
    - không thể truy cập vào phần tử thông qua index
    - không thể cắt set như trong list
    - các phần tử trong set sắp xếp ngẫu nhiên chứ không có thứ tự
'''

s1 = {1,2,3,4,'trung','vui','quang',2}
print(s1)

print(set('NguyenThanhTrung'))

s2 = {10,20,30,40,50}
print(s2)

A = {1,2,3,5,7}
B = {5,7,9,10,11}

'''
    union là lấy tập hợp 2 giá trị của A và B và loại bỏ các giá trị trùng lặp
    intersection là lấy phần tử mà A và B đều có
    
'''