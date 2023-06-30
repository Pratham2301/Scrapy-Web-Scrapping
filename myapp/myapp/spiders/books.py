import scrapy
from pathlib import Path

class BooksSpider(scrapy.Spider):
    
    name = "books"
    
    def start_requests(self):
        urls = [
            "https://books.toscrape.com/catalogue/category/books/travel_2/index.html",
            "https://books.toscrape.com/catalogue/category/books/mystery_3/index.html",
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        
        page = response.url.split("/")[-2]
        filename = f"books-{page}"
        # Path(filename).write_bytes(response.body)
        # self.log(f"Saved file {filename}")
        
        cards = response.css(".product_pod")
        
        for card in cards:
            
            title = card.css("h3>a::text").get()
            print(title)
            
            image = card.css("img").attrib["src"]
            print(image)
        
        
