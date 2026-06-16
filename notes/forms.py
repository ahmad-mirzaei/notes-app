from django import forms
from .models import Note



class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ["title", "content"]
    
    def clean_title(self):
        title = self.cleaned_data["title"].strip()
        if len(title) < 3:
            raise forms.ValidationError("title most be at least 3 characters long")
        return title