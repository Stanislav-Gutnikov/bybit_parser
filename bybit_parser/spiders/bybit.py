import scrapy
from datetime import datetime


class BybitParseSpider(scrapy.Spider):
    name = 'bybit'
    main_url = 'https://announcements.bybit.com'
    start_urls = ['https://announcements.bybit.com/en/?category=&page=1']

    def parse(self, response):
        dates = response.css(
            'div.article-item-date::text',
            ).getall()
        news = response.css('div.article-item')
        news = news.css('span::text').getall()
        urls = response.css('div.article-list')
        urls = urls.css('a::attr(href)').getall()
        news_list = []
        for new in news:
            if new != 'lg' and new != '...':
                news_list.append(new)
        for index in range(0, len(dates)):
            yield {
                'new': news_list[index],
                'date': dates[index],
                'datetime': datetime.now(),
                'url': self.main_url + urls[index]
                }
