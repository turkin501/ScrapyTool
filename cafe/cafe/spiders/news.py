import scrapy
from datetime import date
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor



class NewsSpider(scrapy.Spider):
    name = "news"
    allowed_domains = ["cafef.vn"]
    start_urls = ["https://cafef.vn"]
    # rules = (
    #     # Extract and follow all links!
    #     Rule(LinkExtractor(callback='parse_item'), follow=True),
    # )

    def parse(self, response):
        # Extracting data from the response
        for item in response.css("div.knswli-right"):
            link = "https://cafe.vn" + item.css("h3 a::attr(href)").get()
            title = item.css("h3 a::text").get()
            tag = item.css("p.time_cate a::text").get()
            time = item.css("p.time_cate span::attr(title)").get()
            yield {
                "link": link,   
                "title": title,
                "tag": tag,
                "time": time,
            }