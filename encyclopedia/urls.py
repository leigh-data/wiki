from django.urls import path

from . import views

app_name = "encyclopedia"

urlpatterns = [
    path('', views.EntryIndexView.as_view(), name='index'),
    path('search/', views.EntrySearchView.as_view(), name='search'),
    path('random/', views.RandomEntryView.as_view(), name='random'),
    path('create/', views.EntryCreateView.as_view(), name='create'),
    path('<title>', views.EntryDetailView.as_view(), name='detail'),
    path('<title>/update/', views.EntryUpdateView.as_view(), name='update'),
]
