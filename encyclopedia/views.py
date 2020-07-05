from random import choice

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.views import View
from django.urls import reverse

from . import util
from .forms import CreateEntryForm, UpdateEntryForm


class EntryIndexView(View):
    def get(self, request):
        return render(request, "encyclopedia/index.html", {
            "entries": util.list_entries()
        })


class EntryDetailView(View):
    def get(self, request, title):
        entry = util.get_entry(title)

        if entry:
            return render(request, "encyclopedia/detail.html", {
                "entry": util.get_entry(title),
                "title": title
            })
        else:
            raise Http404("Cannot be found")


class EntrySearchView(View):
    def get(self, request):
        q = request.GET.get('q')

        if q:
            entries = [item for item in util.list_entries() if q in item] or []
            if len(entries) == 1:
                return HttpResponseRedirect(reverse('encyclopedia:detail', kwargs={'title': entries[0]}))
            elif not entries:
                raise Http404("Cannot be found")
            else:
                return render(request, "encyclopedia/search.html", {
                    "entries": entries})
        else:
            raise Http404("There must be search criteria")


class EntryCreateView(View):
    def get(self, request):
        form = CreateEntryForm()
        return render(request, 'encyclopedia/entry_form.html', {
            'create': True,
            'form': form
        })

    def post(self, request):
        form = CreateEntryForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data.get('title')
            content = form.cleaned_data.get('content')
            util.save_entry(title, content)
            return HttpResponseRedirect(reverse('encyclopedia:index'))
        else:
            form = CreateEntryForm(request.POST)
            return render(request, 'encyclopedia/entry_form.html', {
                'create': True,
                'form': form,
                'errors': form.errors
            })


class EntryUpdateView(View):
    def get(self, request, title):
        entry = util.get_entry(title)
        form = UpdateEntryForm({'content': entry, 'title': title})
        return render(request, 'encyclopedia/entry_form.html', {
            'create': False,
            'form': form,
            'title': title
        })

    def post(self, request, title):
        form = UpdateEntryForm(request.POST)

        if form.is_valid():
            content = form.cleaned_data.get('content')
            util.save_entry(title, content)
            return HttpResponseRedirect(reverse('encyclopedia:index'))

        else:
            errors = form.errors
            form = UpdateEntryForm({'content': entry, 'title': title})
            return render(request, 'encyclopedia/entry_form.html', {
                'create': False,
                'form': form,
                'title': title,
                'errors': errors
            })


class RandomEntryView(View):
    def get(self, request):
        random_entry = choice(util.list_entries())
        return HttpResponseRedirect(reverse('encyclopedia:detail', kwargs={'title': random_entry}))
