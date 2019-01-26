import scrapy


class FlipkartSpider(scrapy.Spider):
    name = 'Flipkart'
    allowed_domains = ['www.flipkart.com']
    start_urls = ['http://www.flipkart.com/']

    def parse(self, response):
        #return scrapy.FormRequest.from_response(response,formcss='form[action="/search"]',formdata={'q':'Half girlfriend','as':'on','as-show':'on','otracker':'AS_Query_HistoryAutoSuggest_0_2','otracker1':'AS_Query_HistoryAutoSuggest_0_2','as-pos':'0','as-type':'HISTORY'},callback=self.after_login)
        return scrapy.FormRequest.from_response(response,formcss='form[action="/search"]',formdata={'q':format(self.term)},callback=self.after_login)

    def after_login(self, response):
        content = response.xpath("/html/body/div[1]/div/div[1]/div[2]/div/div[1]/div[2]/div[2]/div/div[1]/div/a[3]/div/div[1]/text()").extract_first()
        link = response.xpath("/html/body/div[1]/div/div[1]/div[2]/div/div[1]/div[2]/div[2]/div/div[1]/div/a[3]").css('a[target="_blank"]::attr(href)').extract_first()
        link = "http://www.flipkart.com"+link
        #print content[1:]
        #review = response.xpath("/html/body/div[1]/div/div[1]/div[2]/div/div[1]/div[2]/div[2]/div/div[1]/div/div[2]/span[1]/div/text()").extract_first()
      	#print review[0:3]
        #print data
      	open("FLIPKART.txt","w").write(content[1:]+"\n"+link)
