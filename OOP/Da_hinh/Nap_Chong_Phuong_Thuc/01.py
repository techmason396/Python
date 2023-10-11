'''
    nạp chồng phương thức  là tạo phương thức cùng tên trong một lớp
    - phương thức cuối cùng cùng tên được định nghĩa sẽ ghi đè lên các phương thức trước đó
      điều này có nghĩa chỉ có một phiên bản của phương thức cùng tên được duyệt tính từ trên
      xuống và sử dụng trong lớp đó
    
      Lưu ý trong python ko khuyến nghị sử dụng nạp chồng phương thức mà khuyến khích sử dụng *args và **kwargs
      để xử lý các trường hợp khách nhau

'''

class Calculator:
    def add(self, a, b):
        return a + b
    
    def add(self, a, b, c):
        return a + b + c

    # cách khắc phục khi sử dụng xử lý cho nhiều trường hợp
    def sum(self, a, b, c=None):
        if c==None:
            return a + b
        return a + b + c
        
c = Calculator()
c.add(10, 20, 30)

print(c.sum(10, 5))
print(c.sum(10, 5, 20))





