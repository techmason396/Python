'''
    version : 1.0

'''
from tkinter import *
from tkinter import ttk
import webbrowser

from libs import Nettruyenco

def open_browser(event):
    item = tree.selection()[0]
    link = tree.item(item, 'values')[3]
    webbrowser.open(link)

list_url_commic = [
    'https://nettruyenco.vn/truyen-tranh/shuumatsu-no-valkyrie-6399',
    'https://nettruyenco.vn/truyen-tranh/vuong-gia-thien-ha-245',
    'https://nettruyenco.vn/truyen-tranh/jujutsu-kaisen-chu-thuat-hoi-chien-5058',
    'https://nettruyenco.vn/truyen-tranh/hiep-khach-giang-ho-218'
]

nettruyen = Nettruyenco(list_url_commic)
nettruyen.get_data_chapter_from_list_url()
data = nettruyen.data

# windown
windown = Tk()
windown.minsize(width=700, height=500)

# tạo một widget Treeview
tree = ttk.Treeview(windown, columns=('Name','Chapter', 'Update'), show='headings')
tree.heading("Name", text="Tên truyện")
tree.heading("Chapter", text="Chương")
tree.heading('Update', text="Cập nhật")

# đỗ dữ liệu vào Treeview
for item in data:
    tree.insert("","end",values=(item['Name'], item['Chapter'],item['Update'],item['Link']))

tree.grid(row=1, column=0)

# gán sự kiện click vào treeview
tree.bind("<ButtonRelease-1>",open_browser)

windown.title('Web app truyen')





windown.mainloop()

'''
    Task
        fix mở browser
        lấy danh sách link từ file txt
            - thêm sử xóa file text
        

'''