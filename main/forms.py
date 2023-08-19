from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(label="First name", max_length=100, widget=forms.TextInput(attrs={
        "class": "form-control",
        "labelClass": "sr-only",
        "placeholder": "First name...",
        "rows": '1',
        }))

    email = forms.EmailField(label="Email", max_length=100, widget=forms.EmailInput(attrs={
        "class": "form-control",
        "labelClass": "sr-only",
        "placeholder": "Email...",
        }))

    subject = forms.CharField(label="Subject", max_length=100, widget=forms.TextInput(attrs={
        "class": "form-control",
        "labelClass": "sr-only",
        "placeholder": "Subject...",
        "rows": '1',
        }))

    message = forms.CharField(widget=forms.Textarea(attrs={
        "class": "form-control",
        "labelClass": "sr-only",
        "placeholder": "Write text here...",
        "rows": '12',
        }))
