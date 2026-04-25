from django import forms
from django.core.mail.message import EmailMessage


class ContactForm(forms.Form):
    name = forms.CharField(label='Name', max_length=100, min_length=10)
    email = forms.EmailField(label='E-mail', max_length=100)
    subject = forms.CharField(label='Subject', max_length=200)  # assunto
    message = forms.CharField(label='Message', widget=forms.Textarea())

    def send_mail(self):
        name = self.cleaned_data['name']
        email = self.cleaned_data['email']
        subject = self.cleaned_data['subject']
        message = self.cleaned_data['message']

        content = f'Name: {name}\nE-mail: {email}\nSubject: {subject}\nMessage: {message}'

        mail = EmailMessage(
            subject='E-mail sended by Django2',
            body=content,
            from_email='contact@yourdomin.com',
            to=['contact@yourdomin.com',],
            headers={'Replay-To': email}
        )
        mail.send()
