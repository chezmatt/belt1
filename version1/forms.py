from django import forms
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from .models import User
import bcrypt
from argcomplete import default_validator

class UserNameField(forms.CharField):
    def validate(self, value):
        super(UserNameField, self).validate(value)
        
        try:
            username = User.objects.get(username=value)
        except ObjectDoesNotExist:
            # This is a good result
            pass
            return
        
        raise forms.ValidationError("User name is already in use.")  
        
        return  

class RegisterForm(forms.Form):
    first_name = forms.CharField(max_length=75)
    last_name = forms.CharField(max_length=75)
    username = UserNameField(max_length=75)
    email = forms.EmailField(max_length=255)
    password = forms.CharField(max_length=255)
    dob_date = forms.DateField()
    