from django.contrib.auth.models import User

class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
    
    def clean_author(self):
        return self.cleaned_data['author'] or User()
    
    def clean_last_modified_by(self):
        return self.cleaned_data['last_modified_by'] or User()