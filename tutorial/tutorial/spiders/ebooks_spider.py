import scrapy

from tutorial.items import BookItem, NovelItem
class EbookSpider(scrapy.Spider):
    name = "ebook"
    allowed_domains = ["www.23us.so"]
    start_urls = [
        "https://www.23us.so/full.html",
    ]

    def parse(self, response):
        i = 0
        for tr in response.xpath("//table/tr[@bgcolor='#FFFFFF']"):
            if i != 0:
                break
            item = BookItem()
            item["title"] = tr.xpath("td[1]/a/text()").extract_first()
            item["link"] = tr.xpath("td[1]/a/@href").extract_first()
            item["author"] = tr.xpath("td[3]/text()").extract_first()
            item["words"] = tr.xpath("td[4]/text()").extract_first()
            item["update_time"] = tr.xpath("td[5]/text()").extract_first()
            item["status"] = tr.xpath("td[6]/text()").extract_first()
            yield item
            yield scrapy.Request(item["link"], callback=self.get_chapter_url, meta={"book_name": item["title"]})
            i += 1

    def get_chapter_url(self, response):
        novel_index = response.xpath("//p[@class='btnlinks']/a[1]/@href").extract_first()
        if novel_index:
            yield scrapy.Request(novel_index, callback=self.get_chapter, meta={"book_name": response.meta["book_name"]})

    def get_chapter(self, response):
        for td in response.xpath("//table/tr/td"):
            link = td.xpath("a/@href").extract_first()
            chapter_name = td.xpath("a/text()").extract_first()
            if link:
                yield scrapy.Request(link, callback=self.get_content, meta={
                    "book_name": response.meta["book_name"],
                    "chapter_link": link,
                    "chapter_name": chapter_name
                })

    def get_content(self, response):
        text = response.xpath("//dd[@id='contents']/text()").extract_first()
        novel = NovelItem()
        novel["title"] = response.meta["book_name"]
        novel["chapter_link"] = response.meta["chapter_link"]
        novel["chapter_name"] = response.meta["chapter_name"]
        novel["chapter_content"] = text
        yield novel

