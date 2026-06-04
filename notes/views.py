from django.shortcuts import render
from django.views.generic import ListView
from .models import Note
# Create your views here.

class NoteListView(ListView):
    model = Note
    template_name = 'notes/note_list.html'
    context_object_name = 'notes'