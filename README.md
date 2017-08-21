A Scrapy project that pulls data from "pgatour.com/stats" and displays the most
commonly used golf statistics in a table.  The "stats" spider crawls stats pages
for specified data from 2002-2016, but can easily be customized for different
data ranges.

The "players" spider is still in development and is not displayed on the
deployed app, but pulls key stats for all players who finished in the top 125 on the money list 
in the specified year.

## Quickstart

To pull PGA tour data, make sure you have the requirements downloaded and
execute:

```$> scrapy crawl stats -o data.csv```

This will import the crawled data into data.csv.  You may also use the ".json"
file extension.
