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

## entries/

Directory where the encyclopedia entries are stored.

## scss/

Directory where **scss** files are held. Contains **\_main.scss**, **style.scss**, and **font-awesome**, a directory for FontAwesome icons.

## static/

Directory for static assets. Contains the folder **scss/**, which holds the **style.css** file.

## templates

The template folder.

### \_base.html

The layout template.

### 404.html

The template that is displayed when an entry is not found.

### 500.html

The template that is displayed when there is a server error.

### encyclopedia/

#### detail.html

The template that shows the detail for an entry.

#### search.html

The template that shows the search results, if there are multiple results.

#### index.html

The template that shows all of the encyclopedia entries.

#### entry_form.html

Template that is rendered when an entry is edited or created.

## .gitignore

Items ingnored by git.

## manage.py

Script used to run Django tasks.

## package.json

An npm file. Used to install **node-scss** and **bootstrap**. Also contains a script to run the **scss** compiler (`npm run scss`)

## requirements.txt

File containing all of the python packages needed for the application.
