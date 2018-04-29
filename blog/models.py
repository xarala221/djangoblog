from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
#from tinymce.models import HTMLField
#from django_markdown.models import MarkdownField
 #content         = HTMLField()//for tinymce
    #content         = MarkdownField() #for markdown

class Blog(models.Model):
    title           = models.CharField(max_length=100)
    content         = models.TextField()
    author          = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    picture         = models.FileField()
    created_at      = models.DateTimeField(auto_now=False, auto_now_add=False)
    published_at    = models.DateTimeField(auto_now=True, auto_now_add=False)


    def get_absolute_url(self):
        return reverse('details', kwargs={'id': self.id})

    def __str__(self):
        return self.title