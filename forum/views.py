from django.shortcuts import render, redirect
from .models import *
from .forms import *

# Create your views here.
def index(request):
    forumPost = ForumPost.objects.all()
    response = {'forumPost': forumPost}
    return render(request, 'forumHome.html', response)

# TODO: implement function that will post to forum
def post_to_forum(request):
    form = ForumForm(request.POST)

    if form.is_valid() and request.method == 'POST':
        form.save()
        return redirect('/forum/')
    
    context = dict()
    context["form"] = form
    return render(request, "postToForum.html", context)

# TODO: Implement function that will view individual post
def individualForumPost(request):
    pass