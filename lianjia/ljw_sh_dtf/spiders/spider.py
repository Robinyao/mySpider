# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.selector import Selector
from scrapy.http import Request
from ljw_sh_dtf.items import LjwShDtfItem

class Spider(CrawlSpider):
    '''上海链家网-地铁租房'''
    name = "zufang"
    allowed_urls = ['http://sh.lianjia.com/']
    start_urls = []
    for i in range(1, 100):
        start_urls.append('http://sh.lianjia.com/ditiezufang/d%d' % i)
    global urls
    urls = []
    rules = [
        Rule(LinkExtractor(allow=('lianjian.com'),
             restrict_xpaths=('//div[@class="page-box house-lst-page-box"]/a[last()]')),
             follow=True,
             callback='parse_item')
    ]

    def parse_start_url(self, response):
        return self.parse_item(response)

    def parse_item(self, response):
        sel = Selector(response)
        lists = sel.xpath('//*[@id="house-lst"]/li/div[@class="info-panel"]/h2/a/@href')

        # 拼接房屋链接地址
        for link in lists:
            urls.append("http://sh.lianjia.com" + link.extract())

        for url in urls:
            yield Request(url, callback=self.parse_item2)

    def parse_item2(self, response):

        sel2 = Selector(response)
        # 抓取信息
        item = LjwShDtfItem()
        # link_url = sel2.xpath('//div[@class="houseRecord"]/span[@class="houseNum"]').extract()
        link_url = response.xpath('//div[@class="houseRecord"]/span[@class="houseNum"]').re(r'shz(\d+)')
        title = sel2.xpath('//div[@class="title"]/h1/text()').extract()
        price = sel2.xpath('//div[@class="houseInfo"]/div[@class="price"]/div/text()').extract()
        rooms = sel2.xpath('//div[@class="houseInfo"]/div[@class="room"]//*/text()').extract()
        square = sel2.xpath('//div[@class="houseInfo"]/div[@class="area"]//*/text()').extract()
        floor = sel2.xpath('//table[@class="aroundInfo"]//tr[1]/td[2]/text()').extract()
        face = sel2.xpath('//table[@class="aroundInfo"]//tr[1]/td[4]/text()').extract()
        area = sel2.xpath('//table[@class="aroundInfo"]//tr[2]/td[2]/text()').extract()
        uptime = sel2.xpath('//table[@class="aroundInfo"]//tr[2]/td[4]/text()').extract()
        community = sel2.xpath('//table[@class="aroundInfo"]//tr[3]/td/p//text()').extract()
        address = sel2.xpath('//table[@class="aroundInfo"]//tr[4]/td/p/text()').extract()

        item['link_url'] = ''
        for lu in link_url:
            item['link_url'] += lu.strip()
            item['link_url'].encode('utf-8').strip()
        item['title'] = ''
        for t in title:
            item['title'] += t.strip()
            item['title'].encode('utf-8').strip()
        item['price'] = ''
        for p in price:
            item['price'] += p.strip()
            item['price'].encode('utf-8').strip()
        item['rooms'] = ''
        for r in rooms:
            item['rooms'] += r.strip()
            item['rooms'].encode('utf-8').strip()
        item['square'] = ''
        for s in square:
            item['square'] += s.strip()
            item['square'].encode('utf-8').strip()
        item['floor'] = ''
        for fl in floor:
            item['floor'] += fl.strip()
            item['floor'].encode('utf-8').strip()
        item['face'] = ''
        for fa in face:
            item['face'] += fa.strip()
            item['face'].encode('utf-8').strip()
        item['area'] = ''
        for ar in area:
            item['area'] += ar.strip()
            item['area'].encode('utf-8').strip()
        item['uptime'] = ''
        for u in uptime:
            item['uptime'] += u.strip()
            item['uptime'].encode('utf-8').strip()
        item['address'] = ''
        for ad in address:
            item['address'] += ad.strip()
            item['address'].encode('utf-8').strip()
        item['community'] = ''
        for c in community:
            item['community'] += c.strip()
            item['community'].encode('utf-8').strip()

        return item
