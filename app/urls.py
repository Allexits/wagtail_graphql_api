from django.conf import settings
from django.urls import path
from django.conf.urls import include
from django.contrib import admin

from wagtail.admin import urls as wagtailadmin_urls

from grapple import urls as grapple_urls

urlpatterns = [
    path('', include('home.urls')),
    path("api/", include(grapple_urls)),
    path("admin/", include(wagtailadmin_urls)),
]


if settings.DEBUG:
    from django.conf.urls.static import static
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

