
'''
    close(): dùng để đóng file
    readline(): dùng để đọc 1 dòng trong file
        - kết quả trả về là một string
    readlines(): đùng để đọc nhiều dòng trong một file
        - kết quả trả về là một list các dòng trong file
    write()": dùng để ghi dữ liệu vào file
    writelines(): dùng để ghi một list dự liệu vào file
'''

file = open('data.txt', 'r')

# readline()
line = file.readline()
print(line)

line = file.readline()
print(line)

#readlines()
file.seek(0)
lines = file.readlines()
print(lines)
file.close()

# write
w_fun = open("w_fun.txt",'w')
data1 = "Hello\nMay Cung\nChuy la python"
w_fun.write(data1)
w_fun.close()

# w writelines
wlines_fun = open("wline_fun.txt",'w')
data2 = ["Trung\n","Vui\n","Quang\n","Hanh\n"] 
wlines_fun.writelines(data2)
wlines_fun.close()