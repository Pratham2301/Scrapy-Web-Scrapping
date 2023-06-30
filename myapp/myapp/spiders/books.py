import scrapy
from pathlib import Path
from pymongo import MongoClient
import datetime
import certifi
ca = certifi.where()
import os
from dotenv import load_dotenv
load_dotenv()



DB_URL = os.getenv('DB_URL')
client = MongoClient(DB_URL, tlsCAFile=ca)



def upload_to_mongoDB(page, title, image, price, avail, stars):

    db = client.ScrapyTutorial
    collection = db[page]

    data = {
        "Title": title,
        "Image": image,
        "Price": price,
        "In Stock": avail,
        "Ratings": stars,
        "date": datetime.datetime.now(tz=datetime.timezone.utc), 
    }

    id = collection.insert_one(data).inserted_id
    print("id : ", id)








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
            # print("Title : ", title)
            
            image = card.css("img").attrib["src"]
            # print("Image : ", image)
            
            price = card.css(".price_color::text").get()
            # print("Price : ", price)
            
            avail = card.css(".availability>i").attrib["class"]
            avail = (avail == "icon-ok")
            # print("In Stock : ", avail)
            
            rating = card.css(".star-rating").attrib["class"]
            stars = rating.split(" ")[-1]
            # print("Rating : ", stars)
            
            upload_to_mongoDB(page, title, image, price, avail, stars)
        
        
