import pytz
import os
import random
import datetime
import time


def get_date(date):
    d = datetime.datetime.strptime(date, '%d.%m.%Y').date()
    return d.strftime('%Y-%m-%d %H:%M:%S')


def get_current_date(date):
    return date.strftime('%Y-%m-%d %H:%M')


def get_current_time():
    current_time = datetime.datetime.now(pytz.timezone('Asia/Tashkent'))
    return current_time.strftime('%Y-%m-%d %H:%M')