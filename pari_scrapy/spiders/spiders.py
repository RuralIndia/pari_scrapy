from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import HtmlXPathSelector
from scrapy.item import Item
from scrapy.contrib.loader import XPathItemLoader

from pari_scrapy.items import Article


class ArticleSpider(CrawlSpider):
    name = "article"
    allowed_domains = ["thehindu.com", "hindu.com"]
    start_urls = [
        #base
        # "http://www.thehindu.com/opinion/columns/sainath/",

        #extra
        # "http://www.thehindu.com/opinion/op-ed/when-water-flows-like-money/",
        # "http://www.thehindu.com/todays-paper/tp-opinion/article2687760.ece",
        # "http://www.thehindu.com/opinion/op-ed/article2248021.ece",
        # "http://www.thehindu.com/opinion/op-ed/article2224641.ece",
        # "http://www.thehindu.com/todays-paper/tp-opinion/article2014092.ece",
        # "http://www.thehindu.com/opinion/op-ed/article847189.ece",
        # "http://www.thehindu.com/opinion/op-ed/article445810.ece",
        # "http://www.thehindu.com/opinion/lead/article428367.ece",
        # "http://www.thehindu.com/opinion/lead/article94324.ece",
        # "http://www.thehindu.com/news/national/article87699.ece",
        # "http://www.thehindu.com/opinion/op-ed/article33086.ece",
        # "http://www.thehindu.com/opinion/lead/article30456.ece",
        # "http://www.thehindu.com/opinion/op-ed/article19803.ece",

        # htm
        "http://www.hindu.com/2009/07/18/stories/2009071853850900.htm",
        "http://www.hindu.com/2009/07/11/stories/2009071152590900.htm"
        "http://www.hindu.com/2009/07/10/stories/2009071054870900.htm",
        "http://www.hindu.com/2009/07/04/stories/2009070455931100.htm",
        "http://www.hindu.com/2009/04/20/stories/2009042051620800.htm",
        "http://www.hindu.com/2009/04/13/stories/2009041355450800.htm",
        "http://www.hindu.com/2009/04/03/stories/2009040355480800.htm",
        "http://www.hindu.com/2008/12/12/stories/2008121250090100.htm",
        "http://www.hindu.com/2008/06/24/stories/2008062454690900.htm",
        "http://www.hindu.com/2008/06/23/stories/2008062355111100.htm"
    ]

    rules = (
        # Rule(SgmlLinkExtractor(allow=('sainath', ), deny=('.*\.ece', ))),
        # Rule(SgmlLinkExtractor(allow=('sainath/.*\.ece', )), callback='parse_articles'),
        # Rule(SgmlLinkExtractor(allow=('.*\.ece$', )), callback='parse_extra'),
        Rule(SgmlLinkExtractor(allow=('.*\.htm$', ), deny=('.*05hdline.htm$', )), callback='parse_htm'),
    )

    def parse_htm(self, response):
        if "P. Sainath" in response.body:
            hxs = HtmlXPathSelector(response)
            l = XPathItemLoader(item=Article(), response=response)

            l.add_xpath("title", "//p/font[contains(@class,'storyhead')]/b/text()")
            l.add_xpath("content", "//comment()[.=' story begins ']/following::p/text()")
            l.add_xpath("date", "//meta[@name='PublicationDate']/@content")
            l.add_value("location", "")
            l.add_value("link", response.url)
            l.add_value("author", 'Sainath')

            return l.load_item()

    def parse_extra(self, response):
        if "P. Sainath" in response.body:
            return self.parse_articles(response)

    def parse_articles(self, response):
        hxs = HtmlXPathSelector(response)

        l = XPathItemLoader(item=Article(), response=response)
        l.add_xpath("title", "//h1[contains(@class,'detail-title')]/text()")
        l.add_xpath("content", "//div[contains(@class,'article-text')]//p[contains(@class,'body')]")
        l.add_xpath("date", "//span[contains(@class,'dateline')]/text()")
        l.add_xpath("location", "//span[contains(@class,'dateline')]/span/text()")
        l.add_xpath("keywords", "//div[@id='articleKeywords']/p/a/text()")
        l.add_value("link", response.url)
        l.add_value("author", 'Sainath')
        return l.load_item()
