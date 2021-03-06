# -*- coding: utf-8 -*-

from smtplib import SMTPException

from django import forms
from django.core.mail import EmailMessage


class ContactForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={'type': "text", 'class': "form-control", 'name': "name", 'placeholder': "first name", 'required': ""}),
    )
    email = forms.EmailField(
        required=True,
        widget=forms.TextInput(attrs={'type': "text", 'class': "form-control", 'name': "Email", 'placeholder': "rds@example.com", 'required': ""}),
    )
    subject = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={'type': "text", 'class': "form-control", 'name': "Skill 1", 'placeholder': "https://Link.com/rds", 'required': ""}),
    )
    message = forms.CharField(
        required=True,
        widget=forms.Textarea(attrs={'type': "text", 'class': "form-control", 'name': "Letter Head", 'placeholder': "Dear Sir, ...", 'required': ""}),
    )

    def clean_subject(self):
        subject = ''.join(self.cleaned_data['subject'].splitlines())
        return subject

    def send_email(self):
        email = EmailMessage(
            self.cleaned_data['subject'],
            self.cleaned_data['message'],
            '',
            ['admin@example.com'],
            reply_to=['{name} <{email}>'.format(**self.cleaned_data)],
        )
        try:
            email.send()
            return True
        except SMTPException:
            return False
