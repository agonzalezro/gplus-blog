import datetime

from gplusblog.utils import string_to_datetime

from flask import Markup


class Post(object):
    author = None
    published = None
    updated = None
    title = None
    content = None
    url = None
    replies = None

    @classmethod
    def get_from_json(cls, json_data):
        if json_data.get('verb') == 'share':
            obj = Reshared()
        else:
            obj = cls()
        obj.fill_data_from_json(json_data)
        return obj

    def updated_if_needed(self, updated_date):
        updated_date = string_to_datetime(updated_date)
        if updated_date > self.published + datetime.timedelta(seconds=5):
            return updated_date

    def fill_data_from_json(self, json_data):
        self.author = json_data.get('actor').get('displayName')
        self.title = json_data.get('title')
        self.published = string_to_datetime(json_data.get('published'))
        self.updated = self.updated_if_needed(json_data.get('updated'))
        self.url = json_data.get('url')
        self.content = Markup(json_data.get('object').get('content'))
        self.replies = json_data.get('object').get('replies').get('totalItems')


class Reshared(Post):
    annotation = None
    original_author = None  # Original author name

    def fill_data_from_json(self, json_data):
        super(Reshared, self).fill_data_from_json(json_data)
        self.annotation = json_data.get('annotation')
        self.original_author = (json_data.get('object')
                                         .get('actor')
                                         .get('displayName'))
