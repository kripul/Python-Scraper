# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class PstoreItem(scrapy.Item):
    title = scrapy.Field()
    penjual = scrapy.Field()
    url = scrapy.Field()
    images = scrapy.Field()
    desc = scrapy.Field()
    rating = scrapy.Field()
    # define the fields for your item here like:
    # name = scrapy.Field()
    # pass
