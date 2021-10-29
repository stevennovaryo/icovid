from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from profileapp.forms import ProfileUpdateForm, UserUpdateForm
from profileapp.models import Profile
from django.core import serializers
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods

# Create your views here.
def profile(request):
    return render(request, 'main_profile.html')

@login_required
def profileupdate(request):
    if request.method == "POST":
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
        #     messages.success(request, ('Your profile has been updated!'))
        # else:
        #     messages.error(request, ('Unable to update your profile'))
        return redirect('user-profile') # reverse
    
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)
        
    context = {
        'user_form' : user_form,
        'profile_form' : profile_form,
    }

    return render(request, 'edit_profile.html', context)

def profiledatas(request):
    form = Profile.objects.all()
    data = serializers.serialize('json', form)
    return HttpResponse(data, content_type="application/json")