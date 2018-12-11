import scrapy
import string


class CancerTermSpider(scrapy.Spider):
    name = 'nci-cancer-dictionary'
    start_urls = [
        'https://www.cancer.gov/publications/dictionaries/cancer-terms?expand=' + x for x in (string.ascii_lowercase + '#')
    ]

    def parse(self, response):
        data = {}
        for term in response.xpath('//dl[@class="dictionary-list"]/dl[@class="dictionary-list"]'):
            names = term.xpath('dt/dfn/a/text()').extract()
            definitions = term.xpath('dd[@class="definition"]/text()').extract()
            for name, definition in zip(names, definitions):
                name = name.rstrip('\n').lstrip('\r\n').lstrip(' ')
                definition = definition.rstrip('\r\n').rstrip(' ').rstrip('\r\n').lstrip('\r\n').lstrip(' ')
                data[name] = definition
        yield data
