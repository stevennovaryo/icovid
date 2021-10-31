from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.http import HttpResponse

# Create your views here.
def index(request):
    forumPost = ForumPost.objects.all()
    response = {'forumPost': forumPost}
    return render(request, 'forumHome.html', response)

# TODO: implement function that will post to forum
def post_to_forum(request):
    form = ForumForm(request.POST)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('/forum/')
    
    context = dict()
    context["form"] = form
    return render(request, "postToForum.html", context)

# TODO: Implement function that will view individual post
def forum_post_detail(request, slug):
    # return HttpResponse(slug)

    forumPost = ForumPost.objects.get(slug=slug)
    return render(request, 'forumDetail.html', {'forumPost':forumPost})