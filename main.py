from download_bot.scraper import *
from download_bot.download import *


if __name__ == '__main__':
    search(input('Enter Movie Name: ').strip().lower())
    url = get_link_to_fast_server(input('\n\nDownload Link in 480p/720p/1080p: ').strip())
    print(url); print()
    load_page(url)
    click_start_verification_btn()
    click_verification_btn()
    click_continue_btn()
    click_goto_download_btn()
    click_direct_download_btns()
    click_download_btn()


