# from django.core.files.uploadedfile import SimpleUploadedFile
# from django.db import models
from django import forms


class CatForm(forms.Form):
    picture = forms.ImageField()
    left_eye_x = forms.IntegerField()
    left_eye_y = forms.IntegerField()
    right_eye_x = forms.IntegerField()
    right_eye_y = forms.IntegerField()
