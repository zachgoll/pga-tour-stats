# -*- coding: utf-8 -*-
import scrapy

class StatsSpider(scrapy.Spider):

    name = 'stats'
    allowed_domains = ['pgatour.com']

    def start_requests(self):
        stat_list = ['102', '103', '02437', '077', '329', '328', '327', '326', '419', 
                      '111', '130', '364', '119', '398', '399', '400', '484', '403']

        years = ['02', '03', '04', '05', '06', '07', '08', '09', '10',
                  '11', '12', '13', '14', '15', '16']
        
        urls = ["http://pgatour.com/stats/stat." + key + 
                ".20" + year + ".html" for year in years for key in stat_list]

        for url in urls:
            yield scrapy.Request(url = url, callback=self.parse)

    def parse(self, response):

        current_year = response.url.split('.')[-2]
        stat_title = response.xpath('//h3/text()')[-1].extract()
        average_stat = response.xpath('//*[contains(concat( " ", @class, " " ), \
                                      concat( " ", "hidden-medium", " " )) \
                                      and (((count(preceding-sibling::*) + 1) = 5) \
                                      and parent::*)]/text()').extract()

        yield {
            'Year': current_year,
            'Stat': stat_title,
            'First': average_stat[1],
            'Top 10': average_stat[10],
            'Top 25': average_stat[25],
            'Top 100': average_stat[100],
            'Last': average_stat[-1]
        }
