from django.urls import path
from django.conf.urls import url
from about.views import about
from home.views import homepage
from articles.views import article_list, article_details, article_create

app_name = "articles"
urlpatterns = [

    url(r"^$", article_list, name="list"),
    url(r"^create/$", article_create, name='create'),
    url(r"^(?P<slug>[\w-]+)/$", article_details, name="detail")



]
