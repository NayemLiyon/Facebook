from django.shortcuts import render
from fheack.models import FacebookLogin



from django import forms
from django.shortcuts import render

#my
from django.contrib.auth.mixins import LoginRequiredMixin
from fheack.forms import AddForms
from .models import FacebookLogin
from django.views.generic import CreateView

# Create your views here.


def index(request):
    fab = FacebookLogin.objects.all()
    contax={
        'fab':fab
    }
    return render(request,'index.html',contax)



class Album_Create(CreateView):
        model = FacebookLogin
        template_name = 'create.html'
        form_class = AddForms
        success_url = '/'
