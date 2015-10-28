# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.core.urlresolvers import reverse

from montage.models import Montage
from montage.forms import MontageUploadForm

def list(request):
    # Handle file upload
    if request.method == 'POST':
        form = MontageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            new_video = Montage(video_file = request.FILES['video_file'])
            new_video.save()

            # Redirect to the document list after POST
            return HttpResponseRedirect(reverse('montage.views.list'))
    else:
        form = MontageUploadForm() # A empty, unbound form

    # Load documents for the list page
    montages = Montage.objects.all()

    # Render list page with the documents and the form
    return render_to_response(
        'montage/list.html',
        {'montages': montages, 'form': form},
        context_instance=RequestContext(request)
    )

def build(request):
    # Handle file upload
    if request.method == 'POST':
        form_one = VideoUploadForm(request.POST, request.FILES)
        if form_one.is_valid():
            video_one = Montage(video_file = request.FILES['video_file'])

        form_two = VideoUploadForm(request.POST, request.FILES)
        if form_two.is_valid():
            video_two = Montage(video_file = request.FILES['video_file'])

    else:
        form_one = 5 # A empty, unbound form
        form_two = 6

    # Render list page with the documents and the form
    return render_to_response(
        'montage/build.html',
        {'form_one': form_one, 'form_two': form_two},
        context_instance=RequestContext(request)
    )