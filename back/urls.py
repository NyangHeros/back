from result.views import SnnView
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from django.conf import settings
from django.views.static import serve
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^media/(?P<path>.*)$', serve,
        {'document_root': settings.MEDIA_ROOT}),
    url(r'^static/(?P<path>.*)$', serve,
        {'document_root': settings.STATIC_ROOT}),
    path('api/snn', SnnView),
]
