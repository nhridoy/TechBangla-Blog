from django import forms
from techblog.models import Blog, BlogComment


class BLogForm(forms.ModelForm):
    blogimg = forms.ImageField(label='Add Image', widget=forms.FileInput(
        attrs={'class': 'input-form', 'type': 'file', 'accept': 'image/jpeg'}))

    class Meta:
        model = Blog
        fields = ('category', 'sub_category', 'blogtitle', 'blogcontent', 'blogimg',)


class CommentForm(forms.ModelForm):
    comment = forms.CharField(widget=forms.Textarea, label='')

    class Meta:
        model = BlogComment
        fields = ('comment',)
