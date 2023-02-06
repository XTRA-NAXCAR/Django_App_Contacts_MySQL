from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from .models import User, Contact
from .forms import ContactForm, UserForm
# Create your views here.
def home (request):
    if request.method == 'POST':
        users = User.objects.all()
        schedule = []
        for user in users:
            if user.Users == request.POST['username'] and user.Passwords == request.POST['password']:
                contacts = Contact.objects.all()
                for contact in contacts:
                    if contact.created_by_id == user.id:
                        schedule.append(contact)
                id_user = user.id
                context = {}
                response = render(request, 'user.html', {'context': context, 'contacts': schedule})
                response.set_cookie('id_user', id_user)
                return response
        return render(request, 'home.html', {'form': AuthenticationForm, 'error': 'Username or password is incorrect'})
    else:
        return render(request, 'home.html', {'form': AuthenticationForm})

def sign_in (request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(home)
    else:
        form = UserForm()
    return render(request, 'sign_in.html', {'form': form})

def user_view (request):
    schedule = []
    id_user = int(request.COOKIES['id_user'])
    contacts = Contact.objects.all()
    for contact in contacts:
        if contact.created_by_id == id_user:
            schedule.append(contact)
    return render(request, 'user.html', {'contacts': schedule})

def add (request):
    users = User.objects.all()
    id_user = int(request.COOKIES['id_user'])
    for user in users:
        if user.id == id_user:
            id = user.id
            if request.method == "POST":
                form = ContactForm(request.POST)
                if form.is_valid():
                    new_form = form.save(commit=False)
                    new_form.created_by_id = id
                    new_form.save()
                    return redirect(user_view)
                else:
                    form = ContactForm()
                    return render(request, 'add.html', {'form': form})
    form = ContactForm()
    return render(request, 'add.html', {'form': form})

def delete (request, contact_id):
    contact = Contact.objects.get(id=contact_id)
    contact.delete()
    return redirect(user_view)

def edit (request, contact_id):
    contact = Contact.objects.get(id=contact_id)
    if request.method == "POST":
        form = ContactForm(request.POST, instance=contact)
        if form.is_valid():
            form.save()
            return redirect(user_view)
    else:
        form = ContactForm(instance=contact)
    context = {"form": form }
    return render(request, "edit.html", context)
