from django.urls import path
from .views import NoteListView, NoteCreateView, NoteUpdateView

urlpatterns = [
    path('', NoteListView.as_view(), name = 'note-list'),
    path('create/', NoteCreateView.as_view(), name = 'note-create'),
    path("<int:pk>/update/", NoteUpdateView.as_view(), name = 'note-update'),
    
]