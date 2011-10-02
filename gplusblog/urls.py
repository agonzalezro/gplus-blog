from flask import Blueprint as Blueprint_


class Blueprint(Blueprint_):
    def register_urls(self, *urls):
        for url, view in urls:
            self.add_url_rule(url, view.__name__, view)


def setup_urls(app):
    from gplusblog.frontend import frontend

    app.register_blueprint(frontend, url_prefix='/')
