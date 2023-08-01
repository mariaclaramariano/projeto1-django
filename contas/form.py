from django.forms import ModelForm
from .models import virada


class viradaform(ModelForm):
    class Meta:
       model = virada
       fields = ['descrição','valor','observações','categoria']
