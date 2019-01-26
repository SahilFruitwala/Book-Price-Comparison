# -*- coding: utf-8 -*-
import scrapy
class AmazonSpider(scrapy.Spider):
    name = 'Amazon'
    allowed_domains = ['www.amazon.in']
    start_urls = ['http://www.amazon.in/']
    user_agent = 'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)'
    download_delay = 0.25
    def parse(self, response):
        return scrapy.FormRequest.from_response(response,formname = "site-search",formdata={'field-keywords':format(self.term)},callback=self.after_login)
    
    def after_login(self,response):
        content = response.css('li[id="result_0"]')
        text1 = content.css('div[class="a-row"]')
        text2 = text1.xpath('div[1]/div[1]/a[1]')
        price = content.css('span[class="a-size-base a-color-price s-price a-text-bold"]::text').extract_first()
        image =  text1.css('img::attr(src)').extract_first()
        link = text1.css('a[class="a-link-normal a-text-normal"]::attr(href)').extract_first()
        open("AMAZON.txt","w").write(link+"\n"+image+"\n"+price)
        #return scrapy.Request(link,callback=self.after_select) 

    #def after_select(self,response):
		#content =  response.css('div[id="reviewSummary"]')
		#text1 = content.xpath('div[2]/span/text()').extract()
		#open("../../AMAZON.txt","a").write(text1)
		
    	#text1 = []
    	#for i in range(0,9):
    		#xp = 'li['+str(i)+']/text()'
    		#a = content.xpath(xp).extract()
    		#if i == 8:
    			#a = str(a[0]).strip("\n  ")
    			#break
    		#text1 = text1 + a
    	#detail = "\n".join(text1)+"\n"+a
    	#open("../../DETAIL.txt","w").write(detail)
		
		

