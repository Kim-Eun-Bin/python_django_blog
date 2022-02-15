from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.utils import timezone

from blog.models import Post
from blog.forms import PostModelForm


def post_new(request):
    post_form = PostModelForm()
    return render(request, 'blog/post_edit.html', {'form': post_form})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post_key': post})


def post_list(request):
    my_name = 'django web framework'
    http_method = request.method

    # return HttpResponse('''
    #     <h2>Welcome {name}</h2>
    #     <p>Http Method : {method}</p>
    #     <p>Http Headers : {header}</p>
    #     <p>Http Path : {mypath}</p>
    # '''.format(name=my_name, method=http_method, header = request.headers['user-agent'], mypath=request.path))

    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'blog/post_list.html', {'post_list': posts})