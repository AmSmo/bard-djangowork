from django.shortcuts import render
from .forms import ChooseForm
from django.forms import forms
from .models import Sonnet
from madlibs import BardWeb as BW
from django.http import HttpResponse
from jinja2 import Markup
from django.shortcuts import redirect
def home(request):
    form = ChooseForm()
    return render(request, 'madlibs/home.html', {'chooseform':form})


def marlib(request):
    if request.method == 'POST' and 'run_script' in request.POST:
        bob = BW.Sonnet(2)
        bob.read_it_to_me()
        return redirect(request.META['HTTP_REFERER'])

    if request.method == "POST":
        filled_form = ChooseForm(request.POST)
        if filled_form.is_valid():
            return render(request, 'madlibs/marlib.html')
    else:
        return render(request, 'madlibs/marlib.html', {'content': Markup(BW.specific_sonnet(2).replace("\n", "<br />")) })
