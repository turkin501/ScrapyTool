import scrapy
from datetime import date
from scrapy.contrib.spiders import CrawlSpider, Rule


class NewsSpider(CrawlSpider):
    name = "news"
    allowed_domains = ["cafef.vn"]
    start_urls = ["https://cafef.vn"]
    rules = (
        # Extract and follow all links!
        Rule(LinkExtractor(callback='parse_item'), follow=True),
    )

    def parse(self, response):
        # Extracting data from the response
        title = response.css('h3.news-title a::text').get()
        author = response.css('div.news-publish p:first-child::text').get()

        # Yielding the extracted data
        yield {
            'Title': title,
            'Author': author
        }