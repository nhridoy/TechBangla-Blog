from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, DetailView, ListView, UpdateView
from techblog.models import Blog, BlogLikes, BlogComment
from techblog.forms import BLogForm, CommentForm
from django.contrib.auth.mixins import LoginRequiredMixin
import uuid
from django.shortcuts import reverse
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required


# Create your views here.
class IndexBlogView(ListView):
    model = Blog
    context_object_name = 'blogs'
    template_name = "index.html"


class BlogView(DetailView, CreateView):
    model = Blog
    form_class = CommentForm
    # slug_field = 'slug_name'
    slug_url_kwarg = 'slug_name'
    template_name = "blog-content.html"

    def form_valid(self, form):
        comment_obj = form.save(commit=False)
        slug = str(self.request.path).split('/')[2]
        blog = Blog.objects.get(slug=slug)
        comment_obj.blog = blog
        comment_obj.user = self.request.user
        comment_obj.save()
        return HttpResponseRedirect(reverse('tech_blog:blog-content', kwargs={'slug_name': slug}))


@login_required
def LikeView(request, slug_name):
    blog = Blog.objects.get(slug=slug_name)
    user = request.user

    already_liked = BlogLikes.objects.filter(blog=blog, user=user)
    if not already_liked:
        like_post = BlogLikes(blog=blog, user=user)
        like_post.save()
    return HttpResponseRedirect(reverse('tech_blog:blog-content', kwargs={'slug_name': slug_name}))


class AllBlogsView(ListView):
    model = Blog
    context_object_name = 'blogs'
    template_name = "all-blogs.html"
    # extra_context = {
    #     'pathss': 'Test'
    # }

    # Class based context passing
    def get_context_data(self, **kwargs):
        context = super(AllBlogsView, self).get_context_data(**kwargs)
        context['path'] = str(self.request.path).split('/')[2]
        return context

    # def get_queryset(self):
    #     qs = super(AllBlogsView, self).get_queryset()
    #     return qs.filter(sub_category=self.kwargs.get('name'))


class AddNewView(LoginRequiredMixin, CreateView):
    model = Blog
    # fields = ('category', 'sub_category', 'blogtitle', 'blogcontent', 'blogimg',)
    form_class = BLogForm
    template_name = "add-new.html"

    def form_valid(self, form):
        blog_obj = form.save(commit=False)
        blog_obj.user = self.request.user
        title = blog_obj.blogtitle
        blog_obj.slug = title.replace(' ', '-') + str(uuid.uuid4())
        blog_obj.save()
        return HttpResponseRedirect(reverse('tech_blog:index'))


class EditBlogView(LoginRequiredMixin, UpdateView):
    model = Blog
    fields = ('category', 'sub_category', 'blogtitle', 'blogcontent', 'blogimg')
    slug_url_kwarg = 'slug_name'
    success_url = reverse_lazy('tech_blog:blog-content')
    template_name = 'add-new.html'

    # This is one method to reverse to previous page, another method is get_absolute_url in model.py page
    def get_success_url(self):
        return reverse('tech_blog:blog-content', kwargs={'slug_name': self.object.slug})


def custom_error_404(request, exception):
    return render(request, '../templates/404.html', {})