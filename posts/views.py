from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Post
from .forms import PostForm


def index(request):
    return render(request, 'posts/index.html', {'posts': Post.objects.all()})


def create(request):
    if request.method == 'POST':
        form = PostForm(request.POST, instance=Post())
        if form.is_valid():
            form.save()
            # @TODO add route name
            return HttpResponseRedirect('/posts/')
    else:
        form = PostForm(instance=Post())

    return render(request, 'posts/create.html', {'form': form})
