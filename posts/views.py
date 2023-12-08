from django.shortcuts import render, redirect
from . form import PostForm
from . models import Post

# Create your views here.
def add_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            form.save()
            return redirect('post_page')
    else:
        form = PostForm()
    return render(request, 'add_post.html', {'form': form})

def edit_post(request, id):
    post = Post.objects.get(pk = id)
    form = PostForm(instance=post)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            print(form.cleaned_data)
            form.save()
            return redirect('home_page')
    return render(request, 'add_post.html', {'form': form})

def delete_post(request, id):
    Post.objects.get(pk = id).delete()
    return redirect('home_page')