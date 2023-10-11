from bs4 import BeautifulSoup

'''
    .title : lấy thẻ tiêu đề
    .title.name: lấy tên của thẻ
    .title.string: lấy nội dung trong thẻ title
    * các thẻ còn lại làm tương tự

    .prettify: in nội dung toàn bộ html

    .find(name='', id='', or class=''): tìm thẻ với name và id tương ứng
    .find_all(name='name tag'): lấy tất cả các thẻ có name = name tag


    .getText(): lấy nội dung bên trong thẻ
    .get('name attr'): lấy giá trị attr
        + href: lấy link
        + class: lấy tên class
        + id: lấy tên id
    
    .select_one(selector=""): chọn ra phần tử đầu tiên dựa vào bộ chọn css CSS (#id, .class, tag(a,q,li...))
'''


#simple_soup = BeautifulSoup()

with open('website.html', encoding='utf-8') as file:
    html = file.read()

soup = BeautifulSoup(html, 'html.parser')
print(soup.title)
print(soup.title.name)
print(soup.title.string)
#print(soup.prettify)

all_li_tag = soup.find_all(name="li")
for li in all_li_tag:
    print(li.getText())

all_anchor_tag = soup.find_all(name='a')

for a in all_anchor_tag:
    print(a.get('href'))

h1 = soup.find(name='h1', id='name')
print(h1)

company_url = soup.select_one(selector='p a')
print(company_url)
