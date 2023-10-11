# import thư viện đa luồng
from threading import *

def display():
    for i in range(65, 91):
        print(chr(i))

# tạo một luồng chạy riêng
t = Thread(target=display, name='Alphabets')
t.start()

for i in range(65, 91):
    print(i)

