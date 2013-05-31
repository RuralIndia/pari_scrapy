# Scrapy settings for pari_scrapy project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#

BOT_NAME = 'pari_scrapy'

SPIDER_MODULES = ['pari_scrapy.spiders']
NEWSPIDER_MODULE = 'pari_scrapy.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'pari_scrapy (+http://www.yourdomain.com)'

FEED_FORMAT = 'jsonlines'

# FEED_STORAGES = 'file:///Users/Admin/projects/pari_scrapy/export.json'
