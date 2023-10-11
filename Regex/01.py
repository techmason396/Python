

# tìm số điện thoại trong text
text = 'This is my number: 555-333-4444 and the office is : 666-777-8888'
# kiểm tra có phải số điện thoại không bằng cách thông thường
# 092-946-7332
phone_number = '092-496-7332'
def is_phone_number(p_string):
    if len(p_string) != 12 or p_string[3] != "-" or p_string[7] != "-":
        # not phone number 
        return False
    for i in range(0,3):
        # isdecimal => kiểm tra các kí tự có phải là số hay không
        if not p_string[i].isdecimal():
            return False
    for i in range (5,7):
        if not p_string[i].isdecimal():
            return False
    for i in range(9,12):
        if not p_string[i].isdecimal():
            return False
    return True


for i in range(len(text)):
    text_find_number = text[i:i+12]
    if is_phone_number(text_find_number):
        print(f"I found phone number: {text_find_number}")


# sử dụng biểu thức chính quy 
import re
'''
   . : khớp với bất kỳ ký tự nào trừ ký tự xuống dòng
   ^ : khớp với đầu của chuỗi hoặc dòng
   $ : khớp với cuối của chuỗi hoặc dòng
   * : khớp với 0 hoặc nhiều lần xuất hiện của mẫu trước đó
   ? : khớp với 0 hoặc 1 lần xuất hiện của mẫu trước đó
   () : nhóm các mẫu lại để áp dụng phép toán regex vào nhóm
   [] : định nghĩa một tập hợp các kí tự có thể khớp
   [^] : định nghĩa các kí tự không được khớp
   \ : dùng để tránh ký tự đặc biệt hoặc tạo chuỗi đặc biệt

'''
# .
dot_text  = 'gray green grey' # khớp với 'gray' hoặc 'grey' nhưng không khớp với 'green'
dot = re.findall('gr.y', dot_text)
print(dot)

#^
mu_text = 'start something start'
mu = re.search('^start', mu_text) # khớp với chuỗi 'start' ở đầu chuỗi
print(mu.group())

#$
end_text = "find to end" # khớp với 'end' nếu nó ở cuối chuỗi
end = re.search('end$',end_text)
print(end.group())

#*
sao_text = "xin chao 1234 tôi da 45679 tuoi roi 49 nam nua se reset"
sao = re.findall('\d*',sao_text) # khớp với bất kỳ cuỗi nào có chứa số hoặc rỗng
print(sao)

'''
    \d : khớp với một chữ số bất kỳ từ 0-9
    \d\d : khớp với 2 chữ số liên tiếp
    \d+ : khớp với một hoặc nhiều chữ số
    \d{3} : khớp chính xác 3 chữ số liên tiếp
    \d$ :  khớp với một chuỗi chứa duy nhất một chữ số
'''

'''
    hàm re.search(biểu thức, chuỗi cần tìm) => tìm ra một giá  trị đầu tiên khớp => (sử dụng group() để hiển thị kq)
    hàm re.findall(biểu thức, chuỗi cần tìm) => tìm ra các giá trị khớp với biểu thức (trả về một list kq)

'''



m = re.search('\d{3}-\d{3}-\d{4}',text)
print(m.group())
print(" ")
f_all = re.findall('\d{3}-\d{3}-\d{4}',text)
print(f_all)




    
     

