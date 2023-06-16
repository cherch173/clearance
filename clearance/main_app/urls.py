from django.contrib import admin
# Add the include function to the import
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # '' represents the "starts with" path
    path('', include('main_app.urls')),
]