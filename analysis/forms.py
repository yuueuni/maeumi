from django import forms


class InputImage(forms.Form):
    house = forms.ImageField(label='house')
    tree = forms.ImageField(label='tree')
    person = forms.ImageField(label='person')