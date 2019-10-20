#!/usr/bin/env python
#coding: utf-8

import datetime
import calendar

y = 2019
m = 10
d = 21
weekdayNumber = datetime.date(y,m,d).weekday()
weekday = calendar.day_name[weekdayNumber]
print weekday
