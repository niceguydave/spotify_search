from django.conf.urls import url

from search.views import search_index

urlpatterns = [
    url(r'^$', search_index, name="search_index"),
]
