from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.conf import settings
from news.forms import articleForm
from news.models import Article

# Create your views here.
def index(request):
    articleList = list(Article.objects.all())
    firstArticle = articleList[len(articleList) - 1]
    remainingArticles = articleList[:len(articleList) - 1]
    remainingArticles = remainingArticles[::-1]

    response = {
        'firstArticle' : firstArticle,
        'remainingArticles' : remainingArticles
    }
    return render(request, 'news-home.html', response)

def read(request):
    return render(request, 'news-read.html')

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