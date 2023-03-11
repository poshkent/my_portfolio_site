from django.contrib import admin

# Register your models here.

from .models import Jamboard, File, Image

admin.site.register(Jamboard)
admin.site.register(File)
admin.site.register(Image)