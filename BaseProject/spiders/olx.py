import scrapy
from scrapy.http import Request
import json

class OlxSpider(scrapy.Spider):
    name = "olx"    
    start_urls = ["https://www.olx.com.br/computadores-e-acessorios/notebook-e-netbook/estado-rj"]

    def start_requests(self):
        for pagina in range(1,20):
            yield scrapy.Request(f"https://www.olx.com.br/computadores-e-acessorios/notebook-e-netbook/estado-rj?o={pagina}")
        
    def parse(self, response, **kwargs):
        html = json.loads(response.xpath('//script[@id="__NEXT_DATA__"]//text()').get())
        items = html.get('props').get('pageProps').get('ads')
        for item in items :
            yield{
            'title': item.get('title'),
            'price':item.get('price'),
            }
