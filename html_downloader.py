# -*- coding: utf-8 -*

import urllib.request

class HtmlDownloader(object):  # 下载网页内容

     def download(self,url):
         if url is None:
            return None

         response = urllib.request.urlopen(url)  # 请求url内容

         if response.getcode() != 200:  # 判断是否请求成功
            return None

         return response.read()  # 返回下载好的内容
         # response = response.decode('utf-8')

