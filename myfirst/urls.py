from django.contrib import admin
from django.conf.urls import include as include_conf
from django.urls import path, include

urlpatterns = [
    path('', include('album.urls')),
    path('grappelli/', include_conf('grappelli.urls')),
    path('admin/', admin.site.urls),
]
