import json
import urllib2
import markdown2

from gplusblog import create_app

from flask.views import View
from flask import render_template, Response, request


class Index(View):
    def dispatch_request(self):
        return render_template('index.html')


class Buzz(View):
    def dispatch_request(self):
        app = create_app()

        url = ('https://www.googleapis.com/'
               'plus/v1/people/%s/activities/public?key=%s' % (
                   app.config['GPLUS_ID'],
                   app.config['API_KEY']))

        data = urllib2.urlopen(url)
        json_data = json.loads(data.read())

        return Response(json_data.get('items'))


class Markdown(View):
    def dispatch_request(self):
        data = request.args.get('data')
        return Response(markdown2.markdown(data))
