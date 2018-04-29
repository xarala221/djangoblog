from django.contrib import admin
from django_markdown.admin import MarkdownModelAdmin
from blog.models import Blog
# Register your models here.

admin.site.register(Blog, MarkdownModelAdmin)

#class YourModelAdmin(admin.ModelAdmin):
   # formfield_overrides = {MarkdownField: {'widget': AdminMarkdownWidget}}