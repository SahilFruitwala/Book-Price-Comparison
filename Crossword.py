# -*- coding: utf-8 -*-
import scrapy
class CrosswordSpider(scrapy.Spider):
    name = 'Crossword'
    allowed_domains = ['www.crossword.in']
    start_urls = ['http://www.crossword.in/']

    def parse(self, response):
        return scrapy.FormRequest.from_response(response,formcss='form[action="/search"]',formdata={'q':format(self.term)},callback=self.after_search)

    def after_search(self, response):
        content = response.css('div[class="variant-image"]')
        text1 = content.css('div[class="variant-image"]')
        text2 = text1.css('a::attr(href)')
        url = response.urljoin(text2.extract_first())
        yield scrapy.Request(url,callback=self.after_select)

    
    def after_select(self, response) :
        # text1 = content.css('div[class="our_price"]').extract_first()
        content1 = response.css('div[class="our_price"]')
        text1 = content1.css('span[class="m-w"]::text').extract_first()
        data=text1+"\n"+response.url
        open("CROSSWORD.txt","w").write(data)

