# -*- coding: utf-8 -*
from Baike_Spider import url_manager, html_downloader, html_parser,\
    html_outputer                  # 创建各个class并引入
class SpiderMain():
    def __init__(self):  # 初始化各个对象( 爬虫总调度程序会使用 url 管理器、 html 的下载器、解析器、输出器)
        self.urls=url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_outputer.HtmlOutputer()

    def craw(self, root_url):  # craw 方法，爬虫调度程序
        count = 1  # 记录当前爬取的是第几个url
        self.urls.add_new_url(root_url)  # 将入口url添加进管理器（添加单个url）
        while self.urls.has_new_url():  # 如果有待爬取的url，启动爬虫循环
            try:  # 异常处理
                new_url = self.urls.get_new_url()  # 获取一个待爬取的url（当前爬取好的url）
                print('craw %d:%s' % (count, new_url))  # 打印传入的第几个 url
                html_cont = self.downloader.download(new_url) # 启动下载器下载页面并保存；下载好页面调用解析器来解析数据
                new_urls, new_data = self.parser.parse(new_url, html_cont) # 得到新的url列表以及数据
                self.urls.add_new_urls(new_urls)  # url添加进url管理器（添加批量url）
                self.outputer.collect_data(new_data)   # 收集数据
                if count == 1000:
                    break
                count +=1
            except Exception as error:
                print('craw failed:', error) # 标记失败

        self.outputer.output_html()  # 输出收集好的数据
    pass



if __name__ == "__main__":
    root_url = "http://baike.baidu.com/view/21087.htm"  # 入口url（以一个入口的接口来爬取整个url页面）
    obj_spider=SpiderMain()
    obj_spider.craw(root_url)   # 启动爬虫

