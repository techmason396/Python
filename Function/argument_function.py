# truyền nhiều tham số ko biết trước ta sử dụng dấu *
def fun1(*args):
    print(args)

fun1(10,20,30,40)

L1 = [10,20,30]

def fun2(a,b,c):
    print(a,b,c)

# giải nén các dữ liệu trong một iterator làm tham số ta sử dụng dấu *iterator để giải nén
fun2(*L1)

# trả về nhiều giá trị
def fun3(a, b, c):
    return a+10, b+10, c+10

a, b, c = fun3(*L1)
tubple_result = fun3(*L1)
print(a, b, c)
print(tubple_result)

# cách truyền nhiều tham số không biết trước với key và value
def fun4(**args):
    print(args)
    for i in args:
        print(i)

fun4(name='trung',age=10,job='manager')