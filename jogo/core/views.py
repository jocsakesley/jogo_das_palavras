from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import SubmitForm
import random
import os
from .models import SubmitModel, Db_SubmitModel
# Create your views here.

def home(request):
    letters = []
    try:
        word = Db_SubmitModel.objects.all()[0]
        for letter in str(word):
            letters.append(letter)
    except IndexError:
        pass
    form = SubmitForm(request.POST)
    if request.method == "POST":
        return submit(request, letters, form)
    else:
        Db_SubmitModel.objects.all().delete()
        SubmitModel.objects.all().delete()
        word_letters()
        return render(request, "index.html", {'form': form, 'letters': letters})

def submit(request, letters, form):
    if not form.is_valid():
        return render(request, "index.html", {'form': form})
    if form.cleaned_data not in list(SubmitModel.objects.all().values('letter')):
        SubmitModel.objects.create(letter=form.cleaned_data['letter'])
    else:
        messages.error(request, "Essa letra já foi enviada")
    list_db_letters = [x['letter'].upper() for x in SubmitModel.objects.all().values('letter')]
    return render(request, 'index.html', {'form': form, 'letters': letters, 'list_db_letters': list_db_letters})

def word_letters():
    module_dir = os.path.dirname(__file__)
    file_path = os.path.join(module_dir, "words.txt")
    with open(file_path, "r", encoding='utf-8') as words:
        word = words.readlines()
        word = random.choices(word)[0].strip('\n')
    if {'word_db':word} not in Db_SubmitModel.objects.all().values('word_db'):
        Db_SubmitModel.objects.create(word_db=word.upper())


def new(request):
    return HttpResponseRedirect('/')
