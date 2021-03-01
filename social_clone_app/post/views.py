from django.shortcuts import render, redirect, get_object_or_404
from . import models
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.urls import reverse
from post.models import Stream, Post, Tag, Likes, PostFileContent
from post.forms import NewPostForm
from comment.models import Comment
from comment.forms import CommentForm
# Create your views here.


@login_required
def Index(request):
    user = request.user

    posts = Stream.objects.filter(user=user)
    groups_id = []
    for post in posts:
        groups_id.append(post.post_id)

    post_items = Post.objects.filter(
        id__in=groups_id).all().order_by('-posted')
    template = loader.get_template('index.html')
    # print(post_items[0].content)
    context = {
        'post_items': post_items,
    }

    return HttpResponse(template.render(context, request))


@login_required
def NewPost(request):
    user = request.user
    tags_objs = []
    files_objs = []

    if request.method == 'POST':
        form = NewPostForm(request.POST, request.FILES)
        if form.is_valid():
            files = request.FILES.getlist('content')
            caption = form.cleaned_data.get('caption')
            tags_form = form.cleaned_data.get('tags')
            tags_list = list(tags_form.split(','))

            for tag in tags_list:
                t, created = Tag.objects.get_or_create(title=tag)
                tags_objs.append(t)

            for file in files:
                file_instance = PostFileContent(file=file, user=user)
                file_instance.save()
                files_objs.append(file_instance)

            p, created = Post.objects.get_or_create(caption=caption, user=user)
            p.tags.set(tags_objs)
            p.content.set(files_objs)
            p.save()
            return redirect('post:index')
    else:
        form = NewPostForm()

    context = {
        'form': form,
    }

    return render(request, 'newpost.html', context)


@login_required
def PostDetails(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    user = request.user
    print(user)
    comment = Comment.objects.filter(post=post).order_by('date')
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.user = user
            comment.save()

            return HttpResponseRedirect(reverse('postdetails', args=[post_id]))
    else:
        form = CommentForm()
    template = loader.get_template('post_detail.html')

    context = {
        'post': post,
        'comment': comment,
        'form': form,
    }

    return HttpResponse(template.render(context, request))
