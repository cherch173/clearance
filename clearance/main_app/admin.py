from django.contrib import admin

from .models import Case, Reporting, Testimony, Photo

# Register your models here.
admin.site.register(Case)
admin.site.register(Reporting)
admin.site.register(Testimony)
admin.site.register(Photo)