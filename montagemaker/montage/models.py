# -*- coding: utf-8 -*-
from django.db import models

class Montage(models.Model):
    video_file = models.FileField(upload_to='montages/%Y/%m/%d')