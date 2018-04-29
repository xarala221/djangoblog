from django import forms
#from django.contrib.flatpages.models import FlatPage
#from tinymce.widgets import TinyMCE
#from django_markdown.fields import MarkdownFormField
#from django_markdown.widgets import MarkdownWidget
from blog.models import Blog


class BlogForm(forms.ModelForm):
    #content = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30}))
    #content = forms.CharField(widget=MarkdownWidget())
     #content2 = MarkdownFormField()
    class Meta:
        model = Blog
        fields = [
            'title',
            'content',
            'picture',
        ]
