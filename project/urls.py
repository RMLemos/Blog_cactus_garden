from django.contrib import admin

from django.urls import include, path

urlpatterns = [
    path('', include('blog.urls')),
    path('summernote/', include('django_summernote.urls')),
    path('admin/', admin.site.urls),
]
