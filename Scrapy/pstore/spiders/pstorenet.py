import scrapy
import re
from pstore.items import PstoreItem


class PstorenetSpider(scrapy.Spider):
    name = 'pstorenet'
    allowed_domains = ['p-store.net']
    start_urls = ["https://p-store.net/categories/akun?page=1"]

    page = range(20)
    for i in page:
        start_urls.append("https://p-store.net/categories/akun?page="+str(i)+"")

    def parse(self, response):
        for href in response.xpath("//*[@class='col-md-12 cusongsblock ']/*/a/@href").extract():
            yield scrapy.Request(href, callback=self.parse_content)

    def parse_content(self, response):
        item = PstoreItem()

        item['title']= response.xpath('//*[h1]/*/text()').extract_first()
        item['penjual']= response.xpath('//*[@class="user-info"]/h3/a/text()').extract()
        item['url']= response.request.url
        item['images']= response.xpath('//*[@class="carousel2Image"]/img/@src').extract()
        item['desc']= response.xpath('//*[@class="gig-description"]/p/text()').getall()
        item['rating']= response.xpath('//*[@class="rating-positive"]/text()').get()
        yield item
        # pass
