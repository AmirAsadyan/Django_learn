from django.shortcuts import render
from django.http.response import HttpResponse


def home_view(requst):
    return HttpResponse("<h1>this is home</h1>")


def contact_view(requst):
    return HttpResponse("<h1>this is contact</h1>")


def blog_view(requst):
    return HttpResponse("<h1>this is blog</h1>")


def about_view(requst):
    return HttpResponse("<h1>this is about</h1>")
