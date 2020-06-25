from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from wagtail.admin import urls as wagtailadmin_urls
from wagtail.core import urls as wagtail_urls
from wagtail.documents import urls as wagtaildocs_urls

# urls.py: provides all the urls for the pages
#   Requires: app.urls (under app) in: path("", include('app.urls')),
#             common.py (under uwhvz/settings) in:
#               urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#   Used in: common.py (under uwhvz/settings) in: ROOT_URLCONF = 'uwhvz.urls'

# Only the 'app.urls' are manual, other path() functions are for wagtail/Django (admin)
urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include('app.urls')),
    path("cms/", include(wagtailadmin_urls)),
    path("documents/", include(wagtaildocs_urls)),
    path("", include(wagtail_urls)),
]

# Adds media URL variables given from common.py
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
