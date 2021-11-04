import collections
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from news.forms import articleForm
from news.models import Article
from django.core import serializers
from django.http import JsonResponse

# Create your views here.
def index(request):

    articleList = list(Article.objects.all())
    firstArticle = articleList[len(articleList) - 1]
    nextThreeArticles = articleList[len(articleList) - 4:len(articleList) - 1]
    nextThreeArticles = nextThreeArticles[::-1]

    context = {
        'firstArticle' : firstArticle,
        'nextThreeArticles' : nextThreeArticles,
    }
    return render(request, 'news-home.html', context)

def read(request, id):
    article = Article.objects.get(title=id)
    context = {
        'article' : article
    }
    return render(request, 'news-read.html', context)

@login_required(login_url='/admin/login/')
def postArticle(request):
    context = {}
    if request.method == "POST":
        form = articleForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/news')
    else:
        form = articleForm()
    context['form'] = form
    return render(request, "article-post.html", context)

def load_more(request):

    articleQuer = Article.objects.all()
    articleQuer = articleQuer[::-1]
    articleQuer = articleQuer[1::]

    offset=int(request.POST['offset'])
    limit=3
    posts=articleQuer[offset:limit+offset]
    totalData=Article.objects.count() - 1
    data={}
    posts_json=serializers.serialize('json', posts)
    return JsonResponse(data={
        'posts':posts_json,
        'totalResult':totalData
    })