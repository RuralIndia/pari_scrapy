from scrapy.item import Item, Field
from scrapy.contrib.loader.processor import MapCompose, Join, TakeFirst
from datetime import datetime
from django.utils import timezone


def remove_empty(str):
    stripped = str.strip()
    return stripped if stripped else None

def strip(str):
    return str.strip().strip('- ')

def change_date_format(str):
    if str.isdigit():
        date = datetime.strptime(str, '%Y%m%d').replace(tzinfo=timezone.utc)
    else: 
        date = datetime.strptime(str, '%B %d, %Y').replace(tzinfo=timezone.utc)
    return unicode(date)

class Article(Item):
    title = Field(input_processor=MapCompose(strip))
    link = Field()
    content = Field(input_processor=MapCompose(strip), output_processor=Join())
    date = Field(input_processor=MapCompose(remove_empty, change_date_format), output_processor=Join())
    location = Field(input_processor=MapCompose(remove_empty), output_processor=TakeFirst())
    author = Field()
    keywords = Field()
