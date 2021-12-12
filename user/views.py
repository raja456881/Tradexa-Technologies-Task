from django.shortcuts import render
from django.views import View
from .models import *
from .form import Userform


# Create your views here.

class post(View):

    def get(self, request):
        form = Userform()
        return render(request, "post.html", {'form': form})

    def post(self, request):
        if request.user.is_authenticated:
            user = User.objects.filter(pk=request.user.id).first()
            form = Userform(request.POST)
            if form.is_valid():
                new_post = Post(text=form.cleaned_data["text"], user=user)
                new_post.save()
                return render(request, "post.html")
            else:
                form = Userform()
                return render(request, "post.html", {'error': form.errors})
        else:
            return render(request, "post.html", {'error': "user is not login"})
