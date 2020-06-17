from django.shortcuts import render
from .forms import ChooseForm, GameForm
from django.forms import formset_factory, forms
from .models import Sonnet
from madlibs import BardWeb as BW
from django.http import HttpResponse, Http404
from jinja2 import Markup
from django.shortcuts import redirect


def home(request):
    form = ChooseForm()
    return render(request, 'madlibs/home.html', {'chooseform':form})


def marlib(request):

    if request.method == "POST":
        filled_form = ChooseForm(request.POST)
        if filled_form.is_valid():
            return render(request, 'madlibs/marlib.html')
    else:
        bob = BW.Sonnet(5)
        bob.read_it_to_me()
        return render(request, 'madlibs/marlib.html', {'content': Markup(BW.specific_sonnet(5).replace("\n", "<br />")) })

def sonnet(request, id):

    try:
        mp3= BW.Sonnet(id)
        mp3.read_it_to_me()
        return render(request,  'madlibs/marlib.html', {'content': Markup(BW.specific_sonnet(id).replace("\n", "<br /> \n"))})
    except:
        raise Http404('Sonnet not found, try a number from 1-154')

def play(request):

    if request.method == 'POST':
        filled_form = ChooseForm(request.POST)
        if filled_form.is_valid():
            choice= int(filled_form.cleaned_data["sonnet"])
            game_on = BW.WordSearch(BW.specific_sonnet(choice))
            user_num= int(filled_form.cleaned_data["changes"])
            word_per_category = game_on.format_to_change(user_num)
            form = GameForm(categories=word_per_category)
            return render(request, 'madlibs/play.html', {'gameform': form, 'duh': game_on.original})

        else:
            game_on = BW.WordSearch(BW.specific_sonnet(0))
            word_per_category = game_on.format_to_change(15)
            form = GameForm(word_per_category)
            note = "Well, either something went wrong or you're in hurry so here is a random sonnet needing 15 new words"
            return render(request, 'madlibs/play.html', {'gameform': form, 'duh': game_on.original, 'note': note})
    else:
        game_on = BW.WordSearch(BW.specific_sonnet(0))
        word_per_category = game_on.format_to_change(15)
        form = GameForm(categories=word_per_category)
        note = "Well, either something went wrong or you're in hurry so here is a random sonnet needing 15 new words"
        return render(request, 'madlibs/play.html', {'gameform': form, 'duh': game_on.original, 'note' : note})
#
def answer(request):
    if request.method == "POST":
        form = GameForm(request.POST)
        if form.is_valid():
            llama= form.data
            return render(request, 'madlibs/answer.html', {'content': llama})
