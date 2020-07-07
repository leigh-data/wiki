# Wiki

[Website](https://wiki.devgrue.com)
[GitHub](https://github.com/leigh-data/wiki)
[YouTube](https://youtube.com)

---

This Django web application displays, creates, and updates different encyclopedia articles stored in individual markdown files. [home page](https://wiki.devgrue.com) displays all of the application's pages in an unordered list. The sidebar contains a search form for discovering encyclopedia entries. Underneath the form are links for the home page, create entry, and get random entry pages. Any user may look up, edit, and create encyclopedia entries in markdown format. All script tags are escaped out.

---

## core/

The main Django directory.

**asgi.py** - The main ASGI file.

**settings.py** - The main settings file.

**urls.py** - The main url file.

**wsgi.py** - The main WSGI file.

## encyclopeida/

The main app of the project.

**/templatetags** - Directory containing a template tag. The lone custom template tag is **markdown**.

### markdown.py

The Python file conataining **markdown**, a template tag that converts markdown-formatted text into HTML.

## tests/

Directory containing pytest tests.

## apps.py

File that contains used to install the app in **core/settings.py.**

## forms.py

File that contains two Django forms: CreateEntryForm and UpdateEntryForm.

## urls.py

File that contains urls specific for this app.

## util.py

File that creates, updates, and retrieves (individual and all) entries.

## views.py

File that contains all of the views for the encyclopedia application. All views inherit from the **views.View** class. The views are: EntryIndexView, EntryDetailView, RandomEntryView, EntryCreateView, and EntryUpdateView
