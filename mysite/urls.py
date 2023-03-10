from django.contrib import admin
from django.urls import path, include 
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.static import serve
from django.contrib.auth.models import Group
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
   
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) 



