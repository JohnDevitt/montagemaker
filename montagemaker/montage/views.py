# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from montage.models import Montage
from montage.forms import MontageUploadForm

def list(request):
    # Handle file upload
    if request.method == 'POST':
        form = MontageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            new_video = Montage(video_file = request.FILES['video_file'])
            nnew_video.save()

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