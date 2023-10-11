# tạo một dict rỗng
dict1 = {}
dict1_1 = dict()


# tạo một dict có các giá trị key và value
dict2 = dict(((1,2),(2,5),(3,6)))
print(dict2)

dict2_2 = dict(('ab','cd','ef'))
print(dict2_2)

# tạo một dict gộp 2 list vại với nhau theo kiểu key và value
dict3 = dict(zip(['A','B','C'],['apple','ball','cat']))
print(dict3)

dict3_1 = dict(zip("AJK",[1,2,3]))
print(dict3_1)


# sử dụng enumerate để tạo một dict sử dụng index làm key và giá trị làm value
dict4 = dict(enumerate(['A','B','C']))
print(dict4)

# sử dụng phương thức viết rút gọn để tạo ra dict
dict5 = {x : x**2 for x in range(1,10)}
print(dict5)

# sử dụng function enumerate(iterable) để truy cập phần tử key và value
for key, value in enumerate(dict3):
    print(f"{key} la : {value}")

