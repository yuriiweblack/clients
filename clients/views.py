from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Client

# Create your views here.


def clients(request):
    clients = Client.objects.all().values()
    template = loader.get_template('all_clients.html')
    context = {
        'clients': clients,
    }
    return HttpResponse(template.render(context, request))


def details(request, id):
    client = Client.objects.get(id=id)
    template = loader.get_template('details.html')
    context = {
        'client': client,
    }
    return HttpResponse(template.render(context, request))


def main(request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render())


def testing(request):
    template = loader.get_template('template.html')
    context = {
        'fruits': ['Apple', 'Cherry', 'Banana']
    }
    return HttpResponse(template.render(context,request))