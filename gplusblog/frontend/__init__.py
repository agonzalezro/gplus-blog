from gplusblog.urls import Blueprint
from gplusblog.frontend import views


frontend = Blueprint('frontend', __name__)

frontend.register_urls(
    ('', views.Index.as_view('index')))
