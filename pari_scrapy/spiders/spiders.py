from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import HtmlXPathSelector
from scrapy.item import Item
from scrapy.contrib.loader import XPathItemLoader

from pari_scrapy.items import Article


class ArticleSpider(CrawlSpider):
    name = "article"
    allowed_domains = ["thehindu.com"]
    start_urls = [
        "http://www.thehindu.com/opinion/columns/sainath/",
    ]

    rules = (
        Rule(SgmlLinkExtractor(allow=('sainath', ), deny=('.*\.ece', ))),
        Rule(SgmlLinkExtractor(allow=('sainath/.*\.ece', )), callback='parse_articles'),
    )

    def parse_articles(self, response):
        hxs = HtmlXPathSelector(response)

        l = XPathItemLoader(item=Article(), response=response)
        l.add_xpath("title", "//h1[contains(@class,'detail-title')]/text()")
        l.add_xpath("content", "//div[contains(@class,'article-text')]//p[contains(@class,'body')]")
        l.add_xpath("date", "//span[contains(@class,'dateline')]/text()")
        l.add_xpath("location", "//span[contains(@class,'dateline')]/span/text()")
        l.add_value("link", response.url)
        return l.load_item()    
