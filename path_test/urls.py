from django.urls import path 
from path_test.views import *

 
urlpatterns =[ 
path("", home_view ),
path("contact/", contact_view ),
path("blog/", blog_view ),
path("about/", about_view ),
]