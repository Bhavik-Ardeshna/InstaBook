from django.shortcuts import render, redirect
from . import models
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.urls import reverse
from post.models import Stream, Post, Tag, Likes, PostFileContent
from post.forms import NewPostForm
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

    user = request.user.id
    tags_obj = []
    if request.method == 'POST':
        form = NewPostForm(request.POST or None, request.FILES or None)
        # check if form data is valid
        if form.is_valid():
            picture = request.cleaned_data.get('content')
            caption = request.cleaned_data.get('caption')
            tags_form = request.cleaned_data.get('tags')

            tags_list = list(tags_form.split(','))

            for tags in tags_list:
                t, created = Tag.objects.get_or_create(title=tag)
                tags_obj.append(t)
            p, created = Post.objects.get_or_create(
                content=picture, caption=caption, id=user)
            p.tags.set(tags_obj)
            p.save()
            return redirect('index')
    else:
        form = NewPostForm()
    context = {
        'form': form,
    }
    return render(request, 'newpost.html', context)
