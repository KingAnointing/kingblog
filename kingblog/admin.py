from django.contrib import admin

from kingblog.models import *

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ('title','slug',)
    prepopulated_fields = {'slug':('title',),}

admin.site.register(Post, PostAdmin)

admin.site.register(Comment)