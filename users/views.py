from django.shortcuts import render, redirect
from .forms import CustomUserCreateForm


def register(request):

    if request.method == 'POST':
        form = CustomUserCreateForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('login')

    else:
        form = CustomUserCreateForm()

    return render(request, 'registration/register.html', {
        'form': form
    })
