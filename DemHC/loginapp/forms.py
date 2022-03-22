from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import BlogPost

class CreateUserForms(UserCreationForm):
    class Meta:
        model=User
        fields=['username','email','password1','password2']


'''form for blog post of model BlogPost '''
class BlogPostForm(ModelForm):
    class Meta:
        model=BlogPost
        fields=['title','content','author']


