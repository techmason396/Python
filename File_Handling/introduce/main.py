'''
    open(file name, mode) :  là function dùng để mở file với các mode và trả về một đối tương file
        mode:
            nếu ko điền giá trị mode thì mặc định sẽ là "r"
            + "r" : đọc file hiện có hiện tại nếu ko tìm thấy file sẽ báo lõi FileNotFoundError
            + "w": thêm nội dung vào file (mode này sẽ xóa toàn bộ dữ liệu file sau đó mới thêm mới nội dung vào,)
                - nếu tệp tồn tại nó sẽ xóa tệp hiện tại và tạo tệp mới
                - nếu tệp không tồn tại thì nó sẽ tạo file mới
            + "a": thêm nội dụng vào file (mode này sẽ không xóa dữ liệu file mà thêm tiếp nội dung vào cuối file)
                - nếu file ko tồn tại thì nó sẽ tạo file mới
                - nếu file tồn tại thì nó sẽ thêm tiếp nội dung vào cuối file 
            + "r+": giống với mới 'a' 
            + "w+": viết xong rồi đọc
            + "a+": thêm vào cuối rồi đọc
            + "x": thêm dữ liệu vào file mới
                - nếu file không tồn tại thì nó sẽ tạo ra một file mới
                + nếu file đã tồn tại thì nó sẽ báo lỗi FileExistError và sẽ không ghi được
    seek(number): dịch chuyển con trỏ trong file
    read(number): đùng để đọc đối tượng trả về từ hàm open()
        number: là số kí tự muống đọc, nếu không điền thì mặc định đọc toàn bộ file

    close(): thực hiện chức năng đóng file sau khi sử dụng để giải phóng tài nguyên
'''

handle_file = open("dot.txt","r")
print(type(handle_file))

str1 = handle_file.read()

print(str1)
print(type(str1))

handle_file.close()

# "w" mode
write_mode = open("w_mode.txt", 'w')
write_mode.write(str1)
write_mode.close()

# 'a' mode
a_mode = open("a_mode.txt",'a')
a_mode.write(str1)
a_mode.close()

# "w" mode
w_plush_mode = open('w_plush.txt','w+')
w_plush_mode.write(str1)
w_plush_mode.seek(0) # dịch chuyển về vị trí đầu tiên trong file
str2 = w_plush_mode.read()
print(str2)
w_plush_mode.close()

