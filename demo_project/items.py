# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader.processors import MapCompose, TakeFirst, Join
from w3lib.html import remove_tags

def clean_quotation(value):
	return value.replace(u"\u201c", "").replace(u"\u201d", "")


class QuoteItem(scrapy.Item):
    text = scrapy.Field(
    	input_processor = MapCompose(str.strip, clean_quotation),
    	output_processor = TakeFirst()
    	)
    author = scrapy.Field(
    	input_processor = MapCompose(str.strip, remove_tags),
    	output_processor = TakeFirst()
    	)
    tags = scrapy.Field(
    	input_processor = MapCompose(remove_tags),
    	output_processor = Join(',')
    	)
