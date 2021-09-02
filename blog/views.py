from django.shortcuts import render, HttpResponse,get_object_or_404,redirect
from django.utils import timezone
from .models import Post
from .forms import PostForm

def home(request):
    return HttpResponse('hello world')

def post_list(request):
    post = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    context = {'posts': post}
    return render(request, 'blog/post_list.html', context)


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk) 
    context = {'post': post}
    return render(request, 'blog/post_detail.html', context)


def post_new(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
        return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
        context = {'form': form}
        return render(request, 'blog/post_edit.html', context )
   

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
        return render(request, 'blog/post_edit.html', {'form': form})


def post_draft_list(request):
    posts = Post.objects.filter(published_date__isnull=True).order_by('created_date')
    context = {'posts': posts}
    return render(request, 'blog/post_draft_list.html', context)
    
def post_publish(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.publish()
    return redirect('post_detail', pk=pk)

def post_remove(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('post_list')