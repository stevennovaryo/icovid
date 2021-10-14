# temporary file for hello world!
from django.http import HttpResponse

def index(request):
  return HttpResponse("<H1>Hello World</H1>")