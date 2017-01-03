from django.contrib import admin
from app.models import Category, Tag, File


admin.site.register(Category)


admin.site.register(Tag)


class FileAdmin(admin.ModelAdmin):
    list_display = ('name', 'content')

admin.site.register(File, FileAdmin)
