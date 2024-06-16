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

import pprint
def testing(request):
    # client = Client.objects.all().values_list('firstname')
    # client = Client.objects.filter(firstname="David", id=3).values()
    # client = Client.objects.filter(firstname__startswith='D').values() | Client.objects.filter(firstname__startswith='M').values()
    # client = Client.objects.filter(firstname="David", id=3).values() | Client.objects.filter(firstname="Misha").values()
    # client = Client.objects.all().order_by('firstname').values()
    # client = Client.objects.all().order_by('-firstname').values()
    client = Client.objects.all().order_by('firstname', '-id').values()
    template = loader.get_template('template.html')
    context = {

        'clients': client
    }
    x = context['clients']
    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(x)


    return HttpResponse(template.render(context, request))

# def testing(request):
#     template = loader.get_template('template.html')
#     context = {
#         'firstname': 'Linux',
#         'cars': ["Opel", "Audi", "Mazda", "BMW"]
#     }
#
#     return HttpResponse(template.render(context, request))