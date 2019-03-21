import scrapy

class BrickSetSpider(scrapy.Spider):
    name = "brickset_spider"
    start_urls = ['https://hust.edu.vn/']

    def parse(self, response):
        SET_SELECTOR = '#menu' 
        for brickset in response.css(SET_SELECTOR):

            NAME_SELECTOR = 'li ::text' 
            yield {
                'name': brickset.css(NAME_SELECTOR).extract(),
            }

# . class
# # id
# 

