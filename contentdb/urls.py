from django.conf.urls import url
from django.contrib import admin

from app.views import (IndexView, SearchFileView, CreateFileView)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', IndexView.as_view(), name='index_view'),
    url(r'^new_file$', CreateFileView.as_view(), name='create_file_view'),
    url(r'^search/$', SearchFileView.as_view(), name='search_file_view'),
]
