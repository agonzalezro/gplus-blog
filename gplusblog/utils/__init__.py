from datetime import datetime


def string_to_datetime(date):
    format = '%Y-%m-%d %H:%M:%S'
    date = date.split('.')[0]
    date = date.replace('T', ' ')
    return datetime.strptime(date, format)
