
from django import urls
from django.contrib import admin
from django.urls import path,include
# for static file intro
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('bongobd.urls')),
    path('auth/', include('account.urls')),
    
    
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
