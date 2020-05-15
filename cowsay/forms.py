from cowsay.models import Cowsay
from django import forms


class CowsayForm(forms.ModelForm):
    class Meta:
        model = Cowsay
        fields = '__all__'
