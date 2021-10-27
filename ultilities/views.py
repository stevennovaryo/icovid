# Create your views here.
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import Announcement
from .forms import AnnouncementForm

def make_announcement(request):
	form = AnnouncementForm(request.POST or None)

	if (request.method == 'POST'):
		if (form.is_valid):
			form.save() 

    response = {'form': form}
    return render(request, 'ultilities_make_announcement.html', response)

def show_announcement(request):
	# Method will be called in home method
	# return latest announcement
	announcement = Announcement.objects.latest('pub_date')
	return announcement


import logging

# Create a logger for this file
logger = logging.getLogger(__file__)

def log_message(request):
    logger.debug("This logs a debug message.")
    logger.info("This logs an info message.")
    logger.warn("This logs a warning message.")
    logger.error("This logs an error message.")
    try:
        raise Exception("This is a handled exception")
    except Exception:
        logger.exception("This logs an exception.")

    raise Exception("This is an unhandled exception")
    return HttpResponse("this worked")

def see_log(request):
	return render(request, 'ultilities_see_log.html', response)