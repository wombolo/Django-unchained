from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import get_template


def home_page(request):
    my_title = 'Hello there 111345'
    doc = "<h1>{title}</h1>".format(title=my_title)
    return render(request, "hello_world.html", {"title": my_title})


def about_page(request):
    return render(request, "about.html", {"title": 'About page'})


def contact_page(request):
    return render(request, "about.html", {"title": 'Contact page'})


def example_page(request):
    context = {"title": "Example page"}
    template_name = "about.html"
    template_obj = get_template(template_name)
    rendered_item = template_obj.render(context)
    return HttpResponse(rendered_item)

