from django.contrib import admin
from myblog.models import article
from myblog.models import BlogPostAdmin
from myblog.models import aboutme
from myblog.models import Category
# Register your models here.
admin.site.register(article, BlogPostAdmin)
admin.site.register(aboutme)
admin.site.register(Category)
