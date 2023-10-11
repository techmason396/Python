'''
    | : union
    & : intersection
    - : difference
    ^ : symmetric_difference
    < : issubset
    <=
    > : supperset
    >= 
    == : kiểm tra 2 set bằng nhau
    != : kiểm tra 2 set khác nhau
    in : kiểm tra một giá trị có trong một set
    not in : kiểm tra một giá trị không có trong một set
'''

S = {1,2,3,4,5,6,7,8,9,10}
A = {1,2,3,5,7}
B = {5,7,9,10,11}

# toán tử | tương tự hàm union
s1 = A | B
print(s1)

# toán tử &  = hàm intersection
s2 = A & B
print(s2)

# toán tử - = hàm difference
s3 = A - B
print(s3)

# toán tử ^ = hàm  symmetric_difference
s4 = A ^ B
print(s4)
A.symmetric_difference

# toán tử < = hàm issubset
print(A < S)

# toán tử > = hàm supperset
print(S > A)

print(A == B)

# toán tử in và not in

print(10 in S)
print(12 not in B)