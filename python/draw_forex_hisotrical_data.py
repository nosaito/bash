#!/usr/bin/env python
# -*- coding: utf8 -*-

# case in Python 2.6~
# same print behavior as python 3
from __future__ import print_function

import jsm
import datetime
import pandas as pd
import matplotlib.dates as mdate
import matplotlib.finance
import pylab as plt
import numpy as np
import sqlite3
import pandas.io.sql as psql

##################
#set stock number
##################
stock_name = 8411

#SQLlite
con = sqlite3.connect("data.db")
c = con.cursor()
try:
    c.execute("""create table all_sort(name integer ,date integer ,open integer ,high integer ,low integer ,close integer ,volume integer);""")
except:
    sql = 'select name,date from all_sort'
    a = c.execute(sql)
    for i, j in a:
        print(i, j)

#JSMによる日足習得
d = datetime.datetime.today()
q = jsm.Quotes()

start_date = datetime.date(2015, 1, 1)

yesterday = datetime.date.today() - datetime.timedelta(1)
end_date = yesterday

this_year = q.get_historical_prices(stock_name, jsm.DAILY, start_date, end_date)

#SQLに格納後Pandasへ移す
quotes = []
days=[]

colums_sql= u"insert into all_sort values(?,?,?,?,?,?,?)"
for i,each_day in enumerate(this_year):
    day =mdate.date2num(each_day.date)
    days.append(tuple([day]))
    quotes.append([i,each_day.open,each_day.close,each_day.high,each_day.low])
    for_sql = [stock_name,each_day.date,each_day.open,each_day.close,each_day.high,each_day.low,each_day.volume]
    c.execute(colums_sql,for_sql)

sql = 'select * from all_sort'
df = psql.read_sql(sql,con)

df2 = df[df['name'] == stock_name]
df2['date'] = df2['date'].apply(pd.to_datetime)

ascend_df = df2.sort_index(by='date',ascending=True)

#con.commit()


############################
#plot
############################

# SMA EMA
sma5 = pd.rolling_mean(df['close'], window=5)
sma5 = sma5.dropna()

ewma = pd.stats.moments.ewma
ewma5 = ewma(df['close'], span=5)

ewma25 = ewma(df['close'], span=25)
#ewma25 = ewma25.dropna()

#ロウソク足で描画
fig = plt.figure()
fig.subplots_adjust(bottom=0.2)
ax = fig.add_subplot(111)
ax.set_xticks(range(0,len(quotes),5))
ax.set_xticklabels([mdate.num2date(days[index][0]).strftime('%y %b %d') for index in ax.get_xticks()])

matplotlib.finance.candlestick(ax, quotes,colorup='red',colordown='blue')
ax.xaxis_date()
ax.autoscale_view()
plt.plot(sma5,label="SMA5")
plt.plot(ewma5,label="EMA5")
plt.plot(ewma25,label="EMA25")
plt.setp( plt.gca().get_xticklabels(),rotation=90, horizontalalignment='left')
plt.legend(loc="best")
ax.invert_xaxis()
plt.show()
