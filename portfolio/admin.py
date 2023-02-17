from django.contrib import admin
from .models import Project
from parler.admin import TranslatableAdmin

admin.site.register(Project, TranslatableAdmin)