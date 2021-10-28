from django.http import response
from django.shortcuts import render
from django.http.response import HttpResponse
from .forms import FilterForm

# Create your views here.
def index(request):
    response = {"number_of_data" : 7, "chart_type" : 2, "form" : FilterForm()}
    return render(request, "tracker_index.html", response)