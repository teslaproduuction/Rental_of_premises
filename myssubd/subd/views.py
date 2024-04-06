from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from django.forms import ModelForm
from django.http import request
from django.template.defaultfilters import slugify
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import *
from .forms import *
from django.shortcuts import render, redirect


# Create your views here.

def index(request):
    return render(request, 'index.html')

def Users(request):
    try:
        get_user = User.objects.all()
        context = {'Users': get_user}
        return render(request, 'Users.html', context)
    except:
        return redirect('index')

def Pomechenia(request):
    try:
        get_dogovor = Dogovor.objects.all()
        get_pomeschenie = Pomeschenie.objects.all()
        context = {'Pomechenia': get_pomeschenie, 'Dogovor': get_dogovor}
        return render(request, 'Pomechenia.html', context)
    except:
        return redirect('index')

def Dogovors(request, pk):
    try:
        get_dogovor = Dogovor.objects.filter(id_user_id=pk)
        context = {'Pomeschenie': get_dogovor}
        return render(request, 'Dogovor.html', context)
    except:
        return redirect('index')

def DogovorALL(request):
    try:
        get_dogovor = Dogovor.objects.all()
        context = {'AllDogovor': get_dogovor}
        return render(request, 'DogovorALL.html', context)
    except:
        return redirect('index')

def DogovorInfo(request, pk):
    try:
        get_dogovor = Dogovor.objects.get(id=pk)
        get_pomeschenie = Pomeschenie.objects.get(id=Dogovor.objects.get(id=pk).id_pomeschenie_id)
        get_zdanie = Zdanie.objects.get(id=Pomeschenie.objects.get(id=Dogovor.objects.get(id=pk).id_pomeschenie_id).id_zdanie_id)
        get_adres = Adres.objects.get(id=Zdanie.objects.get(id=Pomeschenie.objects.get(id=Dogovor.objects.get(id=pk).id_pomeschenie_id).id_zdanie_id).id_adres_id)
        get_user = User.objects.get(id=Dogovor.objects.get(id=pk).id_user_id)
        get_firma = Firma.objects.get(id_user_id=get_user)
        get_firmaZ = Firma.objects.get(id=Zdanie.objects.get(id=Pomeschenie.objects.get(id=Dogovor.objects.get(id=pk).id_pomeschenie_id).id_zdanie_id).id_firma_id)
        get_userZ = User.objects.get(id=Firma.objects.get(id=Zdanie.objects.get(id=Pomeschenie.objects.get(id=Dogovor.objects.get(id=pk).id_pomeschenie_id).id_zdanie_id).id_firma_id).id_user_id)
        context = {'Pomeschenie': get_pomeschenie, 'Zdanie': get_zdanie, 'Adres': get_adres, 'Dogovor': get_dogovor, 'User': get_user, 'FirmaZ': get_firmaZ, 'UserZ': get_userZ, 'Firma': get_firma}
        return render(request, 'DogovorInfo.html', context)
    except:
        return redirect('index')

def PomecheniaInfo(request, pk):

    try:
        get_pomeschenie = Pomeschenie.objects.get(id=pk)
        get_zdanie = Zdanie.objects.get(id=Pomeschenie.objects.get(id=pk).id_zdanie_id)
        get_adres = Adres.objects.get(id=Zdanie.objects.get(id=Pomeschenie.objects.get(id=pk).id_zdanie_id).id_adres_id)
        context = {'Pomechenia': get_pomeschenie, 'Zdanie': get_zdanie, 'Adres': get_adres}

        return render(request, 'PomecheniaInfo.html', context)
    except:
        return redirect('index')

class signup(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"


def ProfilUpdateView(request, pk):
    user = User.objects.get(id=pk)
    form = UserForm(instance=user)
    if request.method == 'POST':
        form = UserForm(request.FILES, request.POST or None, instance=user)
        if form.is_valid():
            form = form.save(commit=False)
            form.slug = slugify(form.title)
            print(form.cleaned_data['Fotografiya'])
            form.save()
            return redirect('index')
    context = {'form': form}
    return render(request, 'Profil.html', context)


class ProfilUpdateView(UpdateView):
    model = User
    form_class = UserForm
    template_name = 'Profil.html'
    success_url = reverse_lazy('index')


def is_member(user):
    return user.groups.get.All()

# @transaction.atomic
# def post(self, request, *args, **kwargs):
#         self.object = self.get_object()
#         form = self.get_form()
#         if form.is_valid():
#             return self.form_valid(form)
#         else:
#             return self.form_invalid(form)