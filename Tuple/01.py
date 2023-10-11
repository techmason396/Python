'''
    ()
    tuple như list nhưng không thể thay thổi giá trị cho tuple được
    giá trị của tuple là bất biến

'''

t1 = tuple('Python')
print(t1)

# packing t1 = 10,20,30,40 print(t1)
type(t1)

# unpack
a,b,c,d = t1
print(a)
print(b)
print(c)
print(d)








