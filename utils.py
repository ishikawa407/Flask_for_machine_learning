import os.path
import time
import json


def log(*args, **kwargs):
    format = '%H:%M:%S'
    value = time.localtime(int(time.time()))
    dt = time.strftime(format, value)
    with open('log.txt', 'a', encoding='utf-8') as f:
        print(dt, *args, file=f, **kwargs)


def local_time(t):
    format = '%Y-%m-%d %H:%M:%S'
    value = time.localtime(int(t))
    dt = time.strftime(format, value)
    return dt