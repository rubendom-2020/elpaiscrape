import requests
import lxml.html as html

XPATH_LINK_TO_ARTICLE = //*[@id="fusion-app"]/div[5]/div[2]/div[1]/div[2]/article[2]/h2/a/text()
XPATH_TITLE = //h1[@class="a_t | font_secondary color_gray_ultra_dark"]/text()
XPATH_SUMMARY = //*[@id="article_header"]/h2/text()
XPATH_BODY = //div[@class="a_b article_body | color_gray_dark"]/p/text()