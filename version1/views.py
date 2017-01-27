from django.contrib import messages
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import generic
import bcrypt

from .forms import RegisterForm
from .models import User

def index(request):
    # TODO: Check the session/user state and redirect accordingly
    # For now just go to the register page
    return redirect(reverse('register'))
                    
class register(generic.edit.FormView):
    template_name = 'register.html'
    form_class = RegisterForm
    success_url = 'success'

    def form_valid(self, form):
        pw_hash = bcrypt.hashpw(form.cleaned_data.get('password').encode(),bcrypt.gensalt())
        
        user = User.objects.create(first_name = form.cleaned_data.get('first_name'),
                                   last_name = form.cleaned_data.get('last_name'),
                                   username = form.cleaned_data.get('username'),
                                   email = form.cleaned_data.get('email'),
                                   password = pw_hash
                                   )
        
        messages.add_message(self.request, messages.INFO, 'User registered.')
        
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        # form.create_user()
        return super(register, self).form_valid(form)

def login(request):
    return redirect(reverse('success'))
    
def success(request):
    return render(request, 'success.html')

def logout(request):
    return redirect(reverse('login_or_register.html'))
    
                    