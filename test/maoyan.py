import requests
from bs4 import BeautifulSoup as bs
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.112 Safari/537.36',
    "Host":"maoyan.com",
    "Referer":"http://maoyan.com/board/4?offset=10"
}
def get_title(url):
    res = requests.get(url,headers=headers)
    soup = bs(res.text,'lxml')
    movies = soup.select('.movie-item-info p a')
    for movie in movies:
        print(movie.text)
base_url = 'http://maoyan.com/board/4?offset={}'
new_urls = []
for i in range(0,11):
    new_url = base_url.format(i*10)
    new_urls.append(new_url)
    get_title(new_url)