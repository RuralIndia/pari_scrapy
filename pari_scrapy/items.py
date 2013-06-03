from scrapy.item import Item, Field
from scrapy.contrib.loader.processor import MapCompose, Join, TakeFirst


def remove_empty(str):
    stripped = str.strip()
    return stripped if stripped else None


class Article(Item):
    title = Field()
    link = Field()
    content = Field(output_processor=Join())
    date = Field(input_processor=MapCompose(remove_empty), output_processor=Join())
    location = Field(output_processor=TakeFirst())
    author = Field()
    keywords = Field()
