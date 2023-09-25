from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings


from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
   path('admin', admin.site.urls),
   path('', views.home, name='home'),
   path('/shops', include('shops.urls')),
]
urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()
