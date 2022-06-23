from django.contrib import admin

from kingblog.models import Post

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':'title published_date'.split()}

admin.site.register(PostAdmin,Post)