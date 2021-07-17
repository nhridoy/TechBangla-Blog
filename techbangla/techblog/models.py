from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import reverse


# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=25, unique=True)

    def has_subcategories(self):
        return self.subcategory.count()

    def __str__(self):
        return self.category_name


class SubCategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='subcategory')
    subcategory_name = models.CharField(max_length=25, unique=True)

    def __str__(self):
        return f"{self.category.category_name} - {self.subcategory_name}"


class Blog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_blog")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category')
    sub_category = models.ForeignKey(SubCategory, on_delete=models.CASCADE, related_name='sub_category')
    blogtitle = models.CharField(max_length=250, verbose_name="BLOG TITLE")
    blogcontent = models.TextField(verbose_name="BLOG CONTENT")
    blogimg = models.ImageField(upload_to="blog_image", verbose_name="ADD BLOG IMAGE")
    slug = models.SlugField(max_length=250, unique=True)
    published_date = models.DateTimeField(auto_now_add=True)
    edit_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.blogtitle

    # def get_absolute_url(self):
    #     return reverse('tech_blog:blog-content', kwargs={'slug_name': self.slug})


class BlogComment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='blog_comment')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_comment')
    comment = models.TextField()
    comment_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment

    class Meta:
        ordering = ('-comment_date',)


class BlogLikes(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='blog_like')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_like')
