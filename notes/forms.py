from django import forms
from .models import Note



class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ["title", "content"]
    
        widgets = {
            "title" : forms.TextInput(
                attrs = {
                    "placeholder" : "title",
                    "class" : "form-control",
                }
            ),
        "content" : forms.Textarea(
            attrs = {
                "placeholder" : "write your note here...",
                "rows" : 6,
                "class" : "form-control",
            }
        ),
        }
    
    def clean_title(self):
        title = self.cleaned_data["title"].strip()
        if len(title) < 3:
            raise forms.ValidationError("title most be at least 3 characters long")
        return title