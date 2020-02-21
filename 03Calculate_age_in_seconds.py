"""
Program oblicza twój dokładny wiek w sekundach po podaniu daty urodzenia
"""

import time, datetime

def date_to_seconds(year, month, day):
    t = datetime.datetime(year, month, day, 0, 0)
    return time.mktime(t.timetuple())

def calculate_age(year, month, day):
    y_seconds = date_to_seconds(year, month, day)
    n_seconds = time.time()
    return n_seconds - y_seconds


print(calculate_age(1998, 11, 24))

