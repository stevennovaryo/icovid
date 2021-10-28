from django import forms
from django.http import response
from django.shortcuts import render
from django.http.response import HttpResponse
from .forms import FilterForm
from .models import TrackerFilter

# Create your views here.
def index(request):
    response = None
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = FilterForm(request.POST)
            if form.is_valid():
                chartType = form.cleaned_data['chart_type']
                numberOfData = form.cleaned_data['number_of_data']
                tmp = TrackerFilter(user=request.user, chart_type=chartType, number_of_data=numberOfData)
                tmp.save()
        else:
            if not hasattr(request.user, 'trackerfilter'):
                tmp = TrackerFilter(user=request.user, chart_type=1, number_of_data=7)
                tmp.save()
        tmp = TrackerFilter.objects.get(user=request.user)
        response = {
            "number_of_data" : tmp.number_of_data,
            "chart_type" : tmp.chart_type,
            "form" : FilterForm({
                'chart_type' : tmp.chart_type,
                "number_of_data" : tmp.number_of_data
            })
        }
    else:
        response = {"number_of_data" : 7, "chart_type" : 1, "form" : FilterForm()}
    
    return render(request, "tracker_index.html", response)