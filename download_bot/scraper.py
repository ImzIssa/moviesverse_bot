import os
import requests as rq
from bs4 import BeautifulSoup


headers = {
'cache-control': 'max-age=0',
'cookie': 'cf_clearance=NeaOVL65Fex72OaU7oAr64nWo9aD45UrkX3pOOIL7Ns-1649507960-0-150; _ga=GA1.1.1514307650.1649512441; _ga_VT1Q5BGXF9=GS1.1.1649512441.1.1.1649512806.0',
'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36'
}


def search(movie_name):
    movie_name =  "+".join(str(movie_name).strip().lower().split())
    url = f'https://moviesverse.club/?s={movie_name}'
    res = rq.get(url, headers=headers)

    if(res.status_code == 200):
        soup = BeautifulSoup(res.text, 'html.parser')
        results = soup.find('div', {'id': 'content_box'})
        print(results.h1.text)
        print()

        for article in results.find_all('article'): 
            movie_link = article.a['href'] 
            movie_img = article.img['src']
            print(f'Movie Link: {movie_link}')
            print(f'Image Link: {movie_img}')
            get_links_to_archives(movie_link)
        

def get_links_to_archives(url):
    pxls = {0:'480p', 1:'720p', 2:'1080p'}
    res = rq.get(url, headers=headers)
    if(res.status_code == 200):
        soup = BeautifulSoup(res.text, 'html.parser')
        achive_download_links = soup.find_all('a', {'class': 'maxbutton'})
        i = 0
        print('\nDownload Links')
        for link in achive_download_links:
            print(f'{pxls[i]} : {link["href"]}')
            i += 1
            if i == 3: i = 0



def get_link_to_fast_server(url):
    res = rq.get(url, headers=headers)
    if(res.status_code == 200):
        soup = BeautifulSoup(res.text, 'html.parser')
        return soup.find('a', {'class': 'maxbutton-1 maxbutton maxbutton-fast-server-gdrive'})['href']



# def click_download_links(url):
#     res = rq.get(url, headers=headers)
#     if(res.status_code == 200):
#         soup = BeautifulSoup(res.text, 'html.parser')
#         achive_download_links = soup.find_all('a', {'class': 'maxbutcd ton'})
#         i = 0
#         for link in achive_download_links:
#             print(f'{pxls[i]} : {link["href"]}')
#             i += 1
#             if i==3: i=0




