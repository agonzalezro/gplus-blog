from gplusblog.urls import Blueprint
from gplusblog.frontend import views


frontend = Blueprint('frontend', __name__)

frontend.register_urls(
    ('', views.Index.as_view('index')),
    ('buzz', views.Buzz.as_view('buzz')),
    ('markdown', views.Markdown.as_view('markdown')))
