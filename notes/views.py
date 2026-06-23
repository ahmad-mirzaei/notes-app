from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView
from .models import Note
from .forms import NoteForm
# Create your views here.

class NoteListView(ListView):
    model = Note
    template_name = "notes/note_list.html"
    context_object_name = 'notes'


class NoteCreateView(CreateView):
    form_class = NoteForm
    template_name = "notes/note_form.html"
    success_url = reverse_lazy("note-list")


class NoteUpdateView(UpdateView):
    model = Note
    form_class = NoteForm
    template_name = "notes/note_form.html"
    success_url = reverse_lazy("note-list")
