import json
import urllib2

from flask.views import View
from flask import render_template

from gplusblog import create_app
from gplusblog.core.models import Post


class Index(View):
    def get_buzz(self):
        app = create_app()

        url = ('https://www.googleapis.com/'
               'plus/v1/people/%s/activities/public?key=%s' % (
                   app.config['GPLUS_ID'],
                   app.config['API_KEY']))

        data = urllib2.urlopen(url)
        json_data = json.loads(data.read())
        buzz =[]
        for item in json_data.get('items'):
            buzz.append(Post.get_from_json(item))
        return buzz

    def dispatch_request(self):
        return render_template('index.html', buzz=self.get_buzz())
