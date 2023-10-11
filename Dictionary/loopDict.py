'''
    get(key) : phương thức lấy giá trị từ một key trong dict 
        + phương thức này ưu việt hơn phương pháp index (dict[]) là nó không có gây ra lỗi khi truy cập key không tồn tại
        + get(key,mess)  : khi truyền thêm mess thì nếu key không được tìm thấy trong dict thì nó sẽ báo mess

    keys() : lấy các giá trị key trong dict
    values() : lấy các giá trị value trong dict
    items() : lấy các giá trị key : value trong dict
'''

dict1 = {101:"Production",102:"Accounts",103:"Sales & Marketing",104:"Inventory"}

# in các key của dict
for key in dict1:
    print(key)

# in các key và value trong một dict sử dụng index
for key in dict1:
    print(f"key: {key} and value: {dict1[key]}")


# in các key và value trong một dict sử dụng phương thức get
print("")
for key in dict1:
    print(f"key: {key} and value: {dict1.get(key)}")


# sử dụng phương thức get(key, mess)
print(dict1.get(111,"Key not valid"))

# lấy danh sách các key : keys()
keys = dict1.keys()
print(keys)

# lấy danh sách các values : values()
values = dict1.values()
print(values)

# lấy danh sách các giá trị key : value trong dict
items = dict1.items()
print(items)

for key, value in dict1.items():
    print(f"Key: {key} - Value: {value}")