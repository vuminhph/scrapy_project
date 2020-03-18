

import scrapy




class NewsTitle(scrapy.Item):

    link = scrapy.Field()

    name = scrapy.Field()

    data_id= scrapy.Field()

class News(scrapy.Item):

    link = scrapy.Field()

    name = scrapy.Field()
    author = scrapy.Field()

class QuoteItem(scrapy.Item):

    author=scrapy.Field()
    picture = scrapy.Field()
    total = scrapy.Field()
    quote=scrapy.Field()
