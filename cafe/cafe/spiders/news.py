import scrapy
from datetime import date
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor



class NewsSpider(CrawlSpider):
    name = "news"
    allowed_domains = ["cafef.vn"]
    start_urls = ["https://cafef.vn"]
    # rules = (
    #     # Extract and follow all links!
    #     Rule(LinkExtractor(callback='parse_item'), follow=True),
    # )

    def parse(self, response):
        # Extracting data from the response
        for item in response.css("listchungkhoannew"):
            yield {
                "title": item.css("knswli-right.h3.a.title::text").get(),
                "type": item.css("time_cate.p.title::text").get(),
                # "tags": item.css("div.tags a.tag::text").getall(),
            }