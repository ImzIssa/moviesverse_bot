import os
import sys
import requests as rq
from bs4 import BeautifulSoup


headers = {
'cache-control': 'max-age=0',
'cookie': 'cf_clearance=NeaOVL65Fex72OaU7oAr64nWo9aD45UrkX3pOOIL7Ns-1649507960-0-150; _ga=GA1.1.1514307650.1649512441; _ga_VT1Q5BGXF9=GS1.1.1649512441.1.1.1649512806.0',
'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36'
}


def search():
    while True:
        movie_name = input('Enter Movie Name: ').strip().lower()
        movie_name =  "+".join(str(movie_name).strip().lower().split())
        url = f'https://moviesverse.club/?s={movie_name}'
        res = rq.get(url, headers=headers)

        if(res.status_code == 200):
            soup = BeautifulSoup(res.text, 'html.parser')
            results = soup.find('div', {'id': 'content_box'})
            print(results.h1.text)
            print()
        
        if (results.div['class'] == ['no-results']):
            print('Movie is Unavailable. Try Different Movie or checking Spelling.\n')
        else:
            for article in results.find_all('article'):
                if "[HQ Fan Dub]" in article.header.text.strip():
                    continue
                print(article.header.h2.a['title']) 
                # movie_link = article.a['href'] 
                # movie_img = article.img['src']
                print(f"Movie Link: {article.a['href']}")
                print(f"Image Link: {article.img['src']}")
                print(); print("-" * 120)
            break

    # get_links_to_archives(input("\nEnter Movie Link of Prefered Movie: "))
        
def get_links_to_archives(url):
    pxls_url = {}
    pxls_dic = {}
    pxls_list = ['480p', '720p', '1080p'] 
    i = 0
    for pxl in pxls_list:
        if pxl in url:
            pxls_dic[i] = pxl
            i += 1

    res = rq.get(url, headers=headers)
    if(res.status_code == 200):
        soup = BeautifulSoup(res.text, 'html.parser')
        archive_download_links = soup.find_all('a', {'class': 'maxbutton'})
        print('\nDownload Links')
        if (len(pxls_dic) == len(archive_download_links)):
            for idx, link in enumerate(archive_download_links):
                print(f'{pxls_dic[idx]} : {link["href"]}')
                pxls_url[pxls_dic[idx]] = link['href']
        else:
            i = 0
            for link in archive_download_links:
                print(f'{pxls_list[i]} : {link["href"]}')
                pxls_url[pxls_list[i]] = link['href']
                i += 1
                if i==3: i=0

    return select_quality(pxls_url)

def select_quality(pxl_url_dic):
    print()
    url = " "
    pxls = ""
    string = "Download in "
    for key in pxl_url_dic.keys():
        string += key + " || "
        pxls += key+" || "

    while True:
        res = input(f'\n{string[:-3]} (Link or Quality): ').strip()
        if res[0].isdigit() and (int(res[:3]) and len(res) >= 3):
            try:
                pxl = str(res)+"p"
                print(pxl_url_dic[pxl])
                url = get_link_to_fast_server(pxl_url_dic[pxl])
                break
            except KeyError:
                print(f'{res} is an invalid movie quality\nor movie is unavailable in desired quality')
                print(f'Try {pxls[:-3]}')
        else:
            print(res)
            url = get_link_to_fast_server(res)
            break
    
    return url


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




