from django.contrib import admin
from . import models
from django.utils.html import format_html
# Register your models here.

@admin.register(models.Post2)
class PostAdmin(admin.ModelAdmin):
    list_display=('photo_tag','title' , 'author' , 'status' , 'published' , 'text' )
    list_filter=('status' , 'author')
    search_fields=('title' , 'text')
    list_editable=('author' , 'status')
    ordering=('published' , 'status')

    