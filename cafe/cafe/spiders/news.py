import scrapy
from datetime import date
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor



class NewsSpider(scrapy.Spider):
    name = "news"
    allowed_domains = ["cafef.vn"]
    start_urls = ["https://cafef.vn/thi-truong.chn",
                  "https://cafef.vn/xa-hoi.chn",
                  "https://cafef.vn/doanh-nghiep.chn",
                  "https://cafef.vn/vi-mo-dau-tu.chn",
                  "https://cafef.vn/thi-truong-chung-khoan.chn",
                  "https://cafef.vn/tai-chinh-ngan-hang.chn",
                  "https://cafef.vn/tai-chinh-quoc-te.chn",
                  "https://cafef.vn/bat-dong-san.chn",
                  "https://cafef.vn/song.chn",
                  "https://cafef.vn/lifestyle.chn",
                  ]
    # rules = (
    #     # Extract and follow all links!
    #     Rule(LinkExtractor(callback='parse_item'), follow=True),
    # )

    def parse(self, response):
        tag = response.css("h1.zone-title a::text").get()
        today = date.today().strftime("%Y-%m-%d")
        
        for item in response.css("div.tlitem-flex"):
            link = "https://cafe.vn" + item.css("a::attr(href)").get()
            title = item.css("a::attr(title)").get()
            time = item.css("div.knswli-right span::attr(title)").get()
            if time.startswith(today):
                yield {
                    "link": link,   
                    "title": title,
                    "tag": tag,
                    "time": time,
                }