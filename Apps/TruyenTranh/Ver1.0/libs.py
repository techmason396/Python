# chứa các funtion xử lý 

from bs4 import BeautifulSoup
import requests

import webbrowser



# nettruyenco.vn 
class Nettruyenco:
    data = []
    urls = []
    def __init__(self,_urls) -> None:
        self.urls = _urls

    '''
        lấy chapter truyện hiện tại
    '''
    def get_current_chapter(self,url):
        response = requests.get(url)
        content = response.text
        soup = BeautifulSoup(content, 'html.parser')
        chapter = soup.select_one(selector='.chapter').text
        name = soup.select_one(selector='.title-detail').text
        link = soup.select_one(selector='.chapter a').get('href')
        update = soup.select_one(selector='div.col-xs-4.no-wrap.small.text-center').text
        return {
            'Name': name,
            'Chapter': chapter,
            'Link': link,
            'Update': update
        }

    def get_data_chapter_from_list_url(self):
        for url in self.urls:
            url_data = self.get_current_chapter(url)            
            self.data.append(url_data)
