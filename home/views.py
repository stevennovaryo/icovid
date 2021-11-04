from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from home.forms import FeedbackForm
from home.models import Feedback
from news.models import Article
from django.contrib.auth.models import User


def index(request):
    
    feedbacks = Feedback.objects.all().order_by("-created_at")[:4]
    feedbacksAll = Feedback.objects.filter(user_id = request.user.id)
    articleList = Article.objects.all()[::-1]
    # articleList = articleList[:3]
    firstArticle = articleList[0]
    secondArticle = articleList[1]
    thirdArticle = articleList[2]
    firstURL = firstArticle.title.replace(" ","%20") 
    secondURL = secondArticle.title.replace(" ","%20") 
    thirdURL = thirdArticle.title.replace(" ","%20") 
    context ={'feedbacks':feedbacks,'feedbacksAll':feedbacksAll,'firstArticle':firstArticle,'secondArticle':secondArticle,'thirdArticle':thirdArticle,'firstURL':firstURL,'secondURL':secondURL,
    'thirdURL':thirdURL}
    # create object of form
    form = FeedbackForm(request.POST or None, request.FILES or None)
      
    # check if form data is valid
    if form.is_valid():
        # save the form data to model
        data = form.save(commit=False) #bisa return object
        try :
            data.user_id = User.objects.get(id=request.user.id)
        except:
            return HttpResponseRedirect("/home/")

        data.save()
        if request.method == 'POST':
          return HttpResponseRedirect("/home/")
  
    context['form']= form
    return render(request, "home2.html", context)

def edit_feedback(request):
  print(request)
  if (request.method == "POST"):
    id = request.POST.get("id")
    message = request.POST.get("message")
    ratings = request.POST.get("ratings")
      
    feedback = Feedback.objects.get(id=id)
    feedback.message = message
    feedback.ratings = ratings
    feedback.save()

  return HttpResponseRedirect("/home/")

def delete_feedback(request):
    if (request.method == "POST"):
        id = request.POST.get("id")
        Feedback.objects.filter(id=id).delete()
    return HttpResponseRedirect("/home/")

