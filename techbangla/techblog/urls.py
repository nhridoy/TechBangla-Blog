from django.urls import path
from techblog import views

app_name = 'tech_blog'

urlpatterns = [
    path('', views.IndexBlogView.as_view(), name='index'),
    path('blog-content/<slug:slug_name>', views.BlogView.as_view(), name='blog-content'),
    path('add-new/', views.AddNewView.as_view(), name='add-new'),
    path('edit-blog/<slug:slug_name>', views.EditBlogView.as_view(), name='edit-blog'),
    path('all/<name>/', views.AllBlogsView.as_view(), name='all-blogs'),
    path('like/<slug:slug_name>/', views.LikeView, name='like'),
]
