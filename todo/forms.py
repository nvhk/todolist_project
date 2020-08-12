from django.forms import ModelForm
from .models import ToDosy


class ToDoFormularz(ModelForm):
    class Meta:
        model = ToDosy
        fields = ['title','memo', 'wazne' ]
