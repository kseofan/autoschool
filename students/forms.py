from django import forms


class ChangeProfileForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100, required=True)
