from tkinter import *

'''
    tkinter.Tk() : tạo một giao diện
    .mainloop(): giữ cho giao diện hoạt động
    .title(str): tiêu đề cho cửa sổ 

    .minsize(): thiết lập độ rộng tối thiểu cho windown
        - các tham số:
            + width: chiều ngang
            + height: chiều cao

    Label(): thiết lập nhãn
        - các tham số
            + text: nội dung hiển thị
            + font: thiết lập liểu chữ 
        - thay đổi nội dung label
            label['text'] = "str"
            .config(text="str")

    Button(): thiết lập nút bấm
        - các tham số
            + text: nội dung hiển thị button
            + command: tên hàm mà nút thực hiện
    
    Entry(): nơi nhập dữ liệu
        - các tham số:
            + width: thiết lập chiều rộng ô nhập liệu
        .get(): trả về string nội dung nhập vào
        .insert(): chèn nội dung có sẵn trên input
            END
            string: nội dung text
    
    Text(): kiểu như text area
        - các tham số:
            + width, height: thiết lập dt textarea
        .focus(): focus vào text area
        .insert(): chèn nội dung mặc định
        .get(): lấy nội dung text area
            "1.0": lấy nội dung ở vị trí đầu tiên của văn bản (hàng 1 cột 0)            
            END : đại diện vị trí cuối cùng văn bản
    
    Spinbox()
        - các tham số
            + from_ : giá trị bắt đầu
            + to : giá trị kết thúc
            + width: chiều rộng
            + command: function 
        .get(): lấy giá trị spinbox

    Checkbutton(): kiểu như check box
        - các tham số:
            + text : label cho checkbox
            + variable: lấy giá trị từ biến ( sử dụng biến tạo tạo từ IntVar)
            + command: function hoạt động
        .get(): lấy giá trị checkbutton

    Radiobutton()
        - các tham số:
            + text: label cho radio
            + value: giá trị cho  radiobutton
            + variable: giá trị biến trạng thái sử dụng
            + command: function gọi tới
        .get(): lấy giá trị radionbutton

    Listbox()
        các tham số:
            + height: chiều cao của list box
        .get(): lấy giá trị của list box
        .curselection(): lấy giá trị click chọn hiện tại
        .bind(tên sự kiện, function sự kiện): gắn sự kiện 
'''
window = Tk()
window.title("Widget Examples")
window.minsize(width=300, height=500)

# label
my_label = Label(text="This is new Text", font=('Arial',15,"bold"))
my_label.pack()

# Button
def button_clicked():
    my_label.config(text="Hello Trung", highlightcolor="red")

def button_get():
    content = input.get()
    my_label.config(text=content)

button = Button(text='Click me', command=button_clicked)
button.pack()

# button_get = Button(text="lay du lieu", command=button_get)
# button_get.pack()

# Entry
input = Entry(width=30)
input.insert(END, string="Input some text here...")
input.pack()

# Text
text = Text(height=5, width=30)
text.focus()
text.insert(END, "Nhap noi dung vao day")
print(text.get("1.0",END))
text.pack()

# Spinbox
def get_spinbox():
    print(spinbox.get())

spinbox = Spinbox(from_=0, to=10, width=5, command=get_spinbox)
spinbox.pack()

# check box
def checkbutton_userd():
    print(check_state.get())

check_state = IntVar()
check_button = Checkbutton(text="Is on?",variable=check_state, command=checkbutton_userd)
check_button.pack()

# radio button
def radio_used():
    print(radio_state.get())

radio_state = IntVar()
radio_button_1 = Radiobutton(text="Option1", value=1, variable=radio_state, command=radio_used)
radio_button_2 = Radiobutton(text="Option2", value=2, variable=radio_state, command=radio_used)
radio_button_1.pack()
radio_button_2.pack()

# listbox
def listbox_used(event):
    print(listbox.get(listbox.curselection()))

listbox = Listbox(height=5)
fruits = ["Apple","Pear","Orange","Banana","Potato"]

for fruit in fruits:
    listbox.insert(fruits.index(fruit), fruit)

listbox.bind("<<ListboxSelect>>",listbox_used)
listbox.pack()


window.mainloop()