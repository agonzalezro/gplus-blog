def setup_urls(app):
    from gplusblog import frontend

    app.register_blueprint(frontend, url_prefix='/')
