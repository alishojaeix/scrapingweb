import scrapy


class ThemeSpider(scrapy.Spider):
    name = "theme"
    allowed_domains = ["www.rtl-theme.com"]
    start_urls = ["https://www.rtl-theme.com/"]

    def parse(self, response):
        for theme in response.css("div"):
            text = theme.css("span.text::text").get()
            author = theme.css("small.author::text").get()
            tags = theme.css("div.tags a.tag::text").getall()

            page_title = response.xpath('//title/text()').get()
            yield {
                'Text': text,
                'title': page_title,
                'Tags': tags,
                'Author': author
            }
