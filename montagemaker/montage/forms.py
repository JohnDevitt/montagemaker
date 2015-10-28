# -*- coding: utf-8 -*-
from django import forms

class MontageUploadForm(forms.Form):
    video_file = forms.FileField(
        label='Select a file',
        help_text='max. 42 megabytes'
    )

class VideoUploadForm(forms.Form):
	video_file = forms.FileField(
		label='select a file',
		help_text='max. 42 megabytes'
	)