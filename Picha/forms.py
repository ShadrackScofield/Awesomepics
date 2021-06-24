from django.forms import ModelForm
from .models import *


class pictures_form(ModelForm):
    class Meta:
        model = Pictures
        fields = ('name', 'image')


class tech_form(ModelForm):
    class Meta:
        model = Tech_pics
        fields = ('name', 'image')


class puppy_form(ModelForm):
    class Meta:
        model = Dog_pics
        fields = ('name', 'image')
