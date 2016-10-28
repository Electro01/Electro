# -*- coding: utf-8 -*

from bs4 import BeautifulSoup
import re
import urllib.parse

class HtmlParser(object):
    # 获取页面中所有词条的url
    def _get_new_urls(self, page_url, soup):
        new_urls = set()  # 将结果存到列表中
        #  /view/123.htm
        links = soup.find_all('a', href=re.compile(r"/view/\d+\.htm"))  # 不是html
        for link in links:
            new_url = link['href']
            new_full_url = urllib.parse.urljoin(page_url, new_url)   # 自动将两个url添加成完整的url(让 new_url 以 page_url 为模板拼接成一个全新的 url)
            new_urls.add(new_full_url)
        return new_urls

    # 获取数据
    def _get_new_data(self, page_url, soup):
        res_data = {}  # 存放数据

        #url
        res_data['url'] = page_url
        #  <dd class="lemmaWgt-lemmaTitle-title"><h1>Python</h1>
        title_node = soup.find('dd', class_="lemmaWgt-lemmaTitle-title").find("h1")  # 如果没找到 'lemmaWgt-lemmaTitle-title' 类，直接跳过
        res_data['title'] = title_node.get_text()

        # <div class="lemma-summary">
        summary_node = soup.find('div', class_="lemma-summary")
        res_data['summary'] = summary_node.get_text()

        return res_data

    def parse(self, page_url, html_cont):
        if page_url is None or html_cont is None:
            return

        soup = BeautifulSoup(html_cont, 'html.parser', from_encoding='utf-8')
        new_urls = self._get_new_urls(page_url, soup)
        new_data = self._get_new_data(page_url, soup)
        return new_urls, new_data

# python3对urllib和urllib2进行了重构，
# 拆分成了urllib.request, urllib.response, urllib.parse, urllib.error等几个子模块，
# urljoin现在对应的函数是urllib.parse.urljoin
