from django.db import models

# Create your models here.

'''model for blog post'''
class BlogPost(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    subtitle = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    date_posted = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    
    def __str__(self):
        return self.title
        
