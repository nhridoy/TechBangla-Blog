from django.contrib import admin
from techblog.models import Category, SubCategory, Blog, BlogComment, BlogLikes

# Register your models here.
admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(Blog)
admin.site.register(BlogComment)
admin.site.register(BlogLikes)
