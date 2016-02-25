from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic

from .models import Inventary
# Create your views here.

class IndexView(generic.ListView):
    template_name = 'ISStuRa/index.html'
    context_object_name = 'inventary_list'

    def get_queryset(self):
        return Inventary.objects.order_by('-id')
