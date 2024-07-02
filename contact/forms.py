from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['full_name', 'email', 'subject', 'enquiry']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields:
            if field == 'enquiry':
                self.fields[field].widget.attrs['class'] = 'extra-form-label-styling-tall'
            else: 
                self.fields[field].widget.attrs['class'] = 'extra-form-label-styling'
