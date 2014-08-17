#!/bin/sh

python -c "from pyalgotrade.tools import yahoofinance; yahoofinance.download_daily_bars('sh601333.ss', 2014, 'sh601333-2014.csv')"
