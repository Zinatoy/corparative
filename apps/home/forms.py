from django import forms 
from apps.home.models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact 
        fields = ('name', 'phone', 'email', 'subject', 'message')
        widgets = {
            'name' : forms.TextInput(attrs={'class': "form-control"}),
            'phone' : forms.TextInput(attrs={'class': "form-control"}),
            'email' : forms.EmailInput(attrs={'class': "form-control"}),
            'subject' : forms.TextInput(attrs={'class': "form-control"}),
            'message' : forms.TextInput(attrs={'class': "form-control"}),
        }

 