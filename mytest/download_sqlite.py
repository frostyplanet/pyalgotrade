#!/usr/bin/env python
# coding:utf-8

import os
import sys
from pyalgotrade.tools.yahoofinance import download_csv
from pyalgotrade.barfeed import sqlitefeed
from pyalgotrade.barfeed import yahoofeed
import datetime

def download_sqlite(symbol, dir_='.'):
    file_path = os.path.join(dir_, "%s.sqlite" % (symbol))
    tmp_path = os.path.join(dir_, "%s.csv.tmp" % (symbol))
    db = sqlitefeed.Database(file_path)
    symbol = symbol.upper()

    last_ts = db.get_last_timestamp(symbol)
    if not last_ts:
        begin = datetime.datetime.now() - datetime.timedelta(days=30*6)
    else:
        begin = datetime.datetime.fromtimestamp(last_ts)
    end = datetime.datetime.now()
    content = download_csv(symbol, begin, end, 'd')
    with open(tmp_path, 'w') as f:
        f.write(content)
    feed_tmp = yahoofeed.Feed()
    feed_tmp.addBarsFromCSV(symbol, tmp_path)
    db.addBarsFromFeed(feed_tmp)
    os.remove(tmp_path)


def inspect(symbol, dir_='.'):
    db_file = os.path.join(dir_, "%s.sqlite" % (symbol))
    symbol = symbol.upper()
    feed = sqlitefeed.Feed(db_file, 86400)
    feed.loadBars(symbol)
    for bar in feed:
        print bar

if __name__ == '__main__':
    download_sqlite('600261.ss')
#    inspect('600261.ss')

    
     

# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4 :
