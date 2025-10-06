from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),       # Django admin
    path('', include('app_school.app_school_urls')),  # include your app routes
]
