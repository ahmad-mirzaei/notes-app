from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from .models import Note
from .forms import NoteForm
from django.db.models import Q
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


class NoteDeleteView(DeleteView):
    model = Note
    template_name = "notes/note_confirm_delete.html"
    success_url = reverse_lazy("note-list")


class NoteDetailView(DetailView):
    model = Note
    template_name = "notes/note_detail.html"
    context_object_name ='note'

class NoteListView(ListView):
    model = Note
    template_name = "notes/note_list.html"
    context_object_name = "notes"

    def get_queryset(self):
        query = self.request.GET.get("q")

        if query:
            return Note.objects.filter(
                Q(title__icontains=query) |
                Q(content__icontains=query)
            )

        return Note.objects.all()