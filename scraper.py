import requests
import lxml.html as html

HOME_URL = 'https://www.elpais.com/'

XPATH_LINK_TO_ARTICLE = '//*[@id="fusion-app"]/div[5]/div[2]/div[1]/div[2]/article[2]/h2/a/text()'
XPATH_TITLE = '//h1[@class="a_t | font_secondary color_gray_ultra_dark"]/text()'
XPATH_SUMMARY = '//*[@id="article_header"]/h2/text()'
XPATH_BODY = '//div[@class="a_b article_body | color_gray_dark"]/p/text()'

def parse_home ():
    try:
        response = requests.get(HOME_URL)
        if response.status_code == 200:
            home = response.content.decode('utf-8')
            parsed = html.fromstring(home)
            links_to_notices = parsed.xpath(XPATH_LINK_TO_ARTICLE)
            print(links_to_notices)
        else:
            raise ValueError(f 'Error: {response.status_code}')
    except ValueError as ve:
        print (ve)

def run():
    parse_home()

if __name__=='__name__':
    run()

