from django.shortcuts import render, redirect
from . form import AuthorForm
# Create your views here.
def add_author(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            form.save()
            return redirect('author_page')
    else:
        form = AuthorForm()
    return render(request, 'add_author.html', {'form': form})