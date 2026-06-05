from django.urls import path
from .views import NoteListView, NoteCreateView

urlpatterns = [
    path('', NoteListView.as_view(), name = 'note-list'),
    path('create/', NoteCreateView.as_view(), name = 'note-create'),
    
]