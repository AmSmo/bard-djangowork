from django.shortcuts import render
from .forms import ChooseForm, GameForm
from django.forms import formset_factory, forms
from .models import Sonnet
from madlibs import BardWeb as BW
from django.http import HttpResponse, Http404
from jinja2 import Markup
from django.shortcuts import redirect
import tempfile

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
        mp3= BW.WordSearch(id)
        mp3.read_it_to_me()

        return render(request,  'madlibs/marlib.html', {'content': Markup(mp3.edited.replace("\n", "<br /> \n"))})
    except:
        raise Http404('Sonnet not found, try a number from 1-154')

def play(request):

    if request.method == 'POST':
        filled_form = ChooseForm(request.POST)
        if filled_form.is_valid():
            choice= int(filled_form.cleaned_data["sonnet"])
            game_on = BW.WordSearch(choice)
            user_num= int(filled_form.cleaned_data["changes"])
            word_per_category = game_on.format_to_change(user_num)
            form = GameForm(categories=word_per_category)
            request.session['sonnet']= choice
            request.session['items'] = word_per_category
            return render(request, 'madlibs/play.html', {'gameform': form})

        else:
            game_on = (BW.WordSearch(0))
            word_per_category = game_on.format_to_change(15)
            form = GameForm(categories=word_per_category)
            request.session['sonnet'] = game_on.randomed
            request.session['items'] = word_per_category
            note = "Well, either something went wrong or you're in hurry so here is a random sonnet needing 15 new words"
            return render(request, 'madlibs/play.html', {'gameform': form,  'note': note})
    else:
        game_on = (BW.WordSearch(0))
        word_per_category = game_on.format_to_change(15)
        request.session['items']= word_per_category
        form = GameForm(categories=word_per_category)
        request.session['sonnet'] = game_on.randomed
        note = "Well, either something went wrong or you're in hurry so here is a random sonnet needing 15 new words"
        return render(request, 'madlibs/play.html', {'gameform': form, 'note' : note})
#
def answer(request):
    if request.method == "POST":
        form = GameForm(request.POST)
        if form.is_valid():
            game_on = BW.WordSearch(request.session['sonnet'])
            unclean= form.data
            nouns = []
            verbs = []
            adverbs = []
            adjectives = []
            verbeds = []
            plnouns = []
            for key, value in form.data.items():
                if key.startswith('noun'):
                    nouns.append(value)
                elif key.startswith('verb'):
                    verbs.append(value)
                elif key.startswith('adverb'):
                    adverbs.append(value)
                elif key.startswith('adjec'):
                    adjectives.append(value)
                elif key.startswith('pt'):
                    verbeds.append(value)
                elif key.startswith('pl'):
                    plnouns.append(value)
            game_on.new_nouns(nouns)
            game_on.new_verbs(verbs)
            game_on.new_adverbs(adverbs)
            game_on.new_adjectives(adjectives)
            game_on.new_verbed(verbeds)
            game_on.new_plnouns(plnouns)
            original = game_on.original
            clean_form = Markup(game_on.edited.replace("\n", "<br />"))
            llama = game_on.read_it_to_me().save('tmp/temp.wav')
        return render(request, 'madlibs/answer.html', {'duh': original, 'content': clean_form, 'dictionary':unclean, 'file': llama})

def about(request):
    return render(request, 'madlibs/about.html')
