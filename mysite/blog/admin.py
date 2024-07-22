from django.contrib import admin
from .models import Post


# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'created')
    list_filter = ('title', 'status', 'created')
    search_fields = ('title', 'body')


admin.site.register(Post, PostAdmin)