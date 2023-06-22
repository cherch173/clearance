from django.contrib import admin

from .models import Case, Reporting, Testimony, Photo, Video, Comment

# Register your models here.
admin.site.register(Case)
admin.site.register(Reporting)
admin.site.register(Testimony)
admin.site.register(Photo)
admin.site.register(Video)
admin.site.register(Comment)

