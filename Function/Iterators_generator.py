'''
    iterators là các đối tượng có thể sử dụng vòng lặp được như (list, tuple, string, dict, set)
        iter(object) : phương thức chuyển object về iterators
            + next(iterator) : truy cập từng phần tử của iterator

    generator là tạo các dãy giá trị mà ko cần lưu trữ tất cả giá trị trong bộ nhớ cùng một lúc
        thay vì sử dụng câu lệnh "return" để trả về kết quả thì sử dụng câu lệnh "yeild"
            + yeild: lệnh này sẽ tạm dừng trả về giá trị hiện tại cho đến khi kết thúc
'''

# iterators
L = [1,2,3,4]
iter = iter(L)
print(next(iter))
print(next(iter))
print(next(iter))
print("")

# generator 
def countdown(seconds):
    while seconds > 0:
        yield seconds
        seconds -= 1

seconds = countdown(5)
for i in seconds:
    print(i)