from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('myapp.urls')),
]

admin.site.site_header = "Blue Bird Public School"
admin.site.site_title = "Major Admin Panel"
admin.site.index_title = "Welcome Admin to BBPS Portal"