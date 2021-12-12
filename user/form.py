from .models import Post
from django.forms import ModelForm


class Userform(ModelForm):
    class Meta:
        model = Post
        fields = ['text']
