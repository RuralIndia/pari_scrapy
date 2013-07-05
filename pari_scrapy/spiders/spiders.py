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
        # "http://www.hindu.com/2008/06/24/stories/2008062454690900.htm",
        # "http://www.hindu.com/2008/06/23/stories/2008062355111100.htm",
        # "http://www.hindu.com/2008/06/16/stories/2008061655371000.htm",
        # "http://www.hindu.com/2008/06/12/stories/2008061254521000.htm",
        # "http://www.hindu.com/2008/06/03/stories/2008060354790900.htm",
        # "http://www.hindu.com/2008/06/02/stories/2008060255151100.htm",
        # "http://www.hindu.com/2008/05/31/stories/2008053154170900.htm",
        # "http://www.hindu.com/2008/05/30/stories/2008053055591100.htm",
        # "http://www.hindu.com/2008/05/26/stories/2008052654011100.htm",
        # "http://www.hindu.com/2008/05/19/stories/2008051951031000.htm",
        # "http://www.hindu.com/2008/04/21/stories/2008042155421000.htm",
        # "http://www.hindu.com/2008/04/17/stories/2008041755841000.htm",
        # "http://www.hindu.com/2008/02/02/stories/2008020255781000.htm",
        # "http://www.hinduonnet.com/2008/01/31/stories/2008013160930100.htm",
        # "http://www.hindu.com/2008/01/18/stories/2008011853351000.htm",
        # "http://www.hindu.com/2007/12/24/stories/2007122455511000.htm",
        # "http://www.hindu.com/2007/11/27/stories/2007112755141000.htm",
        # "http://www.hindu.com/2007/11/15/stories/2007111554771300.htm",
        # "http://www.hindu.com/2007/11/14/stories/2007111453091100.htm",
        # "http://www.hindu.com/2007/11/13/stories/2007111352250900.htm",
        # "http://www.hindu.com/2007/11/12/stories/2007111257790100.htm",
        # "http://www.hindu.com/2007/09/15/stories/2007091555451200.htm",
        # "http://www.hindu.com/2007/09/04/stories/2007090455350900.htm",
        # "http://www.hindu.com/2007/08/23/stories/2007082355471300.htm",
        # "http://www.hindu.com/2007/08/15/stories/2007081554621300.htm",
        # "http://www.hindu.com/2007/08/09/stories/2007080950081000.htm",
        # "http://www.hindu.com/2007/07/27/stories/2007072754131100.htm",
        # "http://www.hindu.com/2007/06/26/stories/2007062650641100.htm",
        # "http://www.hindu.com/2007/06/22/stories/2007062250091100.htm",
        # "http://www.hindu.com/2007/06/13/stories/2007061301671100.htm",
        # "http://www.hindu.com/2007/05/30/stories/2007053001681100.htm",
        # "http://www.hindu.com/2007/05/29/stories/2007052902231100.htm",
        # "http://www.hindu.com/2007/05/24/stories/2007052402321100.htm",
        # "http://www.thehindu.com/2007/05/22/stories/2007052200840900.htm",
        # "http://www.hindu.com/2007/05/21/stories/2007052103541100.htm",
        # "http://www.hindu.com/2007/05/05/stories/2007050507911100.htm",
        # "http://www.hindu.com/2007/03/29/stories/2007032904471000.htm",
        # "http://www.hindu.com/2007/01/27/stories/2007012706361100.htm",
        # "http://www.hindu.com/2007/01/25/stories/2007012503401100.htm",
        # "http://www.hindu.com/2007/01/24/stories/2007012404621300.htm",
        # "http://www.hindu.com/2007/01/23/stories/2007012303591100.htm",
        # "http://www.hindu.com/2006/12/13/stories/2006121303801000.htm",
        # "http://www.thehindu.com/2006/11/25/stories/2006112502891100.htm",
        # "http://www.thehindu.com/2006/11/23/stories/2006112305660900.htm",
        # "http://www.hindu.com/2006/11/22/stories/2006112201731100.htm",
        # "http://www.thehindu.com/2006/09/08/stories/2006090806591000.htm",
        # "http://www.frontlineonnet.com/fl2317/stories/20060908004500400.htm",
        # "http://www.hindu.com/2006/08/11/stories/2006081104361300.htm",
        # "http://www.hinduonnet.com/2006/08/08/stories/2006080806050900.htm",
        # "http://www.hindu.com/2006/07/14/stories/2006071407091000.htm",
        # "http://www.hindu.com/2006/07/04/stories/2006070403340800.htm",
        # "http://www.hindu.com/2006/06/28/stories/2006062804211000.htm",
        # "http://hindu.com/2006/06/12/stories/2006061203181000.htm",
        # "http://www.hindu.com/2006/05/29/stories/2006052904571100.htm",
        # "http://www.hindu.com/2006/05/22/stories/2006052202251100.htm",
        # "http://www.hindu.com/2006/04/25/stories/2006042505020900.htm",
        # "http://www.frontlineonnet.com/fl2307/stories/20060421005000400.htm",
        # "http://www.hindu.com/2006/03/16/stories/2006031607401100.htm",
        # "http://www.hindu.com/2006/03/22/stories/2006032205860500.htm",
        # "http://www.hindu.com/2006/02/18/stories/2006021805511100.htm",
        # "http://www.hindu.com/2006/02/17/stories/2006021704241300.htm",
        # "http://www.hindu.com/2006/02/16/stories/2006021602511100.htm",
        # "http://www.hindu.com/2005/12/29/stories/2005122905321100.htm",
        # "http://www.hindu.com/2005/12/02/stories/2005120205021000.htm",
        # "http://www.hindu.com/2005/11/18/stories/2005111800141000.htm",
        # "http://www.hindu.com/2005/11/11/stories/2005111107231100.htm",
        # "http://www.hindu.com/2005/10/31/stories/2005103104681100.htm",
        # "http://www.hindu.com/2005/10/28/stories/2005102801891100.htm",
        # "http://www.hindu.com/2005/09/27/stories/2005092704521100.htm",
        # "http://www.hindu.com/2005/09/24/stories/2005092401651100.htm",
        # "http://www.hindu.com/2005/09/20/stories/2005092006370900.htm",
        # "http://www.hindu.com/2005/09/17/stories/2005091703701100.htm",
        # "http://www.hindu.com/2005/09/15/stories/2005091504671100.htm",
        # "http://www.hindu.com/2005/08/16/stories/2005081602880800.htm",
        # "http://www.hindu.com/2005/07/01/stories/2005070105241300.htm",
        # "http://www.hindu.com/2005/06/30/stories/2005063004691100.htm",
        # "http://www.hindu.com/2005/06/28/stories/2005062805431100.htm",
        # "http://www.hindu.com/2005/06/25/stories/2005062504361100.htm",
        # "http://www.hindu.com/2005/06/23/stories/2005062302701100.htm",
        # "http://www.hindu.com/2005/06/22/stories/2005062204871100.htm",
        # "http://www.hindu.com/2005/04/30/stories/2005043001001000.htm",
        # "http://www.hindu.com/2005/04/28/stories/2005042804831100.htm",
        # "http://www.hindu.com/2005/04/27/stories/2005042702871300.htm",
        # "http://www.hindu.com/2005/04/21/stories/2005042102341000.htm",
        # "http://www.hindu.com/2005/02/27/stories/2005022701271200.htm",
        # "http://www.hindu.com/2005/02/13/stories/2005021308391000.htm",
        # "http://www.hindu.com/2005/02/06/stories/2005020600211800.htm",
        # "http://www.hindu.com/2005/01/09/stories/2005010900221100.htm",
        # "http://www.hindu.com/2004/12/27/stories/2004122701051200.htm",
        # "http://www.hindu.com/2004/12/26/stories/2004122601191400.htm",
        # "http://www.hindu.com/2004/12/18/stories/2004121806321200.htm",
        # "http://www.hinduonnet.com/2004/12/14/stories/2004121406931200.htm",
        # "http://www.hindu.com/2004/12/12/stories/2004121201381600.htm",
        # "http://www.hindu.com/2004/09/09/stories/2004090903351200.htm",
        # "http://www.hindu.com/2004/09/08/stories/2004090807680100.htm",
        # "http://www.hindu.com/2004/08/08/stories/2004080804671400.htm",
        # "http://www.hindu.com/2004/08/02/stories/2004080203411200.htm",
        # "http://www.hindu.com/2004/08/01/stories/2004080100061100.htm",
        # "http://www.hindu.com/2004/07/30/stories/2004073002611200.htm",
        # "http://www.hindu.com/2004/07/21/stories/2004072102051200.htm",
        # "http://www.hindu.com/2004/07/20/stories/2004072003071200.htm",
        # "http://www.hindu.com/2004/07/18/stories/2004071800631100.htm",
        # "http://www.hindu.com/2004/07/04/stories/2004070400251100.htm",
        # "http://www.hindu.com/2004/07/04/stories/2004070400251100.htm",
        # "http://www.hindu.com/2004/07/01/stories/2004070103681200.htm",
        # "http://www.hindu.com/2004/06/26/stories/2004062606591200.htm",
        # "http://www.hinduonnet.com/2004/06/23/stories/2004062303171200.htm",
        # "http://www.hindu.com/2004/03/15/stories/2004031503631000.htm",
        # "http://www.hindu.com/2004/03/08/stories/2004030802311000.htm",
        # "http://www.hindu.com/mag/2003/07/27/stories/2003072700670100.htm",
        # "http://www.hindu.com/thehindu/mag/2003/07/13/stories/2003071300490100.htm",
        # "http://www.hindu.com/thehindu/mag/2003/06/22/stories/2003062200110200.htm",
        # "http://www.hindu.com/thehindu/mag/2003/06/15/stories/2003061500100100.htm",
        # "http://www.hindu.com/thehindu/mag/2003/06/08/stories/2003060800160200.htm",
        # "http://www.hindu.com/thehindu/mag/2003/06/01/stories/2003060100520100.htm",
        # "http://www.hindu.com/thehindu/mag/2002/12/29/stories/2002122900190400.htm",
        # "http://www.thehindu.com/thehindu/mag/2002/08/11/stories/2002081100500100.htm",
        # "http://www.thehindu.com/thehindu/mag/2001/12/23/stories/2001122300410100.htm",
        # "http://www.hindu.com/thehindu/mag/2001/11/11/stories/2001111100010100.htm",
        # "http://www.hinduonnet.com/thehindu/2001/10/14/stories/13140611.htm",
        # "http://www.hindu.com/thehindu/2001/05/06/stories/13060612.htm",
        # "http://www.hindu.com/thehindu/2001/04/29/stories/13290611.htm",
        # "http://www.hindu.com/thehindu/2001/03/25/stories/13250612.htm",
        # "http://www.hindu.com/thehindu/2001/03/18/stories/13180611.htm",
        # "http://www.hindu.com/thehindu/2001/02/25/stories/13250611.htm"
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
        l.add_xpath("location", " ")
        l.add_xpath("keywords", "//div[@id='articleKeywords']/p/a/text()")
        l.add_value("link", response.url)
        l.add_value("author", 'Sainath')
        return l.load_item()
