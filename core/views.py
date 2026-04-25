from django.shortcuts import render, redirect
from django import forms
from django.contrib import messages


def index(request):
    return render(request, 'index.html')


class ContactForm(forms.Form):
    nome = forms.CharField(max_length=100)
    email = forms.EmailField()
    mensagem = forms.CharField(widget=forms.Textarea)


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # ... lógica de envio de e-mail ou salvar no banco ...

            # 2. Adicione a mensagem de sucesso
            messages.success(request, 'Sua mensagem foi enviada com sucesso!')
            return redirect('contact')
        else:
            # 3. Adicione uma mensagem de erro (opcional, o form já mostra erros)
            messages.error(request, 'Erro ao preencher o formulário.')
    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})
