import requests
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import Chrome, ChromeOptions, Keys
from selenium.webdriver.chrome.service import Service
from functions import wait_element, contains_keywords, get_article_links
from time import sleep




def main():
    KEYWORDS = ['дизайн', 'фото', 'web', 'python']

    chrome_path = ChromeDriverManager().install()
    service = Service(executable_path=chrome_path)
    browser = Chrome(service=service)

    browser.get('https://habr.com/ru/articles/')
    sleep(1)
    print('Программа запущена.')
    info = get_article_links(browser, KEYWORDS)
    if info:
        for date, title, post in info:
            print(f'{date} - {title} - {post}')
    else:
        print('Нет статей, соответствующих заданным ключевым словам.')
    print('Программа завершена.')


if __name__ == '__main__':
    main()