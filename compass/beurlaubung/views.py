from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import beurlaubung
import datetime
from django.urls import reverse_lazy
from django.utils import timezone
from django.urls import reverse
from django.http import HttpResponseRedirect

def default(request):
    return render(request, 'beurlaubung/index.html')

class BeurlaubungCreateView(CreateView):
    model=beurlaubung
    fields = [
        'name',
        'klasse',
        'tutor',
        'begruendung',
    ]

    def form_valid(self, form):
        self.object = form.save()
        succes_url = self.object.getredirceturl("/beurlaubung/status/")
        return HttpResponseRedirect(succes_url)
    
class BeurlaubungDetailView(DetailView):
    model=beurlaubung
