from django.shortcuts import render
from .models import virada
import datetime
from .form import viradaform
from contas.models import virada


def home(request):
    data = {}
    data['virada'] = ['t1','t2','t3']
    data['now'] = datetime.datetime.now()
   #html = "<html><body>It is now %s.</body></html>" %   now
    return render(request, 'contas/home.html', data)

def listagem(request):
    data = {}
    data ['virada']= virada.objects.all() 
    return render(request, 'contas/listagem.html', data)

def nova_virada(request):
    data = {}
    form = viradaform()
    data['form']= form
    return render(request, 'contas/form.html',data)