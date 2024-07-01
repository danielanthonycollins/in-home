from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['full_name', 'email', 'subject', 'enquiry']

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
