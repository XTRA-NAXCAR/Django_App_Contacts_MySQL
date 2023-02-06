from django import forms
from .models import User, Contact

class ContactForm (forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['Name', 'Number', 'Email']
    
class UserForm (forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'
