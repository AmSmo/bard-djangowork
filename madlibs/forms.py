from django import forms

from .models import Sonnet

class ChooseForm(forms.Form):
    random = forms.ChoiceField(widget=forms.RadioSelect,
                               choices=[('random', 'Random'), ('spec', 'Specific Sonnet')], label="Random or Not:")
    random.widget.attrs.update({'onchange': 'random()'})
    sonnet = forms.IntegerField(max_value=154, min_value= 1,
                                label="Which sonnet would you choose?", initial=1)
    changes = forms.IntegerField(max_value=30, min_value=15,
                                 required=True, label="How many words do you want to change?", initial=15)

class GameForm(forms.Form):
    def __init__(self, *args, **kwargs):
        categories= kwargs.pop('categories', None)
        super(GameForm, self).__init__(*args, **kwargs)

        if categories:
            for i in range(0, categories[0]):
                j=i+1
                self.fields["noun_%d" % j] = forms.CharField(max_length=15, label=("Noun "+ str(j)+":"), initial=("noun_%d" % j))
                self.fields["noun_%d" % j].widget.attrs.update({'class': 'special'})

            for i in range(0, categories[1]):
                j = i + 1
                self.fields["verb_%d" % j] = forms.CharField(max_length=15, label=("Verb "+ str(j)+":"), initial=("verb_%d" % j))
                self.fields["verb_%d" % j].widget.attrs.update({'class': 'special verb'})
            for i in range(0, categories[2]):
                j = i + 1
                self.fields["adverb_%d" % j] = forms.CharField(max_length=15, label=("Adverb "+ str(j)+":"), initial=("adverb%d" % j))
                self.fields["adverb_%d" % j].widget.attrs.update({'class': 'special adverb'})

            for i in range(0, categories[3]):
                j = i + 1
                self.fields["adjective_%d" % j] = forms.CharField(max_length=15, label=("Adjective "+ str(j)+":"), initial=("adjective%d" % j))
                self.fields["adjective_%d" % j].widget.attrs.update({'class': 'special adjective'})
            for i in range(0, categories[4]):
                j = i + 1
                self.fields["ptverb_%d" % j] = forms.CharField(max_length=15, label=("Past Tense Verb "+ str(j)+":"), initial=("verbed%d" % j))
                self.fields["ptverb_%d" % j].widget.attrs.update({'class': 'special verbed'})
            for i in range(0, categories[5]):
                j = i + 1
                self.fields["plnoun_%d" % j] = forms.CharField(max_length=15, label=("Plural Noun "+ str(j)+":"), initial=("plnoun%d" % j))
                self.fields["plnoun_%d" % j].widget.attrs.update({'class': 'special'})

    def nouns(self):
        return [self[name] for name in filter(lambda x: x.startswith('noun'), self.fields)]

    def verbs(self):
        return [self[name] for name in filter(lambda x: x.startswith('verb'), self.fields)]

    def adverbs(self):
        return [self[name] for name in filter(lambda x: x.startswith('adverb'), self.fields)]

    def adjectives(self):
        return [self[name] for name in filter(lambda x: x.startswith('adject'), self.fields)]

    def verbeds(self):
        return [self[name] for name in filter(lambda x: x.startswith('ptverb'), self.fields)]

    def plnouns(self):
        return [self[name] for name in filter(lambda x: x.startswith('plnoun'), self.fields)]


