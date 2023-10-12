import scrapy


class OlxSpider(scrapy.Spider):
    name = "olx"
    allowed_domains = ["www.olx.com.br"]
    start_urls = ["https://www.olx.com.br/computadores-e-acessorios/notebook-e-netbook/estado-rj"]

    def parse(self, response):
        pass
