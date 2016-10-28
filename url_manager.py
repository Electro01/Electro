# -*- coding: utf-8 -*
class UrlManager(object):
    # url 管理器需要维护待爬取的 url 列表 和 已爬取的 url 列表
    def __init__(self):  # 初始化
        self.new_urls = set()  # 待爬取的url列表
        self.old_urls = set()  # 已爬取的url列表

    def add_new_url(self, url):  # 向URL管理器中添加一个新的URL
        if url is None:
            return
        if url not in self.new_urls and url not in self.old_urls :
            self.new_urls.add(url)  # 全新的url，可以用来再爬取

    def add_new_urls(self, urls):  # 向URL管理器中批量添加新的URL

        if urls is None or len(urls) == 0:
            return
        for url in urls:
            self.add_new_url(url)  # 调用单条添加方法

    def has_new_url(self):  # 判断URL管理器中是否有新的待爬取的URL
        return len(self.new_urls) != 0  # 长度不为0，有待爬取的url

    def get_new_url(self):  # 从URL管理器中获取一个新的带爬取的URL
        new_url=self.new_urls.pop()  # pop这个方法返回一个URL（从列表中获取一个url）并从中移除这条URL
        self.old_urls.add(new_url)  # 添加到 self.old_urls中
        return new_url  # 将这个url访问
