# -*- coding: utf-8 -*-
import scrapy

players = {}
YEAR = '2016'

class PlayersSpider(scrapy.Spider):
    name = 'players'
    allowed_domains = ['pgatour.com']
    start_urls = ['http://www.pgatour.com/stats/stat.109.' + YEAR + '.html']

    def parse(self, response):
        temp_list = []
        for player in response.xpath('//*[(@id = "statsTable")]//a/text()') \
                                    .extract():
            temp_list.append(" ".join(str(player).split('\xa0')))

        for i in range(125):
            players[temp_list[i]] = {}

        stat_list = ['119', '103', '102', '130', '364', '111']

        for item in stat_list:
            yield scrapy.Request("http://pgatour.com/stats/stat." + item + "." + YEAR + ".html", callback = self.parse_players)

    def parse_players(self, response):
        player_list = []
        stat_title = response.xpath('//h3/text()')[-1].extract()

        for player in response.xpath('//*[(@id = "statsTable")]//a/text()').extract():
            player_list.append(" ".join(str(player).split('\xa0')))
        stat_list = response.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "hidden-medium", " " )) and (((count(preceding-sibling::*) + 1) = 5) and parent::*)]/text()').extract()
        for i in range(len(player_list)):
            if player_list[i] in players:
                players[player_list[i]][stat_title] = stat_list[i+1]

