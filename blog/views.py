from django.shortcuts import render, HttpResponse,get_object_or_404
from django.utils import timezone
from .models import Post

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
   