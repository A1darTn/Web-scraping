from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By




def contains_keywords(text: str, keywords: list):
    return any(keyword.lower() in text.lower() for keyword in keywords)


def wait_element(browser, delay=3, by=By.TAG_NAME, value=None):
    try:
        return WebDriverWait(browser, delay).until(
            expected_conditions.presence_of_element_located((by, value))
        )
    except TimeoutException:
        return None
    

def get_article_links(driver, keywords_list):
    posts = driver.find_elements(by=By.CSS_SELECTOR, value='div.tm-article-snippet')
    articles = []
    for post in posts:
        article = wait_element(browser=post, by=By.CSS_SELECTOR, value='a.tm-title__link').get_attribute('href')
        articles.append(article)
    result = []
    for post in articles:
        driver.get(post)
        title = wait_element(browser=driver, by=By.TAG_NAME, value='h1').text
        date = wait_element(browser=driver, by=By.TAG_NAME, value='time').get_attribute('datetime')
        text_article = wait_element(browser=driver, by=By.TAG_NAME, value='p').text
        if contains_keywords(text_article, keywords_list) or contains_keywords(title, keywords_list):
            result.append((date, title, post))
    return result