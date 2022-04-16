from download_bot.scraper import *
from download_bot.download import *


if __name__ == '__main__':
    search()
    url = get_links_to_archives(input("\nEnter Movie Link of Prefered Movie: "))
    print(f"\n{url}")
    load_page(url)
    click_start_verification_btn()
    click_verification_btn()
    click_continue_btn()
    click_goto_download_btn()
    click_direct_download_btns()
    click_download_btn()


