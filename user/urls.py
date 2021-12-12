
from django.urls import path
from.views import *
urlpatterns = [
    path("post_create/", post.as_view() , name="post-create" )

]
