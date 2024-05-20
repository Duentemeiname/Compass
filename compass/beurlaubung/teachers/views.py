from django.shortcuts import render
from compass.beurlaubung.models import beurlaubung
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

def default(request):
    return render(request, 'beurlaubung/teachers/index.html')

class TeachersListView(ListView):
    model = beurlaubung
    template_name = 'beurlaubung/teachers/teachers_list.html'

class TeachersUpdateView(UpdateView):
    model = beurlaubung
    fields=['name', 'klasse', 'tutor', 'begruendung']
    template_name = 'beurlaubung/teachers/edit_requests.html'