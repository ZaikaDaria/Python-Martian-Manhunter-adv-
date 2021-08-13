from django.forms import ModelForm
from .models import *


class NewsLetterForm (ModelForm):
    class Meta:
        model = NewsLetter
        fields = ['email']
        labels = {'Email': ''}