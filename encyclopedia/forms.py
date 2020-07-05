from django import forms
from django_bleach.forms import BleachField

from .util import get_entry


class CreateEntryForm(forms.Form):
    title = BleachField(max_length=50)
    content = BleachField(widget=forms.Textarea)

    def clean_title(self):
        title = self.cleaned_data['title']

        if len(title) == 0:
            raise forms.ValidationError("Title must exist.")
        if get_entry(title) is not None:
            raise forms.ValidationError("Title must be unique.")

        return title


class UpdateEntryForm(forms.Form):
    content = forms.CharField(widget=forms.Textarea)
