from django import forms
from django.forms import widgets
from .models import Task
from django import forms

# Reordering Form and View
class PositionForm(forms.Form):
    position = forms.CharField()

# form to render from our Model in models.py
class AddForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('title', 'jobdescription',
                  'joblink', 'interview', 'rejected')

        widgets = {
           
        }

# form class for the in progress form which contains the Google Calendar API
class CalendarForm(forms.Form):
    calendar_field = forms.DateTimeField()