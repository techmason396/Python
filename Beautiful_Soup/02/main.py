from bs4 import BeautifulSoup
import requests

'''
    sử dụng thư viện requests để lấy nội dung trang web
    requests.get(url): truy cập vào trang web để lấy nội dung dựa vào url

    .text: lấy nội dung từ resquest.get(url)
'''
response = requests.get('https://www.nettruyenus.com/truyen-tranh/hiep-khach-giang-ho-44050')
content = response.text

soup = BeautifulSoup(content, 'html.parser')
print(soup)

